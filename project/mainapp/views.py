from django.shortcuts import render

from mainapp.models import News


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)

