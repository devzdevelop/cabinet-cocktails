from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(
        'cocktails/',
        include(
            [
                path('list/', views.CocktailsList.as_view(), name='cocktailslist'),
                path('featuredlist/', views.FeaturedCocktailsList.as_view(), name='featuredcocktailslist'),
                path('<int:pk>/details/', views.CocktailsDetail.as_view(), name='cocktailsdetail'),
                path('add/', views.CreateCocktail.as_view(), name='newcocktail'),
                path('<int:pk>/edit', views.UpdateCocktail.as_view(), name='editcocktail'),
                path('<int:pk>/delete', views.DeleteCocktail.as_view(), name='deletecocktail'),
            ]
        ),
    ),
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
]
