from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'categories', views.RecipeCategoryViewSet)
router.register(r'chat-history', views.ChatHistoryViewSet, basename='chathistory')

urlpatterns = [
    path('', include(router.urls)),
    path('chatgpt/', views.chatgpt_proxy, name='chatgpt_proxy'),
    path('suggestions/', views.recipe_suggestions, name='recipe_suggestions'),
    path('tips/', views.cooking_tips, name='cooking_tips'),
    path('test/', views.test_api, name='test_api'),
    path('api-auth/', include('rest_framework.urls')),
]