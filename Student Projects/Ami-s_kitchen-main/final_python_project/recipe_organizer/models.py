# Importing necessary modules from Django
from django.db import models

# Define Django model for recipe
class recipe(models.Model):
    # Define field for storing recipe name as a string with maximum length of 100 characters
    recipe_name = models.CharField(max_length=100)
    
    # Define field for storing recipe text as a large text field
    recipe_text = models.TextField()
    
    # Define field for storing recipe picture as an image file, specifying upload destination
    recipe_picture = models.ImageField(upload_to="recipe_FOLDER")
