from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string('contact/emails/contactform.html',{
                'name':name,
                'email': email,
                'subject': subject,
                'message': message,
            })

            send_mail('The contact form subject', 'This is the message', 'smilesmoon5@gmail.com', ['smilesmoon5@gmail.com'], html_message=html)
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/index.html', {
        'form': form,
    })