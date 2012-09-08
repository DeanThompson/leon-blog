# coding:utf-8

__author__ = 'leon'

from django.db import models
from django.contrib import admin

from models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date', 'category',)
    search_fields = ('title', 'content',)
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title', 'slug',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)