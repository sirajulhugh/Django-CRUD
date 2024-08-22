from django.urls import path,include
from .import views

urlpatterns = [

    path('a',views.student,name="student"),
    path('adddetails',views.adddetails,name="adddetails"),
    path('v',views.viewtable,name="viewtable"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('editdetails/<int:id>',views.editdetails,name="editdetails"),
    path('deletedetails/<int:id>',views.deletedetails,name="deletedetails"),
    path('students/<int:id>', views.student_detail, name='student_detail'),
    path('',views.home,name="home"),
    path('v',views.page1,name="page1"),
    

]