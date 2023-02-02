from django import forms
from tests.models import TestModel, TestModelCategories

class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['category','questions', 'first_variant', 'second_variant', 'third_variant', 'fourth_variant','answer']

        widgets = {
            
            'questions': forms.Textarea(attrs={'class':'questions-input'},),
            'first_variant': forms.Textarea(attrs={'class':'first_variant-input'},),
            'second_variant': forms.Textarea(attrs={'class':'second_variant-input'},),
            'third_variant': forms.Textarea(attrs={'class':'third_variant-input'},),
            'fourth_variant': forms.Textarea(attrs={'class':'fourth_variant-input'},),
            'category': forms.Select(attrs={'class':'category-choice'},),
            'answer': forms.Select(attrs={'class':'answer-choice'},),
            
        }

class TestFormCategories(forms.ModelForm):
    class Meta:
        model = TestModelCategories
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class':'name-input'}, ),
            # 'quantity': forms.NumberInput(attrs={'class':'qauntity-input',})
        }