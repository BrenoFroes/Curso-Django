from django import forms
from django.core.mail import send_mail
from django.conf import settings
from simplemooc.core.mail import send_mail_template
class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )
    def send_email(self):
        subject='Contato sobre o curso'
        message='Nome: %(name)s;Email: %(email)s;%(message)s'
        context = {
            'name':self.cleaned_data['name'],
            'email':self.cleaned_data['email'],
            'message':self.cleaned_data['message'],
        }
        template_name = 'courses/contact_email.html'
        message = message % context
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
