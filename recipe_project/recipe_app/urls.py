from django.urls import path
from.views import recipe_list, recipe_details,category_list, category_detail
app_namke = recipe_app
urlpatterns ={
path('recipe/',recipe_list,name='recipe_list'),
path('categories/',category_list, name='category_list'),

    

}