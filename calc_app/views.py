# from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from calc_app.models import Calculation
from calc_app.forms import CalcForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from calc_app.utils import do_math


# Create your views here.


class IndexView(CreateView):
    template_name = 'index.html'
    form_class = CalcForm
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        calc_form = form.save(commit=False)
        self.num1 = form.cleaned_data['num1']
        self.num2 = form.cleaned_data['num2']
        self.operator = form.cleaned_data['operator']
        calc_form.result = do_math(self.num1, self.operator, self.num2)
        if self.request.user.is_authenticated:
            calc_form.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['calc_hist'] = Calculation.objects.filter(user=self.request.user)
        else:
            context['calc_hist'] = Calculation.objects.filter(user=None)
            context['login_form'] = AuthenticationForm()
            context['user_creation_form'] = UserCreationForm()
        return context


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('index_view')


class CalcDeleteView(DeleteView):
    model = Calculation
    success_url = reverse_lazy('index_view')
