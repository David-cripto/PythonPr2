from django.test import TestCase

from .models import Rubric, SuperRubric
from .forms import SubRubricForm


class RubricTest(TestCase):
    def setUp(self):
        Rubric.objects.create(name='Химия')

    def test_name_len(self):
        rubric = Rubric.objects.get(name='Химия')
        max_length = rubric._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_name(self):
        rubric = Rubric.objects.get(name='Химия')
        field_label = rubric._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')


class SubRubricFormTest(TestCase):
    def test_super_rubric_queryset(self):
        form = SubRubricForm()
        self.assertEquals(type(form.fields['super_rubric'].queryset),
                          type(SuperRubric.objects.all()))

    def test_super_rubric_label(self):
        form = SubRubricForm()
        self.assertEquals(form.fields['super_rubric'].label, 'Надрубрика')
