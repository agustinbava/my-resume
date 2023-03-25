from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ( TemplateView )
from .forms import ContactForm

class HomePageTemplateView(TemplateView):
    template_name = 'index.html'

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()
            messages.success(request, 'Your message was sent successfully!')
            return render(request, 'success.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
