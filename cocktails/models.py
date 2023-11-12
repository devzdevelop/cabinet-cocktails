from django.db import models
from django.urls import reverse

# Create your models here.
class MixedDrinks(models.Model):
    name = models.CharField(max_length=70)
    recipe = models.TextField()
    garnishes = models.TextField(default='No garnish needed.')
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse("model_detail", kwargs={"pk": self.pk})
        return reverse("home")


class FeaturedMixedDrinks(models.Model):
    name = models.ForeignKey("MixedDrinks", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.name
    
    def get_absolute_url(self):
        #return reverse("model_detail", kwargs={"pk": self.pk})
        return reverse("home")