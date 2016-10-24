from django.db import models
from calc_app.utils import do_math, int_or_float


class Calculation(models.Model):
    user = models.ForeignKey('auth.User', null=True)
    num1 = models.FloatField()
    operator_choices = (('+', '+'), ('-', '-'), ('/', '/'), ('X', 'X'))
    operator = models.CharField(max_length=1, choices=operator_choices)
    num2 = models.FloatField()

    class Meta:
        ordering = ['-id']

    @property
    def get_result(self):
        return do_math(self.num1, self.operator, self.num2)

    @property
    def get_num1(self):
        return int_or_float(self.num1)

    @property
    def get_num2(self):
        return int_or_float(self.num2)

    def __str__(self):
        return "{} {} {} = {}".format(self.num1, self.operator, self.num2, self.get_result)
