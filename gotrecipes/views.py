from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def index(request):
	userRecipes = Recipe.objects.order_by('title')
	return render(request, 'gotrecipes/index.html', {'recipes': userRecipes})

def recipe_detail(request, pk):
	recipe=get_object_or_404(Recipe, pk=pk)
	return render(request, 'gotrecipes/recipe_detail.html', {'recipe': recipe})

def new_recipe(request):
	if request.method == "POST":
		form = RecipeForm(request.POST, request.FILES)
		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.save()
			return redirect('recipe_detail', pk=recipe.pk)
	else:
		form = RecipeForm()
	return render(request, 'gotrecipes/recipe_edit.html', {'form': form})

def search_recipe(request):
	if request.method == "POST":
		return redirect('search_result', st=request.POST.get('search-term', ""))
	return render(request, 'gotrecipes/search_recipe.html')

def search_result(request, st):
	userRecipes = Recipe.objects.order_by('title')
	results = Recipe.objects.filter(ingredients__icontains=st).filter(title__icontains=st)
	return render(request, 'gotrecipes/search_result.html', {'recipes': results})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def recipe_delete(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	recipe.delete()
	return redirect('gotrecipes.views.index')

def login(request):
	username = password = ""
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HTTPResponseRedirect('/')
	return render(request, 'login.html')
