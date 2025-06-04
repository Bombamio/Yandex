from django.shortcuts import render


def index(request):
    tamplate_name = 'main/index.html'
    return render(request, tamplate_name)

    tamplate_name = 'ice_cream/list.html'
    return render(request, tamplate_name)