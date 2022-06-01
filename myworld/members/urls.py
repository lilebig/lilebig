from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from members import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('members/', views.memberList.as_view()),
    path('members/<int:pk>/', views.memberDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)