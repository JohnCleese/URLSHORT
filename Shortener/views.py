from django.shortcuts import render
from .models import New_adress
from .form import Adressform


def shortener(request):
    if request.method == 'POST':
        form = Adressform(request.POST)
        if form.is_valid():
            url_old = form.cleaned_data['url_old']
            if not New_adress.objects.filter(url_old=url_old).exists():
                form.save()
            pk = New_adress.objects.get(url_old=url_old).pk
            context = {'url_old': url_old, 'pk': pk}
            return render(request, 'Shortener/Display.html', context)
    else:
        form = Adressform()
        context = {'form': form}
        return render(request, 'Shortener/Shortener.html', context)

def display_urls(request):
    return render(request, 'Shortener/Display.html')

def redirecturl(request, pk):
    link = New_adress.objects.get(pk=pk).url_old
    contect = {'link': link}
    return render(request, 'Shortener/Destination.html', contect)

