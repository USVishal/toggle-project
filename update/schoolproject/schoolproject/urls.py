"""schoolproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appschool import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage),
    path('login/',views.login),
    path('newaccount/',views.newaccount),
    path('create/',views.create),

    path('addteacher/',views.addteacher),
    path('addstudents/',views.addstudents),
    path('addstaff/',views.addstaff),

    path('staff/',views.staff),
    path('student/',views.student),
    path('teacher1/',views.teacher1),

    path('viewstaff/',views.viewstaff),
    path('viewstudent/',views.viewstudent),
    path('viewteacher/',views.viewteacher),

    path('updatestaff/<int:id>',views.updatestaff),
    path('updatestudent/<int:id>',views.updatestudent),
    path('updateteacher/<int:id>',views.updateteacher),
    
    path('updatestaff1/<int:id>',views.updatestaff1),
    path('updatestudent1/<int:id>',views.updatestudent1),
    path('updateteacher1/<int:id>',views.updateteacher1),

    path('deletestaff/<int:id>',views.deletestaff),
    path('deletestudent/<int:id>',views.deletestudent),
    path('deleteteacher/<int:id>',views.deleteteacher),

]  
