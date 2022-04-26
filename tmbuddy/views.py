from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import SelfReflection, BuddyFeedback
from users.models import Profile
from django.contrib.auth.models import User
from .forms import SelfReflectionForm, BuddyFeedbackForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


def home(request):
    return render(request, 'tmbuddy/home.html')


class SelfReflectionCreateView(LoginRequiredMixin, CreateView):
    model = SelfReflection
    form_class = SelfReflectionForm
    template_name = 'tmbuddy/reflection_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = Profile.objects.filter(user=self.request.user).first()
        return context


class BuddyFeedbackCreateView(LoginRequiredMixin, CreateView):
    model = BuddyFeedback
    form_class = BuddyFeedbackForm
    template_name = 'tmbuddy/feedback_create.html'

    def form_valid(self, form):
        form.instance.from_user = self.request.user
        if self.request.user.profile.buddy == None:
            messages.info(self.request, f'Please select your buddy. ')
            return redirect('profile')
        else:
            form.instance.to_user = self.request.user.profile.buddy
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = Profile.objects.filter(user=self.request.user).first()
        return context


class SelfReflectionListView(LoginRequiredMixin, ListView):
    model = SelfReflection
    template_name = 'tmbuddy/user_reflection.html'
    context_object_name = 'reflections'
    paginate_by = 10

    def get_queryset(self):
        return SelfReflection.objects.filter(user=self.request.user)


class GivenFeedbackListView(LoginRequiredMixin, ListView):
    model = BuddyFeedback
    template_name = 'tmbuddy/user_given_feedback.html'
    context_object_name = 'feedbacks'
    paginate_by = 10

    def get_queryset(self):
        return BuddyFeedback.objects.filter(from_user=self.request.user).filter(to_user=self.request.user.profile.buddy)


class ReceivedFeedbackListView(LoginRequiredMixin, ListView):
    model = BuddyFeedback
    template_name = 'tmbuddy/user_received_feedback.html'
    context_object_name = 'feedbacks'
    paginate_by = 10

    def get_queryset(self):
        return BuddyFeedback.objects.filter(to_user=self.request.user).filter(from_user=self.request.user.profile.buddy)


class SelfReflectionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SelfReflection
    form_class = SelfReflectionForm
    template_name = 'tmbuddy/reflection_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        reflection = self.get_object()
        if self.request.user == reflection.user:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = Profile.objects.filter(user=self.request.user).first()
        return context


class BuddyFeedbackUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BuddyFeedback
    form_class = BuddyFeedbackForm
    template_name = 'tmbuddy/feedback_update.html'

    def form_valid(self, form):
        form.instance.from_user = self.request.user
        if self.request.user.profile.buddy == None:
            messages.info(self.request, f'Please select your buddy. ')
            return redirect('profile')
        else:
            form.instance.to_user = self.request.user.profile.buddy
        return super().form_valid(form)

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.from_user:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = Profile.objects.filter(user=self.request.user).first()
        return context


class SelfReflectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SelfReflection
    template_name = 'tmbuddy/reflection_confirm_delete.html'

    def test_func(self):
        reflection = self.get_object()
        if self.request.user == reflection.user:
            return True
        return False
    
    def get_success_url(self):
        return reverse_lazy('user-reflection', kwargs={'username':self.get_object().user.username})


class BuddyFeedbackDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BuddyFeedback
    template_name = 'tmbuddy/feedback_confirm_delete.html'

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.from_user:
            return True
        return False
    
    def get_success_url(self):
        return reverse_lazy('user-given-feedback', kwargs={'username':self.get_object().from_user.username})


def about(request):
    return render(request, 'tmbuddy/about.html')


def tm_fam(request):
    context = {
        'fam': User.objects.exclude(username='admin'),
    }
    return render(request, 'tmbuddy/tm_fam.html', context)


def resources(request):
    return render(request, 'tmbuddy/resources.html')
