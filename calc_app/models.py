from django.db import models

# Create your models here.


class Calculation(models.Model):
    user = models.ForeignKey('auth.User', null=True)
    num1 = models.FloatField()
    operator_choices = (('+', '+'), ('-', '-'), ('/', '/'), ('X', 'X'))
    operator = models.CharField(max_length=1, choices=operator_choices)
    num2 = models.FloatField()
    result = models.FloatField(null=True, blank=False)

    def __str__(self):
        return str(self.result)
