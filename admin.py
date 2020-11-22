from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin


class EditModeAdminMixin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and request.GET.get('edit_mode')

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or dict()
        extra_context['edit_mode_exists'] = True
        extra_context['edit_mode'] = request.GET.get('edit_mode')
        return super().changeform_view(request, object_id, form_url, extra_context)


class EditModeInlineAdminMixin(InlineModelAdmin):


    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and request.GET.get('edit_mode')
    #
    def has_add_permission(self, request, obj=None):
        return super().has_add_permission(request, obj) and request.GET.get('edit_mode')

