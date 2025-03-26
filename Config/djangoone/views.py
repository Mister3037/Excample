from django.shortcuts import render

# Create your views here.

def home(request):
    malumot = {
        "kitoblar": ["O'limga mahkum qilinganlar", "Burgut tog'da ulg'ayadi", "Alvido Bolalik", "Sariq devni minib"],
        "muallif": "Nurddin Ismoilov"
    }
    return render(request, 'index.html', context=malumot)