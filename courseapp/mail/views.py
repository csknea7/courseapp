from django.shortcuts import render, redirect
from django.template.loader import render_to_string
import os
from .forms import ContactForm
from django.core.mail import send_mail



def send_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('mail/email.html', {
                'name': name,
                'email': email,
                'content': content
            })

            print('the form is valid')
            send_mail('test', 'test', 'csknea@gmail.com', ['coskunesra@outlook.com'], html_message=html)
            return redirect('email')
    else:
        form = ContactForm()

    return render(request, 'mail/email.html', {'form': form})

os.environ['SSL_CERT_FILE'] = '/Library/Frameworks/Python.framework/Versions/3.12/etc/openssl/cert.pem'

#import ssl

#print(ssl.get_default_verify_paths())