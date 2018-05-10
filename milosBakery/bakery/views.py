from django.shortcuts import render, HttpResponse
from .forms import ContactForm
def index(request):
    if request.method == 'POST':
        return HttpResponse('yay')
    form = ContactForm(request.POST or None)
    return render(request, 'index.html',{'form':form})
