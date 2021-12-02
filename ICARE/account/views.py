from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from assessment.views import assessment


# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_patient:
                login(request, user)
                return redirect('pprofile')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('dprofile')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


@login_required()
def pprofile(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    query = request.POST.get("query")

    email = EmailMessage(
        subject=f"{name} from ICARE.",
        body=query,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER],
        reply_to=[email]
    )
    email.send()
    return render(request, 'pprofile.html')


@login_required()
def dprofile(request):
    return render(request, 'dprofile.html')
