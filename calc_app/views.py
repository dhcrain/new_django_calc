# from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from calc_app.models import Calculation
from calc_app.forms import CalcForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.


class IndexView(CreateView):
    template_name = 'index.html'
    model = Calculation
    fields = ('num1', 'operator', 'num2')
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        calc_form = form.save(commit=False)
        if self.request.user.is_authenticated:
            calc_form.user = self.request.user
        num1 = form.cleaned_data['num1']
        num2 = form.cleaned_data['num2']
        operator = form.cleaned_data['operator']
        if operator == '+':
            calc_form.result = num1 + num2
        elif operator == '-':
            calc_form.result = num1 - num2
        elif operator == '/':
            calc_form.result = num1 / num2
        elif operator == 'X':
            calc_form.result = num1 * num2
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['calc_hist'] = Calculation.objects.filter(user=self.request.user)
        else:
            context['calc_hist'] = Calculation.objects.filter(user=None)

        return context
