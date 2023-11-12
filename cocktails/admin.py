from django.contrib import admin
from .models import MixedDrinks, FeaturedMixedDrinks

# Register your models here.
admin.site.register(MixedDrinks)
admin.site.register(FeaturedMixedDrinks)