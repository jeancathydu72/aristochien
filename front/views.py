from django.shortcuts import render

def accueil(request):
    return render(request, 'front/accueil.html')

def boutique(request):
    return render(request, 'front/boutique.html')

def realisations(request):
    return render(request, 'front/realisations.html')

