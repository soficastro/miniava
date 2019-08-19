from django import forms
from django.core.mail import send_mail
from django.conf import settings
from miniava.core.mail import send_mail_template
from .models import Comment


class ContactCourse(forms.Form):
	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='Email')
	message = forms.CharField(
		label='Mensagem/Dúvida', widget=forms.Textarea)

	def send_mail(self, course):
		subject = '[%s] Contato' %course
		context = {
			'name': self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'message': self.cleaned_data['message'],
		}
		template_name = 'contact_email.html' #mudar?
		send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields= ['comment']
	