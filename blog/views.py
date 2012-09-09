# coding: utf-8

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template


from models import Blog, Category

def index(request):
    posts_list = Blog.objects.all()

    return response(request, 'blog/index.html', locals())


def post(request, year, month, slug):
    post = get_object_or_404(Blog, slug=slug, pub_date__year=int(year), \
                                pub_date__month=int(month))

    post_link = request.get_host() + post.get_absolute_url()

    return response(request, 'blog/post.html', locals())


def blogs(request):
    posts_list = Blog.objects.all()

    return response(request, 'blog/blogs.html', locals())


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = category.blogs.all()

    return response(request, 'blog/category.html', locals())

def archive(request, year, month):
    archive = year + u' 年 ' + month + u' 月'
    posts_list = get_list_or_404(Blog, pub_date__year=int(year), \
                                pub_date__month=int(month))

    return response(request, 'blog/archive.html', locals())


def about(request):
    return response(request, 'blog/about.html', locals())


def response(request, template, args):
    t = get_template(template)
    c = RequestContext(request, args)
    return HttpResponse(t.render(c))