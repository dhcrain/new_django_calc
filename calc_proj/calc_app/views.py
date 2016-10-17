# from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from calc_app.models import Calculation
from calc_app.forms import CalcForm
# Create your views here.


class IndexView(CreateView):
    template_name = 'index.html'
    model = Calculation
    fields = ('num1', 'operator', 'num2')
