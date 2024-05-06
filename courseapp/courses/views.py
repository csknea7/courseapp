import os
import random

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Course
from .forms import CreateForm

# Create your views here.


data = {
    "blogs": [
        {
            "id": 1,
            "programlama": "programlamaya ait kurslar",
            "web-gelistirme": "web geliştirmeye ait kursalar",
            "mobil": "mobil geliştirmeye ait kursalar"

        }
    ]}

"""def index(request):
    database = {
        "kategoriler": data
    }
    return render(request, 'courses/index.html', database)"""


def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, 'courses/index.html', context)


def details(request):
    return HttpResponse('details')


"""def programlama(request):
    return HttpResponse('programlama kurs listesi')

def mobiluygulamalar(request):
    return HttpResponse('mobiluygulamalar kurs listesi')"""

"""def getCoursesByCategory(request, category):
    return HttpResponse(f'{category} kategorisindeki kurs listesi')"""


def designer(request, designer):
    return HttpResponse(f'{designer} tasarımcı kurs sayfası')


def article(request, year, month):
    return HttpResponse(f'{year} {month} zaman dilimi')


def search(request):
    pass


def kurslar(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'courses/kurslar.html', {'page_obj': page_obj})


def kurs(request):
    courses = Course.objects.all()
    return render(request, 'courses/kurs.html', {'courses': courses})


def create(request):
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.POST["imageUrl"]
        date = request.POST["date"]
        isActive = request.POST["isActive"]

        kurs = Course(title=title,
                      description=description,
                      imageUrl=imageUrl,
                      date=date,
                      isActive=isActive)
        kurs.save()
        return redirect("/courses/kurslar")
    return render(request, 'courses/create.html')


def create_form(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            kurs = Course(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                imageUrl=form.cleaned_data["imageUrl"],
                date=form.cleaned_data["date"],
                isActive=form.cleaned_data["isActive"]
            )
            kurs.save()
            return redirect("/courses/kurslar")

    form = CreateForm()
    return render(request, 'courses/form.html', {"form": form})


def course_list(request):
    courses = Course.objects.all()
    # kurs = Course.objects.filter(isActive=1)
    return render(request, 'courses/course-list.html', {'courses': courses})


def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        return redirect("/courses/kurs")
    return render(request, 'courses/course-delete.html', {'course': course})


def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CreateForm(request.POST, instance=course)
        form.save()
        return redirect("/courses/course-list")
    else:
        form = CreateForm(instance=course)
    return render(request, 'courses/course-edit.html', {'form': form})


def course_share(request):
    pass


def upload(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
        handle_uploaded_files(uploaded_image)
        return render(request, 'courses/success.html')
    return render(request, "courses/upload.html")


def success(request):
    return render(request, "courses/success.html")

def handle_uploaded_files(file):
    number = random.randint(1,99999999)
    filename, file_extention = os.path.splitext(file.name)
    name = filename + "_" + str(number) + file_extention
    with open('courseapp/temp/' + name, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

