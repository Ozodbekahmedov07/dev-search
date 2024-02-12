
from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('news', NewsSetApiView, basename='news'),
router.register('user ', UserSetApiView, basename='user')
urlpatterns = router.urls


#
# urlpatterns = [
#     path('News/', NewsApiView.as_view()),
#     path('News/<int:pk>/', NewsRetrieveApiView.as_view()),
#     path('Newsupdeate/<int:pk>/', NewsUpdateApiView.as_view()),
#     path('Newscreate/', NewsCreateApiView.as_view()),
    #
    # path('properties/', PropertyApiView.as_view()),
    # path('properties/<int:pk>/', PropertyRetrieveApiView.as_view()),
    # path('agent/', AgentApiView.as_view()),
    # path('agent/<int:pk>/', AgentRetrieveApiView.as_view()),
    # path('property/', propertyApiView.as_view()),
    # path('property/<int:pk>/', propertyRetrieveApiView.as_view()),
    # path('comments/', CommentsApiView.as_view()),
    # path('comments/<int:pk>/', AgentRetrieveApiView.as_view()),
#]