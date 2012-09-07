from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template

from models import Blog, Category

def post(request, year, month, slug):
    post = get_object_or_404(Blog, slug=slug, pub_date__year=int(year), \
                                pub_date__month=int(month))
    t = get_template('blog/post.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def blogs(request):
    posts_list = Blog.objects.all()

    t = get_template('blog/blogs.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def about(request):
    t = get_template('blog/about.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))