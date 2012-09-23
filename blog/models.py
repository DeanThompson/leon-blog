# coding: utf-8

from django.db import models

from taggit.managers import TaggableManager

from datetime import datetime


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name = ('category')
        verbose_name_plural = ('categories')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return 'leon_category', None, {'slug': self.slug}
    get_absolute_url = models.permalink(get_absolute_url)


class Blog(models.Model):
    title = models.CharField("标题", max_length=200)
    content = models.TextField("内容")
    slug = models.SlugField()   # more readable url
    category = models.ForeignKey(Category, related_name='blogs', blank=True, \
                    null=True, default=None, on_delete=models.SET_NULL)
    tags = TaggableManager("标签", blank=True)
    pub_date = models.DateTimeField("发布时间", default=datetime.now())

    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name = ('blog')
        verbose_name_plural = ('blogs')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return 'leon_blog', None, {'year': self.pub_date.year,
                                   'month': '%02d' % self.pub_date.month,
                                   'slug': self.slug}
    get_absolute_url = models.permalink(get_absolute_url)
