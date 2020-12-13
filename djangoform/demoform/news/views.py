from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def index(request):
    return HttpResponse('Hello')

# Resister
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("news:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "news/register.html",
                          context={"form": form})
    form = UserCreationForm
    return render(request=request,
                  template_name="news/register.html",
                  context={"f": form})

# PostForm
def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})
def save_news(request):
    if request.method == 'POST':
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Luu thanh cong")
        else:
            return HttpResponse("Khong duoc validate")
    else:
        return HttpResponse("Khong phai POST request")

# Email
def email_view(request):
    b= SendEmail()
    return render(request, 'news/email.html', {'f': b})
def process(request):
    if request.method == 'POST':
        m = SendEmail(request.POST)
        if m.is_valid():
            # lay noi dung
            # tieude = m.cleaned_data['title']
            # noidung = m.cleaned_data['content']
            # email = m.cleaned_data['email']
            # context1 = {'a': tieude, 'b': noidung, 'c': email}
            # return render(request, 'news/print_email.html', context1)
            context2 = {'email_data': m}
            # return HttpResponse("Luu thanh cong")
            return render(request, 'news/print_email.html', context2)
        else:
            return HttpResponse("Form not validate")
    else:
        return HttpResponse("not POST method")

