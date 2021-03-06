from django.urls import path

from . import views

urlpatterns = [
    #path('jet/', include('jet.urls', 'jet')),
    path('', views.index, name='index'),
    path('question/', views.QuestionList.as_view(), name='list'),
    path('question/<int:question_id>/', views.QuestionDetail.as_view(), name='details'),
    path('choice/', views.ChoiceList.as_view(), name='list'),
    path('choice/<int:choice_id>/', views.ChoiceDetail.as_view(), name='details'),

]
