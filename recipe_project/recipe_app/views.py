from django.shortcuts import render, HttpResponse

def recipe_list(request):
    return HttpResponse('List of Recipes')


# Create your views here.
