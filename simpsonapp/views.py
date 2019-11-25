
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template.loader import get_template
from simpsonapp.forms import ContactForm, LoginForm, SignupForm

from simpsonapp.models import Character


def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(request, username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                if user.is_authenticated:
                    return HttpResponseRedirect('introduction')
            else:
                error = "invalid username or password"
                return render(request, 'authentication.html', {'error': error, 'form': LoginForm()})

    return render(request, 'authentication.html', {'form': LoginForm()})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create(first_name=form.cleaned_data['first_name'],
                                    last_name=form.cleaned_data['last_name'],
                                    email=form.cleaned_data['email'], password=form.cleaned_data['password'],
                                    username=str(form.cleaned_data['email']))

                return HttpResponseRedirect('/login', {'form': LoginForm})

            except Exception:
                return render('404.hmtl', {'error': 'Signup is unsuccessful'})

    return render(request, 'authentication.html', {'form': SignupForm()})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def introduction():
    return render('introduction.html')


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            subject = request.POST.get('subject', '')

            form_content = request.POST.get('content', '')

            template = get_template('contact_form.html')
            context = ({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                'subject': subject,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content, "Simpsons" + '', ['zzeynepp.zt@gmail.com'], headers={'Reply-To': contact_email})
            email.send()

    return render(request, 'contact.html', {'form': form_class})


def character(request):
    if request.GET.get('id'):
        try:

            character = Character.objects.get(id=request.GET.get('id'))
            return render(request, 'employees.html', {'character': character})
        except ObjectDoesNotExist:
            return Http404

    else:
        return render(request, 'employees.html', {'characters': Character.objects.all()})


def subscribe(request):
    email = request.data.get('email')

