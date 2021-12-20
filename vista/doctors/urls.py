from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('SignUpAsDoctor' , views.SignUpAsDoctor , name = 'SignUpAsDoctor' ),
    path('signUpAsClient' , views.SignUpAsClient , name = 'SignUpAsClient'),
    path('login' , views.login , name = 'login'),
    path('doctorDetails/<int:id>' , views.doctorDetails , name = 'doctorDetails'),
    path('delete/<int:id>' , views.delete , name = 'deleteDoctor'),
    path('newExperience/<int:id>' , views.addnewExperience , name = 'newExperience'),
    path('book/<int:id>' , views.book , name = 'book'),
]