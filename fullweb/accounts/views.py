from django.shortcuts import redirect
from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, get_user_model, logout
from fullweb.accounts.forms import SignUpForm, SignInForm, ProfileEditForm
from fullweb.accounts.models import Profile
from django.contrib.auth import mixins


UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'accounts/sign-in.html'
    form_class = SignInForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['show_footer_p'] = True
        return context


class SignOutView(mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'accounts/sign-out.html'

    def post(self, request):
        logout(request)
        return redirect('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['show_footer_p'] = True
        context['show_admin_site'] = self.request.user.is_staff
        return context


class ProfileDetailsView(mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['show_footer_p'] = True
        return context


class ProfileEditView(mixins.LoginRequiredMixin, views.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk':self.request.user.pk,})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['show_footer_p'] = True
        return context


class ProfileDeleteView(mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['show_footer_p'] = True
        return context


class ProfilePasswordView(mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    model = UserModel
    template_name = 'accounts/profile-password.html'

    def get_success_url(self):
        logout(self.request)
        return reverse_lazy('sign in')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['show_footer_p'] = True
        return context

