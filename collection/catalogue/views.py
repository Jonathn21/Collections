from .models import Produit,Panier
from django.shortcuts import render, get_object_or_404,redirect

def produit_detail(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    prix_s_xl = None
    prix_2xl_5xl = None

    for variante in produit.variantes.all():
        print(f"Vérification de la variante: {variante.taille}, Prix: {variante.prix}")  # Ajoutez cette ligne pour déboguer
        if variante.taille.lower() in ["s", "m", "l", "xl"]:
            if prix_s_xl is None:
                prix_s_xl = variante.prix
                print(f"Prix pour S-XL défini à: {prix_s_xl}")  # Ajoutez cette ligne pour déboguer
        elif variante.taille.lower() in ["2xl", "3xl", "4xl", "5xl"]:
            if prix_2xl_5xl is None:
                prix_2xl_5xl = variante.prix
                print(f"Prix pour 2XL-5XL défini à: {prix_2xl_5xl}")  # Ajoutez cette ligne pour déboguer

    return render(request, 'produit_detail.html', {
        'produit': produit,
        'prix_s_xl': prix_s_xl,
        'prix_2xl_5xl': prix_2xl_5xl,
    })



def catalogue(request):
    produits = Produit.objects.prefetch_related('images', 'variantes').all()
    return render(request, 'catalogue.html', {'produits': produits})




