# coding:utf-8

__author__ = 'leon'

from django.template import Library

from blog.models import Blog
from blog.models import Category

register = Library()

@register.inclusion_tag("blog/sidebar_items/latest.html")
def latest_posts():
    latest_posts = Blog.objects.select_related(depth=1).order_by("-pub_date")
    return {
        'template': "blog/sidebar/items/latest.html",
        'latest_posts': latest_posts[:5],
    }


@register.inclusion_tag("blog/sidebar_items/categories.html")
def categories():
    ''' 自定义的 包含标签，用于显示所有的分类 '''
    return {
        'template': "blog/sidebar_items/categories.html",
        'categories': Category.objects.order_by('title'),
    }


@register.inclusion_tag("blog/sidebar_items/archives.html")
def archives():
    return {
        'template': "blog/sidebar_items/archives.html",
        'archives': Blog.objects.dates('pub_date', 'month')[:12],
    }
    pass
