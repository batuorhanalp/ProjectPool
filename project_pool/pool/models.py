# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField("İsim", max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        """string representation of the model"""
        return self.name

    def get_absolute_url(self):
        return reverse('pool:cms_brand_list')


class Category(models.Model):
    name = models.CharField("Kategori Adı", max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        """string representation of the model"""
        return self.name

    def get_absolute_url(self):
        return reverse('pool:cms_category_list')


class Budget(models.Model):
    start = models.PositiveIntegerField("Başlangıç Fiyatı")
    end = models.PositiveIntegerField("Bitiş Fiyatı")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['start', 'end']

    def __unicode__(self):
        """string representation of the model"""
        return "$%s - $%s" % (self.start, self.end)

    def get_absolute_url(self):
        return reverse('pool:cms_budget_list')


class Idea(models.Model):
    name = models.CharField("Fikir Ismi", max_length=64)
    summary = models.CharField(max_length=255, blank=True)
    detail = models.TextField(blank=True)
    offerred_brands = models.ManyToManyField('Brand', related_name="+",
                                             null=True, blank=True)
    dealt_brands = models.ManyToManyField('Brand', related_name="ref+",
                                          null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name="ideas",
                                        null=True)
    budget = models.ForeignKey('Budget', null=True)
    date = models.DateTimeField("Fikir Tarihi", blank=True,
                                default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = EmbeddedModelField('User')

    def __unicode__(self):
        """string representation of the model"""
        return self.name

    def get_absolute_url(self):
        return reverse('pool:cms_idea_details', kwargs={
            'pk': self.id
        })
