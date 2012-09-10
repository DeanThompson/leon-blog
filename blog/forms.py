# coding:utf-8

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Blog
from rte.kindeditor.widgets import KindEditor

class MyBlogAdminForm(forms.ModelForm):
    content = forms.CharField(label=_(u"Content"), \
        widget=KindEditor(attrs={'row': 15, 'cols': 100}), required=True)

    class Meta:
        model = Blog
