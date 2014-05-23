# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from djangotoolbox.fields import (
    ListField,
    EmbeddedModelField
)


class Brand(models.Model):
    name = models.CharField("İsim", max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField("Kategori Adı", max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)


class Budget(models.Model):
    start = models.PositiveIntegerField("Başlangıç Fiyatı")
    end = models.PositiveIntegerField("Bitiş Fiyatı")
    created_at = models.DateTimeField(auto_now_add=True)


class Idea(models.Model):
    name = models.CharField("Fikir Ismi", max_length=64)
    summary = models.CharField(max_length=255, blank=True)
    detail = models.TextField(blank=True)
    offerred_brands = ListField(EmbeddedModelField('Brand'))
    dealtBrands = ListField(EmbeddedModelField('Brand'))
    categories = ListField(EmbeddedModelField('Category'))
    budget = EmbeddedModelField('Budget', null=True)
    date = models.DateTimeField("Fikir Tarihi", blank=True, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    #created_by = EmbeddedModelField('User')
