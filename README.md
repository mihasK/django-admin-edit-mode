# djang-admin-edit-mode

The intention of this library is provide a possibility to open objects in django-admin in read-only mode by default,
with a special button "Go to edit mode" to open the same change-object page in regular editable mode.

Why read-only mode in the beginning is needed ? For some applications, django-admin serves mostly for reading the info.
Readonly mode looks better, doesn't allow to make some changes accidentially, and the page loads quicker (no need to load a list of choices for the fields).

But despite this, sometimes you want to change the object. Then you can go to edit mode!


## Installation

* `pip install -e git+https://github.com/mihasK/djang-admin-edit-mode.git#egg=django_admin_edit_mode`
* Add `'django_admin_edit_mode'` to `INSTALLED_APPS`, **before `'django.contrib.admin'`**. Order matters for template loading!
* Install and add `'spurl'` to `INSTALLED_APPS`.
* Check that `'APP_DIRS'` is `True` in `TEMPLATES` settings.


## Usage

Use the mixins for the model admins you want to have "readonly by default and edit by clicking button" mode:

```python
import django_admin_edit_mode.admin


@admin.register(models.Respondent)
class RespondentAdmin(django_admin_edit_mode.admin.EditModeAdminMixin,
                      admin.ModelAdmin):
    inlines = (AnswerInline, )
    ...
    


class AnswerInline(django_admin_edit_mode.admin.EditModeInlineAdminMixin,
                admin.TabularInline):
      ...
 

```

Don't forget to add the special mixin to all your inlines!
