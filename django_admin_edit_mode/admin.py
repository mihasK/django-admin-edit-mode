from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin


def _is_edit_mode(request):
    # We need this restriction only on rendering of the page, so we check that request method is GET
    # Also we always allow adding of objects and changing lists, so skipping if it's not a change-obj page
    return (request.method != 'GET') \
        or request.GET.get('edit_mode') \
           or not is_a_change_object_page(request)


def is_a_change_object_page(request):
    return request.path.rstrip('/').endswith('/change')


class EditModeAdminMixin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and _is_edit_mode(request)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):

        if is_a_change_object_page(request):
            extra_context = extra_context or dict()
            extra_context['edit_mode_exists'] = True
            extra_context['edit_mode'] = request.GET.get('edit_mode')
        return super().changeform_view(request, object_id, form_url, extra_context)

    def get_inline_instances(self, request, obj=None):
        def add_mixin(C):
            if not issubclass(C, _EditModeInlineAdminMixin):
                return type(C.__name__ + '_EditMode', (_EditModeInlineAdminMixin, C), {})
            else:
                return C
        self.inlines  = [
            add_mixin(c)
            for c in self.inlines
        ]
        return  super().get_inline_instances(request, obj)



class _EditModeInlineAdminMixin(InlineModelAdmin):

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and _is_edit_mode(request)
    
    def has_add_permission(self, request, obj=None):
        return super().has_add_permission(request, obj) and _is_edit_mode(request)


