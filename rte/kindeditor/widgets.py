from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.template import RequestContext

class KindEditor(forms.Textarea):

    class Media:
        css = {
            'all': (settings.STATIC_URL + 'editor/kindeditor-4.0.1/themes/default/default.css',
                    settings.STATIC_URL + 'editor/kindeditor-4.0.1/plugins/code/prettify.css',),
        }

        js = (
            settings.STATIC_URL + 'editor/kindeditor-4.0.1/kindeditor.js',
            settings.STATIC_URL + 'editor/kindeditor-4.0.1/plugins/code/prettify.js',
        )

    def __init__(self, attrs = {}):
        attrs['rel'] = 'kind'
        super(KindEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(KindEditor, self).render(name, value, attrs)
        context = {
            'name': name,
            'STATIC_URL': settings.STATIC_URL,
        }
        return rendered + mark_safe(render_to_string('editor/kindeditor.html', context))