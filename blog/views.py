# coding: utf-8

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.core.paginator import Paginator

from taggit.models import Tag

from models import Blog, Category

def index(request):
    posts_list = Blog.objects.all()
    posts_list = pager(request, posts_list, 5)
    return response(request, 'blog/index.html', locals())


def post(request, year, month, slug):
    post = get_object_or_404(Blog, slug=slug, pub_date__year=int(year), \
                                pub_date__month=int(month))

    post_link = request.get_host() + post.get_absolute_url()

    return response(request, 'blog/blog.html', locals())


def blogs(request):
    posts_list = Blog.objects.all()
    posts_list = pager(request, posts_list, 20)

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


def tags(request, tag):
    tag = get_object_or_404(Tag, name=tag)
    posts_list = Blog.objects.filter(tags__name__in=[tag])

    return response(request, 'blog/tag.html', locals())


def about(request):
    return response(request, 'blog/about.html', locals())


def pager(request, lst, num_per_page):
    paginator = Paginator(lst, num_per_page)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        lst = paginator.page(page)
    except Exception:
        lst = paginator.page(paginator.num_pages)

    return lst


def response(request, template, args):
    t = get_template(template)
    c = RequestContext(request, args)
    return HttpResponse(t.render(c))