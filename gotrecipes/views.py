from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	userRecipes = Recipe.objects.order_by('title')
	return render(request, 'gotrecipes/index.html', {'recipes': userRecipes})

def recipe_detail(request, pk):
	recipe=get_object_or_404(Recipe, pk=pk)
	return render(request, 'gotrecipes/recipe_detail.html', {'recipe': recipe})

def new_recipe(request):
	if request.method == "POST":
		form = RecipeForm(request.POST)
		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.save()
			return redirect('recipe_detail', pk=recipe.pk)
	else:
		form = RecipeForm()
	return render(request, 'gotrecipes/recipe_edit.html', {'form': form})

@login_required	
def recipe_edit(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	if request.method == "POST":
		form = RecipeForm(request.POST, instance=recipe)
		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.save()
			return redirect('recipe_detail', pk=recipe.pk)
	else:
		form = RecipeForm(instance=recipe)
	return render(request, 'gotrecipes/recipe_edit.html', {'form': form})

@login_required
def recipe_delete(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	recipe.delete()
	return redirect('gotrecipes.views.index')