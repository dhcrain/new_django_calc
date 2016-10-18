from django import forms
from calc_app.models import Calculation


class CalcForm(forms.ModelForm):

    class Meta:
        model = Calculation
        fields = ['num1', 'operator', 'num2']
        widgets = {
            'operator': forms.RadioSelect(),
        }
