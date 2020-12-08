from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from .models import Customer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import auth_logout
from .forms import CreateUserForm, ChangePasswordForm, ResetPasswordForm

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
# Create your views here.

def logout(request):
    auth_logout(request)
    return redirect('/home/')

def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('pass')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            messages.warning(request, "Login Error !! Username or Password is incorrect")
        else:
            request.session.set_expiry(86400)
            login(request, my_user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
    return render(request, 'login.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            pass_word1 = form.cleaned_data.get('password1')
            my_user = authenticate(username=user_name, password=pass_word1)
            login(request, my_user)
            customer = Customer()
            customer.user_id = my_user.id
            customer.email = my_user.email
            customer.name = customer.user_name()
            customer.save()
            return redirect('home')
        else:
            messages.warning(request, 'Please correct the error below.')
    return render(request, 'signup.html', {'f': form})


def view_profile(request):
    current_user = request.user  # Access User Session information

    if current_user.has_usable_password():
        customer = Customer.objects.get(user=request.user)
        if request.method == 'POST':
            # Name
            full_name = request.POST.get('fullname')
            if full_name != "":
                split_name = full_name.split()
                current_user.first_name = split_name[0]
                current_user.last_name = ""
                list_length = len(split_name)
                for i in range(1, list_length):
                    current_user.last_name += (" " + split_name[i] + " ")
            else:
                current_user.first_name = current_user.last_name = ""
            # Email
            email = request.POST.get('email')
            current_user.email = email
            current_user.save()
            # Customer
            customer.email = current_user.email
            customer.name = customer.user_name()
            customer.address = request.POST.get('address')
            customer.phone = request.POST.get('phone')
            customer.save()
        return render(request, 'profile.html', {'customer': customer})
    else:
        customer = Customer()
        if request.method == 'POST':
            full_name = request.POST.get('fullname')
            if full_name != "":
                split_name = full_name.split()
                current_user.first_name = split_name[0]
                current_user.last_name = ""
                list_length = len(split_name)
                for i in range(1, list_length):
                    current_user.last_name += (" " + split_name[i] + " ")
            else:
                current_user.first_name = current_user.last_name = ""
            # Email
            email = request.POST.get('email')
            current_user.email = email
            current_user.save()
            # Customer
            customer.user = current_user
            customer.email = current_user.email
            customer.name = customer.user_name()
            customer.address = request.POST.get('address')
            customer.phone = request.POST.get('phone')
            customer.save()
        return render(request, 'profile.html', {'customer': customer})


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('home')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'changepass.html', {'f': form})


def send_email(request):
    if request.method == 'POST':
        subject = 'Subject here',
        message = 'Here is the message.',
        email_from = settings.EMAIL_HOST_USER,
        recipient_list = [request.POST.get('email_receive')],
        email_template_name = "password_reset_email.txt"
        associated_users = User.objects.filter(email=request.POST.get('email_receive'))
        if associated_users.exists():
            for user in associated_users:
                context = {
                    "email": user.email,
                    'domain': '127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, context)
                send_mail(
                    'Password reset',
                    email,
                    settings.EMAIL_HOST_USER,
                    recipient_list[0],
                )
                return redirect('password_reset_done')
        else:
            messages.error(request, 'Email is not registered')
    return render(request, 'password_reset_form.html')


class SetNewPasswordView(View):
    def get(self, request, uidb64, token):
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
        form = ResetPasswordForm(user)
        context = {
            'uidb64': uidb64,
            'token': token,
            'f': form
        }
        return render(request, 'password_reset_confirm.html', context)

    def post(self, request, uidb64, token):
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
        if request.method == 'POST':
            form = ResetPasswordForm(request.user, request.POST)
            if form.is_valid():
                pass_word = form.cleaned_data.get('new_password1')
                user.set_password(pass_word)
                user.save()
            else:
                messages.warning(request, 'Please correct the error below.')
        return redirect('login')







