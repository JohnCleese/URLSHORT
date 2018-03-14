from django.shortcuts import render
from .models import NewAdress
from .form import Adressform


def shortener(request):
    if request.method == 'POST':
        form = Adressform(request.POST)
        if form.is_valid():
            main_url = form.cleaned_data['main_url']
            if not NewAdress.objects.filter(main_url=main_url).exists():
                form.save()
            pk = NewAdress.objects.get(main_url=main_url).pk
            context = {'main_url': main_url, 'pk': pk}
            return render(request, 'Shortener/Display.html', context)
    else:
        form = Adressform()
        context = {'form': form}
        return render(request, 'Shortener/Shortener.html', context)

def display_urls(request):
    return render(request, 'Shortener/Display.html')

def redirecturl(request, pk):
    link = NewAdress.objects.get(pk=pk).main_url
    contect = {'link': link}
    return render(request, 'Shortener/Destination.html', contect)

