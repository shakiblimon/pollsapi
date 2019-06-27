from  django.urls import path

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="polls_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",CreateVote.as_view(),name="polls_list",),
]

router = DefaultRouter()
router.register('', QuestionViewSet, base_name='questions')
urlpatterns += router.urls