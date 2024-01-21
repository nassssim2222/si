from django.contrib import admin

from .models import achats_tranche, emprunt, produit , main_store , centre_pv , client , agent, pvs , team , matiere_premiere , fournisseur , Delivrer , SeCompose , R1 , R2 , R3,achats, transferer, ventes, ventes_tranche


# Register your models here.
admin.site.register(produit)
admin.site.register(main_store)
admin.site.register(centre_pv)
admin.site.register(client)
admin.site.register(agent)
admin.site.register(team)
admin.site.register(matiere_premiere)
admin.site.register(fournisseur)
admin.site.register(Delivrer)
admin.site.register(SeCompose)
admin.site.register(R1)
admin.site.register(R2)
admin.site.register(R3)
admin.site.register(achats)
admin.site.register(achats_tranche)
admin.site.register(transferer)
admin.site.register(ventes)
admin.site.register(ventes_tranche)
admin.site.register(pvs)
admin.site.register(emprunt)
