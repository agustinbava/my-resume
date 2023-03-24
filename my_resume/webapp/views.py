from django.shortcuts import render
from django.views.generic import ( TemplateView )
from .forms import ContactForm

class HomePageTemplateView(TemplateView):
    template_name = 'index.html'
    
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = f"Thank you, {form.name}, for submitting the email!"
            context = {'message': message}
    return render(request, 'index.html', context)
