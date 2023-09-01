from django.contrib import admin


class ConditionalListEditableAdminMixin(admin.ModelAdmin):

 
    def get_changelist_instance(self, request):
        """
        Changes list_editable property value depending on list_edit_mode *(on/off)
        """
        request.GET._mutable = True
        if not request.GET.pop('list_edit_mode', None):
            self.list_editable = ()
            is_list_edit_mode = False
        else:
            self.list_editable = self.conditional_list_editable
            is_list_edit_mode = True

        request.GET._mutable = False

        cl =  super(ConditionalListEditableAdminMixin, self).get_changelist_instance(request)
        
        cl.list_edit_mode_exist = True
        cl.is_list_edit_mode = is_list_edit_mode
        
        return cl
    
    def lookup_allowed(self, lookup, value):
        if lookup == 'list_edit_mode':
            return True
        return super(ConditionalListEditableAdminMixin, self).lookup_allowed(lookup, value)


    @property
    def conditional_list_editable(self):
        raise NotImplementedError('Specify property in your admin class. Should be a list or tuple.')

