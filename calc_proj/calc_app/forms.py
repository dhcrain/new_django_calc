from django import forms
from calc_app.models import Calculation


class CalcForm(forms.ModelForm):
    # operator_choice = [('+', '+'), ('-', '-'), ('/', '/'), ('X', 'X')]
    # num1 = forms.FloatField()
    # operator = forms.ChoiceField(operator_choice)
    # num2 = forms.FloatField()

    class Meta:
        model = Calculation
        fields = ['num1', 'operator', 'num2']
