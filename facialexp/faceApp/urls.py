from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('prediction/',views.modelPredict),
    path('pic/',views.picClick,name='pic'),
    path('',views.videoClick,name='video')
]
