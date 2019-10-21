from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .apiviews import ChoiceList, QuestionList, QuestionDetail, UserCreate, vote_view, WordListList, WordListDetail, WordPairCreation, WordPairDetail, WordPairFilter
from rest_framework.authtoken import views as authviews
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('', views.index, name='index'),
    path('landing', views.landing),
    path("questions/", QuestionList.as_view(), name="question_list"),
    path("questions/<int:pk>/", QuestionDetail.as_view(), name="question_detail"),
    path("questions/<int:pko>/choice/", ChoiceList.as_view()),
    path('wordlists/', WordListList.as_view(), name="word_list_list"),
    path('wordlists/<int:pk>/', WordListDetail.as_view()),
    path('wordpairs/', WordPairCreation.as_view()),
    path('wordpairs/<int:pk>', WordPairDetail.as_view()),
    path("createuser", UserCreate.as_view(), name="user_create"),
    path("login/", authviews.obtain_auth_token),
    path("questions/<int:question_pk>/choice/<int:choice_pk>/", vote_view),
    path('swagger-docs/', schema_view),
    path("filters/", WordPairFilter)
   # path('question', views.question_list),
   # path('question/<int:pk>/', views.question_detail)
]

  ##  path('details/<int:question_id>', views.detail, name="details"), """

   #    path("polls/<int:pk>/", polls_detail