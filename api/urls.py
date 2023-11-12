from django.urls import path, include
from .views import CocktailList, CocktailDetails, UserList, CocktailCreate
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # Cocktails CRUD
    path('v1/cocktails/', CocktailList.as_view(), name='cocktail_list'),
    path('v1/cocktails/<int:pk>/', CocktailDetails.as_view(), name='cocktail.details'),
    path('v1/cocktails/create/', CocktailCreate.as_view(), name='cocktail_create'),
    
    # Users List
    path('v1/users/', UserList.as_view(), name="user_list"),

    # Authentication
    path('api-auth/', include('rest_framework.urls')),
    path('v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Schema/Documentation
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
