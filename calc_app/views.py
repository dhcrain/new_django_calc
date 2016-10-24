from django.views.generic import CreateView, DeleteView
from calc_app.models import Calculation
from calc_app.forms import CalcForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class IndexView(CreateView):
    template_name = 'index.html'
    form_class = CalcForm
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        calc_form = form.save(commit=False)
        if self.request.user.is_authenticated:
            calc_form.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['calc_hist'] = Calculation.objects.filter(user=self.request.user)
        else:
            context['calc_hist'] = Calculation.objects.filter(user=None)[:5]
            context['login_form'] = AuthenticationForm()
            context['user_creation_form'] = UserCreationForm()
        return context


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class CalcDeleteView(DeleteView):
    model = Calculation
    success_url = reverse_lazy('index_view')
