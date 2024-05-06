from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Destination


data = {
    "blogs": [
        {
            "id": 1,
            "number": 56,
            "name": "Angela",
            "title": "js",
            "description": "JAVASCRIPT",
        },
        {
            "id": 2,
            "number": 566,
            "name": "Robert",
            "title": "css",
            "description": "CSS HTML",
        },
        {
            "id": 3,
            "number": 6,
            "name": "Tesla",
            "title": "java",
            "description": "JAVA",
        },
        {
            "id": 3,
            "number": 6,
            "name": "Tesla",
            "title": "java",
        },
    ]
}


def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, 'page/index.html', context)


def about(request):
    return render(request, 'page/about.html')


def contact(request):
    contact_list = models.Destination.objects.all()
    paginator = Paginator(contact_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "page/contact.html", {"page_obj": page_obj})

