from django.shortcuts import render


def MainView(request):
    return render(request, 'cocktail/main.html')


def InfoView(request):
    return render(request, 'cocktail/info.html')


def ModalView(request):
    return render(request, 'cocktail/modal.html')