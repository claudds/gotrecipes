from django.shortcuts import render
from .forms import RecipeForm

# Create your views here.
def index(request):
	return render(request, 'gotrecipes/index.html', {})

def new_recipe(request):
	if request.method == "POST":
		form = RecipeForm(request.POST)
		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.save()
	else:
		form = RecipeForm()
	return render(request, 'gotrecipes/recipe_edit.html', {'form': form})