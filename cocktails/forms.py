from django import forms

from .models import MixedDrinks


class CreateCocktailForm(forms.ModelForm):
    
    class Meta:
        model = MixedDrinks
        fields = ('name','recipe', )


class UpdateCocktailForm(forms.ModelForm):

    class Meta:
        model = MixedDrinks
        fields = ('name','recipe', 'image')

    

class DeleteCocktailForm(forms.ModelForm):

    class Meta:
        model = MixedDrinks
        fields = ('name','recipe', 'image')