from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('view_info/<int:id>',views.view_info),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('update_emp/<int:id>',views.update_emp,name='update_emp'),
    path('delete/<int:id>',views.remove_emp,name='remove_emp')
]
