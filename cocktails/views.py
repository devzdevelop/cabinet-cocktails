from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

from .models import MixedDrinks, FeaturedMixedDrinks
from .forms import CreateCocktailForm, UpdateCocktailForm, DeleteCocktailForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'cocktails/home.html'


class CocktailsList(ListView):
    model = MixedDrinks
    template_name = 'cocktails/cocktails_list.html'
    

class FeaturedCocktailsList(ListView):
    model = FeaturedMixedDrinks
    template_name = 'cocktails/featured_cocktails_list.html'

class CocktailsDetail(DetailView):
    model = MixedDrinks
    template_name = 'cocktails/cocktails_detail.html'


class CreateCocktail(CreateView):
    model = MixedDrinks
    template_name = 'cocktails/create_cocktail.html'
    form_class = CreateCocktailForm


class UpdateCocktail(UpdateView):
    model = MixedDrinks
    template_name = 'cocktails/edit_cocktail.html'
    form_class = UpdateCocktailForm
    success_url = reverse_lazy('cocktailslist')


class DeleteCocktail(DeleteView):
    model = MixedDrinks
    template_name = 'cocktails/delete_cocktail.html'
    success_url = reverse_lazy('cocktailslist')


class SearchResultsListView(ListView):
    model = MixedDrinks
    template_name = 'cocktails/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return MixedDrinks.objects.filter(
            Q(name__icontains=query)
        )