# coding: utf-8

from django.http import  HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.core.paginator import Paginator

from taggit.models import Tag

from .models import Blog, Category

def index(request):
    """ 首页，分页显示所有的博客文章，每页5篇。
    """
    posts_list = Blog.objects.all()
    posts_list = pager(request, posts_list, 5)
    return response(request, 'blog/index.html', locals())


def post(request, year, month, slug):
    """ 每篇博客的页面，URL 包含三个参数用于从数据库取出请求的对象，
        同时获取前后两篇（如果有的话）
    """
    post = get_object_or_404(Blog, slug=slug, pub_date__year=int(year), \
                                pub_date__month=int(month))

    post_link = request.get_host() + post.get_absolute_url()

    try:
        next_post = Blog.get_next_by_pub_date(post)
    except Blog.DoesNotExist:
        next_post = None

    try:
        previous_post = Blog.get_previous_by_pub_date(post)
    except Blog.DoesNotExist:
        previous_post = None

    return response(request, 'blog/blog.html', locals())


def blogs(request):
    """ 博客列表，按标题分页列出所有博客，每页20条记录。
    """
    posts_list = Blog.objects.all()
    posts_list = pager(request, posts_list, 20)

    return response(request, 'blog/blogs.html', locals())


def category(request, slug):
    """ 列出该分类下的所有文章
    """
    category = get_object_or_404(Category, slug=slug)
    blogs = category.blogs.all()

    return response(request, 'blog/category.html', locals())

def archive(request, year, month):
    """ 按时间归档，列出该归档下的所有文章
    """
    archive = year + u' 年 ' + month + u' 月'
    posts_list = get_list_or_404(Blog, pub_date__year=int(year), \
                                pub_date__month=int(month))

    return response(request, 'blog/archive.html', locals())


def tags(request, tag):
    """ 按标签获取文章
    """
    tag = get_object_or_404(Tag, name=tag)
    posts_list = Blog.objects.filter(tags__name__in=[tag])

    return response(request, 'blog/tag.html', locals())


def about(request):
    """ 单页面，应该有更好的处理方式。
    """
    return response(request, 'blog/about.html', locals())


def pager(request, lst, num_per_page):
    """ 辅助函数，用于分页
    """
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
    """ 辅助函数，由于每个view都需要 获取模板-替换上下文-返回 这几个步骤，
        所以做了这个函数来完成这些工作。
    """
    t = get_template(template)
    c = RequestContext(request, args)
    return HttpResponse(t.render(c))