from django.shortcuts import render
from .models import About, Resume, Skills
from .forms import ContactForm

def contact_submit(request):
    if request.method == 'GET':
        about = About.objects.get()
        about_text_desc = about.text_description.split('.')
        about.text_description = about_text_desc
        context = {'about': about}
        return render(request, 'index.html', context)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'form': form})
        else:
            form = ContactForm()
    return render(request, 'index.html', {'form': form})
