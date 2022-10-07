from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer, CategoryListSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def recipe_list(request):
    if request.method == 'GET':
        recipe = Recipe.objects.all()
        data = CategoryListSerializer(recipe, many=True, fields=['id', 'title', 'making_time', 'serves', 'ingredients', 'cost']).data
        return JsonResponse({'recipes': data}, safe=False,
                            status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Recipe successfully created',
                                 'recipe': [serializer.data]}, safe=False,
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                                 "message": "Recipe creation failed!",
                                 "required": "title, making_time, serves, ingredients, cost"
                                }, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PATCH'])
def recipe_detail(request, id):
    try:
        fields = ('id', 'title', 'making_time', 'serves', 'ingredients', 'cost')
        recipe = Recipe.objects.all().get(pk=id)
    except Recipe.DoesNotExist:
        return JsonResponse({"message": "No recipe found"}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = RecipeSerializer(recipe)
        all_fields = set(serializer.fields)
        for field in all_fields:
            if field not in fields:
                serializer.fields.pop(field)
        return JsonResponse({'message': 'Recipe details by id', 'recipe': [serializer.data]
                            } , safe=False,
                            status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        serializer = RecipeSerializer(recipe, data=request.data)
        all_fields = set(serializer.fields)
        for field in all_fields:
            if field not in fields:
                serializer.fields.pop(field)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Recipe successfully updated!", 'recipe': serializer.data}, safe=False,
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                         "message": "Recipe creation failed!",
                         "required": "title, making_time, serves, ingredients, cost"
                         }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        recipe.delete()
        return JsonResponse({"message": "Recipe successfully removed!"},
                            status=status.HTTP_200_OK)
