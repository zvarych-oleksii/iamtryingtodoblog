from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from .forms import SignUpForm, AuthenticationForm, ProfileChangeForm, ChangeUserForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout

class ProfileDetail(DetailView):
    model = Profile
    pk_url_kwarg = "pk"
    template_name = "profiles/user_detail.html"
    context_object_name = "profile"
class ProfileChangeDetail(FormMixin, DetailView):
    model = Profile
    pk_url_kwarg = "pk"
    template_name = "profiles/user_detail_change.html"
    form_class = ProfileChangeForm

    def get_context_data(self, **kwargs):
        context = super(ProfileChangeDetail, self).get_context_data(**kwargs)
        context.update({"form_user": ChangeUserForm(initial={'username': self.request.user.username,
                                                             'email': self.request.user.email}),
                        "form_profile": ProfileChangeForm(initial=self.request.user.profile.get_initial_date())})
        return context
    def post(self, request, *args, **kwargs):
        user_form = ChangeUserForm(request.POST, instance=request.user)
        profile_form = ProfileChangeForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save(commit=False)
            profile_form.save(commit=False)
        else:
            print("FormIsInvalid")
        return redirect("Index")



def LoginPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("Index")
        return render(request, "accounts/login.html", context={})
    else:
        return redirect("Index")

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get("last_name")
                email = form.cleaned_data.get("email")
                user = authenticate(username=username, password=password)
                print(email)
                Profile.objects.create(user=user, name=username, user_email=email, first_name=first_name, last_name=last_name)
                return redirect("Login")
        else:
            form = SignUpForm()
        return render(request, "accounts/signup.html", context={"form": SignUpForm()})
    else:
        return redirect("Index")