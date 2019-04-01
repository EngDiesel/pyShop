from .forms import contactform
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactform(request.POST or None)
    confirm_message = None
    context = {'title': title,}

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        subject = 'Message from MYSITE.COM'
        message = '%s ,%s' % (comment, name)
        send_mail(subject, message, email_from, email_to, fail_silently=False,)
        title = 'Thanks'
        confirm_message = "Thanks for the message, we'll get right back to you."
        form = None
    
    context = {'title': title, 'form': form, 'confirm_message': confirm_message,}
    template = 'contact.html'

    return render(request, template, context)