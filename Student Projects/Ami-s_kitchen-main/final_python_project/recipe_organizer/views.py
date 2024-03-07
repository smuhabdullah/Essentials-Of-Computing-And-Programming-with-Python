from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # Importing the models from the same directory
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# View function for displaying recipes and adding new ones
def recipes(request):
    if request.method == "POST":  # Check if the request method is POST
        data = request.POST  # Get the POST data
        recipe_name = data.get("recipe_name")  # Get the recipe name from the form
        recipe_text = data.get("recipe_text")  # Get the recipe text from the form
        recipe_picture = request.FILES.get("recipe_picture")  # Get the recipe picture from the form
        
        # Create a new recipe object with the received data and save it to the database
        recipe.objects.create(
            recipe_name=recipe_name,
            recipe_picture=recipe_picture,
            recipe_text=recipe_text
        )

    # Retrieve all recipes from the database
    datalist = recipe.objects.all()

    # If there is a search query in the request GET parameters, filter the recipes accordingly
    if request.GET.get('searchs'):
        datalist = datalist.filter(recipe_name__icontains=request.GET.get('searchs'))

    # Pass the retrieved recipes to the template as context
    get_data = {'recipes': datalist}
    return render(request, 'recipes.html', get_data)

# View function for deleting a recipe
def delete_recipe(request, id):
    # Get the recipe object with the provided ID
    recipe_instance = recipe.objects.get(id=id)
    # Delete the recipe object from the database
    recipe_instance.delete()
    # Redirect the user back to the recipes page
    return redirect('recipes')

# View function for updating a recipe
def update_recipe(request, id):
    # Get the recipe object with the provided ID or return a 404 error if not found
    recipe_instance = get_object_or_404(recipe, id=id)

    # If the request method is POST, update the recipe with the provided data
    if request.method == "POST":
        data = request.POST  # Get the POST data
        recipe_name = data.get("recipe_name")  # Get the updated recipe name from the form
        recipe_text = data.get("recipe_text")  # Get the updated recipe text from the form
        recipe_picture = request.FILES.get("recipe_picture")  # Get the updated recipe picture from the form
        
        # Update the recipe object with the new data
        recipe_instance.recipe_name = recipe_name
        recipe_instance.recipe_text = recipe_text

        # If a new picture is provided, update the recipe picture
        if recipe_picture:
            recipe_instance.recipe_picture = recipe_picture

        # Save the updated recipe object to the database
        recipe_instance.save()
        # Redirect the user back to the recipes page
        return redirect('recipes')
        
    # Pass the recipe object to the template as context
    get_data = {'recipe': recipe_instance} 
    return render(request, 'update.html', get_data)
