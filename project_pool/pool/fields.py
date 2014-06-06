from django import forms
from django.db import models
from djangotoolbox.fields import ListField


class StringListField(forms.CharField):
    u"""
    Taken from: https://gist.github.com/jonashaag/1200165
    """
    def prepare_value(self, value):
        return ', '.join(value)

    def to_python(self, value):
        if not value:
            return []
        return [item.strip() for item in value.split(',')]


class EmbeddedModelListField(ListField):
    u"""
    Taken from: https://gist.github.com/jonashaag/1200165
    """
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)