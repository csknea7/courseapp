from django.urls import path
from . import views

urlpatterns = [

    path('details/', views.details),
    path('index/', views.index),
    path('search/', views.search, name="search"),
    path('create/', views.create, name="create"),
    path('kurslar/', views.kurslar, name="kurslar"),
    path('kurs/', views.kurs, name="kurs"),
    path('form/', views.create_form, name="course-form"),
    path('course-list/', views.course_list, name="course-list"),
    path('course-delete/<int:id>/', views.course_delete, name="course-delete"),
    path('course-edit/<int:id>/', views.course_edit, name="course-edit"),
    #path('programlama', views.programlama),
    #path('mobil-uygulamalar', views.mobiluygulamalar),
    #path('<category>', views.getCoursesByCategory), #category dynamic url
    path('designer/<str:designer>/', views.designer),
    path('article/<int:year>/<int:month>/', views.article),
    path('upload/', views.upload, name="upload"),
    path('success/', views.success, name="success")
]