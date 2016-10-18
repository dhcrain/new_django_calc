# from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from calc_app.models import Calculation
from calc_app.forms import CalcForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from calc_app.utils import do_math


# Create your views here.


class IndexView(CreateView):
    template_name = 'index.html'
    form_class = CalcForm
    # model = Calculation
    # fields = ('num1', 'operator', 'num2')
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        calc_form = form.save(commit=False)
        self.num1 = form.cleaned_data['num1']
        self.num2 = form.cleaned_data['num2']
        self.operator = form.cleaned_data['operator']
        calc_form.result = do_math(self.num1, self.operator, self.num2)
        if self.request.user.is_authenticated:
            calc_form.user = self.request.user
        else:
            self.request.session['calc_session'] = {'num1': self.num1, 'operator': self.operator, 'num2': self.num2, 'result': calc_form.result}
            self.request.session.set_expiry(600)  # Data removed from DB after 10 min, (600 sec)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['calc_hist'] = Calculation.objects.filter(user=self.request.user)
        else:
            context['calc_hist'] = Calculation.objects.filter(user=None)
            context['login_form'] = AuthenticationForm()

        return context
