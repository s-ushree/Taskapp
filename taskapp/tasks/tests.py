from django.test import TestCase

from .forms import TaskForm


class TaskFormTests(TestCase):
    def test_upload_fields_are_optional(self):
        form = TaskForm()

        self.assertFalse(form.fields['image'].required)
        self.assertFalse(form.fields['file'].required)
