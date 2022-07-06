from django.shortcuts import render

def index(request):
    return render(
        request,
        'gameinfo/index.html',
        {
            'title': 'Главная страница'
        }
    )
