from django.shortcuts import render, redirect
import os

from myapp import settings
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.contrib import messages


def index(request):
    testimonials = Testimonial.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {'testimonials': testimonials, 'skills': skills, 'projects': projects}
    return render(request, 'index.html', context)


def contact_me(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        template = loader.get_template('contact_form.txt')
        context = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            'Portfolio Message', message,
            'New Message',
            [settings.EMAIL_HOST_USER, email])
        email.content_subtype = 'html'
        email.send()
        messages.success(request, 'Message Sent Succesfully')
        return redirect('/')


def details(request, pk):
    models = Project.objects.get(id=pk)
    context = {'models': models}
    return render(request, 'portfolio-details.html', context)
