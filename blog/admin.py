# coding:utf-8

__author__ = 'leon'

from django.contrib import admin
from django import forms

from .models import Blog, Category
from rte.kindeditor.widgets import KindEditor


class MyBlogAdminForm(forms.ModelForm):
    #content = forms.CharField(label="Content", widget=KindEditor(attrs={'row': 15, 'cols': 100}), required=True)

    class Meta:
        model = Blog
        widgets = {
            'content': KindEditor(attrs={'row': 15, 'cols': 100})
        }


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date', 'category',)
    search_fields = ('title', 'content',)
    list_filter = ('category', 'pub_date',)

    form = MyBlogAdminForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title', 'slug',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)