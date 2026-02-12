from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.utils import timezone
import os

from .models import Recipe, RecipeCategory, ChatHistory
from .serializers import (
    RecipeSerializer,
    RecipeCategorySerializer,
    ChatHistorySerializer
)

# -------------------- Recipe ViewSet --------------------

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            recipes = Recipe.objects.filter(title__icontains=query)
        else:
            recipes = Recipe.objects.all()

        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)


# -------------------- Category ViewSet --------------------

class RecipeCategoryViewSet(viewsets.ModelViewSet):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


# -------------------- Chat History --------------------

class ChatHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = ChatHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChatHistory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# -------------------- ChatGPT Proxy --------------------

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def chatgpt_proxy(request):
    user_message = request.data.get('message', '')
    user = request.user if request.user.is_authenticated else None

    if not user_message:
        return Response({
            'success': False,
            'response': "Please provide a message."
        }, status=status.HTTP_400_BAD_REQUEST)

    # Simple fallback
    if "pizza" in user_message.lower():
        return Response({
            'success': True,
            'response': "🍕 Try making homemade pizza dough with flour, yeast, water, salt, and olive oil!"
        })

    # Try OpenAI
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are KuriousChef, a helpful cooking assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )

        bot_response = completion.choices[0].message.content

        # Save history if logged in
        if user:
            ChatHistory.objects.create(
                user=user,
                user_message=user_message,
                bot_response=bot_response
            )

        return Response({
            'success': True,
            'response': bot_response
        })

    except Exception as e:
        print("OpenAI Error:", str(e))
        return Response({
            'success': True,
            'response': "👨‍🍳 Ask me any cooking question!"
        })


# -------------------- Recipe Suggestions --------------------

@api_view(['GET'])
@permission_classes([AllowAny])
def recipe_suggestions(request):
    recipes = Recipe.objects.all()[:5]
    suggestions = []

    for recipe in recipes:
        suggestions.append({
            'id': recipe.id,
            'title': recipe.title,
            'description': recipe.description[:100],
            'prep_time': recipe.preparation_time,
            'cook_time': recipe.cooking_time,
            'total_time': recipe.preparation_time + recipe.cooking_time
        })

    return Response({
        'success': True,
        'suggestions': suggestions
    })


# -------------------- Cooking Tips --------------------

@api_view(['GET'])
@permission_classes([AllowAny])
def cooking_tips(request):
    tips = [
        "🔪 Always sharpen your knives",
        "🌡️ Use a meat thermometer",
        "🧂 Season in layers",
        "⏰ Prep ingredients first",
        "🔥 Don’t overcrowd the pan"
    ]

    return Response({
        'success': True,
        'tips': tips
    })


# -------------------- Test API --------------------

@api_view(['GET'])
@permission_classes([AllowAny])
def test_api(request):
    return Response({
        'success': True,
        'message': 'KuriousChef API is working!',
        'timestamp': timezone.now()
    })
