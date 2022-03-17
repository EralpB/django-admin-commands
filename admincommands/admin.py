from django.contrib import admin
from django import forms
from django.apps import apps

from .models import CommandRunInstance


@admin.register(CommandRunInstance)
class CommandRunInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'command', 'executed_at', )
    raw_id_fields = ('runner_user',)
    def get_exclude(self, request, obj=None):
        if not obj:
            return ('runner_user', 'stdout', 'stderr', 'exception',)
        return super().get_exclude(request, obj)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('runner_user', 'command', 'stdout', 'stderr', 'exception', 'executed_at', 'finished_at',)
        return super().get_readonly_fields(request, obj)

    def save_model(self, request, instance, form, change):
        instance.runner_user = request.user
        return super().save_model(request, instance, form, change)