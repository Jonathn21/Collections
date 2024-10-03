
from django.contrib import admin
from .models import Produit, ImageProduit, VariationProduit, Collection

class ImageProduitInline(admin.TabularInline):
    model = ImageProduit
    extra = 1  # Nombre d'images supplémentaires à afficher dans le formulaire

class VariationProduitInline(admin.TabularInline):
    model = VariationProduit
    extra = 1  # Nombre de variations supplémentaires à afficher dans le formulaire



@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'collection')  # Champs à afficher dans la liste des produits
    search_fields = ('nom', 'collection__nom')  # Champs à utiliser pour la recherche
    inlines = [ImageProduitInline, VariationProduitInline]  # Afficher les images et les variations en ligne



