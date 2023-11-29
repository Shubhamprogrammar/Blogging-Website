from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("education",views.education, name="education"),
    path("social",views.social, name="social"),
    path("news",views.news, name="news"),
    path("disclaimer",views.disclaimer, name="disclaimer"),
    path("career",views.career, name="career"),
]