from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings 

from .forms import ContactForm


# Create your views here.
def contact(request):
	title = 'Contact'
	form = ContactForm(request.POST or None)
	confirm_msg = None

	if form.is_valid():

		comment = form.cleaned_data['comment']
		name = form.cleaned_data['name']
		emailFrom = form.cleaned_data['email']

		subject = 'Message from ' + emailFrom
		message = '%s \n%s' % (comment, name)
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=False)

		title = 'Thank You !'
		confirm_msg = 'Thanks, we appreciate your contact :)'
		form = None
		
	context = {'title': title, 'form':form, 'confirm_msg': confirm_msg}
	template = 'contact.html'
	return render(request, template, context)