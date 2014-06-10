# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from djangotoolbox.fields import (
    EmbeddedModelField
)
from .fields import EmbeddedModelListField


class Brand(models.Model):
    name = models.CharField("İsim", max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """string representation of the model"""
        return self.name

    def get_absolute_url(self):
        return reverse('pool:cms_brand_list')


class Category(models.Model):
    name = models.CharField("Kategori Adı", max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

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
    offerred_brands = EmbeddedModelListField(EmbeddedModelField('Brand'),
                                             blank=True)
    dealt_brands = EmbeddedModelListField(EmbeddedModelField('Brand'),
                                          blank=True)
    categories = EmbeddedModelListField(EmbeddedModelField('Category',
                                                           blank=True))
    budget = EmbeddedModelField('Budget', null=True, blank=True)
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

    def save(self, *args, **kwargs):
        """
        somehow model id's won't be mapped to their model instances
        this is a hack to solve this issue
        TODO: look at mongodb-nonrel docs to solve this issue
        """
        if isinstance(self.budget, basestring):
            self.budget = Budget.objects.filter(id=self.budget)[0]

        for i, category in enumerate(self.categories):
            if isinstance(category, basestring):
                self.categories[i] = Category.objects.filter(id=category)[0]

        for i, dealt_brand in enumerate(self.dealt_brands):
            if isinstance(dealt_brand, basestring):
                self.dealt_brands[i] = Brand.objects.filter(id=dealt_brand)[0]

        for i, offerred_brand in enumerate(self.offerred_brands):
            if isinstance(offerred_brand, basestring):
                self.offerred_brands[i] = Brand.objects.filter(id=offerred_brand)[0]

        super(Idea, self).save(*args, **kwargs)
