# django-admin-edit-mode
[![PyPI - Version](https://img.shields.io/pypi/v/django-admin-edit-mode?label=django-admin-edit-mode&link=https%3A%2F%2Fpypi.org%2Fproject%2Fdjango-admin-edit-mode%2F)](https://pypi.org/project/django-admin-edit-mode/)

Allows to open django admin in read-only mode by default,
with a special button "Go to edit mode" to open the same change-object page in regular editable mode.

Why read-only mode by default is needed ? For some applications, django-admin serves mostly for reading the info.
**Readonly mode page looks better (cleaner)**, doesn't allow to make some changes accidentially, and the **page loads quicker** (e.g., no need to load a list of choices for the fields).
But you're not going to make admin completely readonly (e.g., by persmissions), because **sometimes you still want to change** the object.
Then you can **go to edit mode by clicking the button**!

Even more suitable edit mode could be on a list page.
For quick multi-object editing you would like to enable changing of some fields on list page 
with help of [`list_editable`](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_editable). But it will alsways shows you edit mode on list page,
which looks not good (for most times you don't want to change, only look).
This libary provides you with buttons "Go Edit Mode" / "Go Readonly Mode".
Important note: your editable field should not serve as a link to the object, i.e., should not be in `list_display_links` or be the first field of `list_display` (the same restriction applies to regular Django's `list_editable`).

## Installation

* `pip install django-admin-edit-mode`
* Add `'django_admin_edit_mode'` to `INSTALLED_APPS`, **before `'django.contrib.admin'`**. Order matters for template loading!
* Add `'spurl'` to `INSTALLED_APPS`.
* Check that `'APP_DIRS'` is `True` in `TEMPLATES` settings.


## Usage

Use the mixins for the model admins you want to have "readonly by default and edit by clicking button" mode:

```python
import django_admin_edit_mode.admin


# Conditional edit mode enabled on edit object page
@admin.register(models.Book)
class BookAdmin(django_admin_edit_mode.admin.EditModeAdminMixin,
                      admin.ModelAdmin):
    ...

# Conditional edit mode enabled on list page
@admin.register(models.Author)
class AuthorAdmin(django_admin_edit_mode.admin.ConditionalListEditableAdminMixin,
                      admin.ModelAdmin):
    ...

    list_display = ('id', 'name', 'description', 'num_books')

    # list_editable = ('list_editable', )  # This you would use for "constant" edit mode
    conditional_list_editable = ('list_editable', ) 
```
