from .views import ProfileList,TwitterList,CommentCreate
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'tweets',TwitterList)
router.register(r'profiles',ProfileList)





urlpatterns = [
    path('',include(router.urls)),
    # path('profiles/<int:pk>/',include(router.urls)),
    # path('tweets/',TwitterList.as_view()),
    # path('tweets/create/',TwitterCreate.as_view()),
    # path('tweets/<int:pk>/',TwitterDetail.as_view(),name='detail'),
    path('tweets/<int:pk>/create-comment/',CommentCreate.as_view()),
]
