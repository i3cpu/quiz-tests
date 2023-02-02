from django.db import models

# Create your models here
class TestModelCategories(models.Model):
    # quantity = models.IntegerField(verbose_name='quantity of questions', default=0)
    name = models.CharField(max_length=200, verbose_name='name')
    
    def __str__(self) -> str:
        return f'{self.name}'

class TestModel(models.Model):
    category = models.ForeignKey('TestModelCategories', on_delete=models.CASCADE, blank=True, null=True)
    questions = models.TextField(max_length=500, verbose_name='questions')
    first_variant = models.CharField(max_length=300, verbose_name='first_variant')
    second_variant = models.CharField(max_length=300, verbose_name='second_variant')
    third_variant = models.CharField(max_length=300, verbose_name='third_variant')
    fourth_variant = models.CharField(max_length=300, verbose_name='fourth_variant')
    answer = models.CharField(max_length=10, verbose_name='answer', choices=(('A', "A"), ('B', "B"), ('C', "C"), ('D', "D")))

    def __str__(self) -> str:
        return f'{self.questions}'


