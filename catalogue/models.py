from django.db import models

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=255)  # Nom du produit
    description = models.TextField(blank=True)  # Description du produit
    lien = models.CharField(max_length=255,null=True)  # Nom du produit
 
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, null=True)  # Lien vers la collection (permet null)

    def __str__(self):
        return f"{self.nom}"
    
class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, related_name='images', on_delete=models.CASCADE)  # Lien vers le produit
    image = models.ImageField(upload_to='produits/images/')  # Image du produit

    def __str__(self):
        return f"Image de {self.produit.nom}"

class VariationProduit(models.Model):
    produit = models.ForeignKey(Produit, related_name='variantes', on_delete=models.CASCADE)  # Lien vers le produit
    taille = models.CharField(max_length=50)  # Taille du produit
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # Prix en FCFA

    def __str__(self):
        return f"{self.produit.nom} - {self.taille}"
    
class Collection(models.Model):
    nom = models.CharField(max_length=255)  # Nom de la collection
    description = models.TextField(blank=True)  # Description de la collection

    def __str__(self):
        return self.nom

class Panier(models.Model):
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} unités"

