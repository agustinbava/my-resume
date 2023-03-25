from django.shortcuts import render
from django.views.generic import ( TemplateView )
from .forms import ContactForm

class HomePageTemplateView(TemplateView):
    template_name = 'index.html'

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'form': form})
        else:
            form = ContactForm()
    return render(request, 'index.html', {'form': form})
