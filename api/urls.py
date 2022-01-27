
from django.urls import path
from .views import tasks,detailtask,posttask,updatetask,deletetask

urlpatterns = [
    path('', tasks,name='tasks'),
    path('<int:pk>/', detailtask,name='task'),
    path('post/',posttask,name='posttask'),
    path('update/<int:pk>/',updatetask,name='update'),
    path('delete/<int:pk>',deletetask,name='delete')
]

