# django-admin-edit-mode
[![PyPI - Version](https://img.shields.io/pypi/v/django-admin-edit-mode?label=django-admin-edit-mode&link=https%3A%2F%2Fpypi.org%2Fproject%2Fdjango-admin-edit-mode%2F)](https://pypi.org/project/django-admin-edit-mode/)

Allows to open objects in django admin in read-only mode by default,
with a special button "Go to edit mode" to open the same change-object page in regular editable mode.

Why read-only mode by default is needed ? For some applications, django-admin serves mostly for reading the info.
**Readonly mode page looks better (cleaner)**, doesn't allow to make some changes accidentially, and the **page loads quicker** (e.g., no need to load a list of choices for the fields).
But you're not going to make admin completely readonly (e.g., by persmissions), because **sometimes you still want to change** the object.
Then you can **go to edit mode by clicking the button**!


## Installation

* `pip install django-admin-edit-mode`
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
    ...
    
```
