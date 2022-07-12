from django.urls import include, path
from rest_framework import routers
from comment.views import CommentViews

router = routers.DefaultRouter()
router.register(r'comment', CommentViews)



urlpatterns = [

]

urlpatterns += router.urls