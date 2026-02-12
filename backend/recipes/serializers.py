from rest_framework import serializers
from .models import Recipe, RecipeCategory, ChatHistory

class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    category = RecipeCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=RecipeCategory.objects.all(),
        source='category',
        write_only=True
    )
    
    class Meta:
        model = Recipe
        fields = '__all__'

class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = '__all__'
        read_only_fields = ['user']