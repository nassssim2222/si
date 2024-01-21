from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.db.models import Sum
from .forms import FiltreStockForm, PointageForm, achatsform, centerform, clientform, empruntform, matiereform, productform,fournisseurform, pvform, regler_client_form, regler_fournisseur_form, teamform, trancheform, trancheform1, transfereform, venteform
from django.http import JsonResponse

from .models import achats_tranche, produit,centre_pv,client,fournisseur, pvs,team,matiere_premiere,achats,transferer, ventes


def home(response):
    return render(response, "home.html",{})
def index(response):
    return render(response, "index.html",{})

def tables(response):
    return render(response, "tables.html",{})

def afficher_table(request) :
    produits = produit.objects.all()
    centre = centre_pv.objects.all()
    clients = client.objects.all()
    fournisseurs = fournisseur.objects.all()
    employe = team.objects.all()
    matiere = matiere_premiere.objects.all()

    types={"produit":produits,
           "centre":centre,
           "client":clients,
           "fournisseur":fournisseurs,
           "team":employe,
           "matiere_premiere":matiere
          }


    return render(request,"index.html",types)


def select(request , id , type) :
   
    types = {}

    if type == 'produit' :
        produits = produit.objects.get(prod_ID = id)
        types = {'produit' : produits}

    if type == 'centre' :
        centres = centre_pv.objects.get(centre_ID = id)
        types = {'centre' : centres}

    if type == 'client' :
        clients = client.objects.get(client_ID = id)
        types = {'client' : clients}

    if type == 'fournisseur' :    
        fournisseurs = fournisseur.objects.get(fournisseur_ID = id)
        types = {'fournisseur' : fournisseurs}


    if type == 'team' :
        employe = team.objects.get(employer_CODE = id)
        types = {'team' : employe}

    if type == 'matiere_premiere' :    
        matiere = matiere_premiere.objects.get(matiere_ID = id)
        types = {'matiere_premiere' : matiere}

    return render(request,"select.html",types)



def matieres(request) :
    
    return render(request,"matieres.html",{})



def add_product(request,type):

    if type == 'produit' :    
        if request.method == 'POST':
            form = productform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = productform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = productform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})

    if type == 'center' :
        if request.method == 'POST':
            form = centerform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = centerform()  # Create a new empty form
                write = "centre added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = centerform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})
        return render(request, 'add.html', {'form': form})
    
    if type == 'pv' :
        if request.method == 'POST':
            form = pvform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = pvform()  # Create a new empty form
                write = "centre added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = pvform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})
        return render(request, 'add.html', {'form': form})
    
    if type == 'team' :    
        if request.method == 'POST':
            form = teamform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = teamform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = teamform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})

    if type == 'fournisseur' :    
        if request.method == 'POST':
            form = fournisseurform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = fournisseurform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = fournisseurform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})

    if type == 'matiere_premiere' :    
        if request.method == 'POST':
            form = matiereform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = matiereform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = matiereform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})        

    if type == 'client' :    
        if request.method == 'POST':
            form = clientform(request.POST)

            if form.is_valid():
                form.save()  # Call the save method to save the product
                form = clientform()  # Create a new empty form
                write = "Product added, you can add another."
                return render(request, 'add.html', {'form': form, 'message': write})
        else:
            form = clientform()
            write = "Make sure you have entered all fields."
            return render(request, 'add.html', {'form': form, 'message': write})


def modify_product(request, id , type):

    if type == 'produit' :
        produits = produit.objects.get(prod_ID=id)
    
        if request.method == 'POST':
            form = productform(request.POST, instance=produits)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = productform(instance=produits)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})

        
    if type == 'client':
        centres = client.objects.get(client_ID=id)
    
        if request.method == 'POST':
            form = clientform(request.POST, instance=client)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = clientform(instance=centres)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})
    
    if type == 'centre':
        centres = centre_pv.objects.get(centre_ID=id)
    
        if request.method == 'POST':
            form = centerform(request.POST, instance=centres)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = centerform(instance=centres)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})
    
    if type == 'fournisseur':
        fournisseurs = fournisseur.objects.get(fournisseur_ID=id)
    
        if request.method == 'POST':
            form = fournisseurform(request.POST, instance=fournisseurs)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = fournisseurform(request.POST ,instance=fournisseurs)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})
    
    if type == 'team':
        teams = team.objects.get(employer_CODE=id)
    
        if request.method == 'POST':
            form = teamform(request.POST, instance=teams)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = teamform(instance=teams)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})

    if type == 'matiere_premiere':
        matiers = matiere_premiere.objects.get(matiere_ID=id)
    
        if request.method == 'POST':
            form = matiereform(request.POST, instance=matiers)

            if form.is_valid():
                form.save()
                return redirect('list_produit')         
        else:
            form = matiereform(instance=matiers)
            return render(request, 'update.html', {"form": form })
        return render(request, 'index.html', {'form': form})
    


    
    
def regler_fournisseur_sold(request,id):
        fournisseurs = fournisseur.objects.get(fournisseur_ID=id)
        if request.method == 'POST':
            form = regler_fournisseur_form(request.POST,instance=fournisseurs)
            montant_reglage =  request.POST.get('number_input')
            montant_reglage = int(montant_reglage)
            if montant_reglage < fournisseurs.fournisseur_SOLD :
                fournisseurs.fournisseur_SOLD = fournisseurs.fournisseur_SOLD - montant_reglage
                fournisseurs.save()

                    
        else:
            form = regler_fournisseur_form(request.POST ,instance=fournisseurs)
            
            return render(request, 'regler_fournisseur.html', {"form": form })
        
        form = regler_fournisseur_form(request.POST ,instance=fournisseurs)
            
        return render(request, 'regler_fournisseur.html', {"form": form })

def regler_client_credit(request,id):
        clients = client.objects.get(client_ID=id)
        if request.method == 'POST':
            form = regler_client_form(request.POST,instance=clients)
            montant_reglage =  request.POST.get('number_input')
            montant_reglage = int(montant_reglage)
            if montant_reglage < clients.client_credit :
                clients.client_credit = clients.client_credit - montant_reglage
                clients.save()

                    
        else:
            form = regler_client_form(request.POST,instance=clients)
            
            return render(request, 'regler_fournisseur.html', {"form": form })
        
        form = regler_client_form(request.POST,instance=clients)
            
        return render(request, 'regler_fournisseur.html', {"form": form })

def delete_product(request,id,type):
    if type == 'produit':
        produits = produit.objects.get(prod_ID=id)
        produits.delete()
        return redirect('list_produit')
    if type =='centre':
        centres = centre_pv.objects.get(centre_ID=id)
        centres.delete()
        return redirect('list_produit')
    if type == 'team':
        teams = team.objects.get(employer_CODE=id)
        teams.delete()
        return redirect('list_produit')
    if type == 'matiere_premiere':
        matiers = matiere_premiere.objects.get(matiere_ID=id)
        matiers.delete()
        return redirect('list_produit')
    if type == 'fournisseur':
        fournisseurs = fournisseur.objects.get(fournisseur_ID=id)
        fournisseurs.delete()
        return redirect('list_produit')
    if type == 'client':
        clients = client.objects.get(client_ID=id)
        clients.delete()
        return redirect('list_produit')
    if type == 'achats':
        achat = achats.objects.get(achats_ID=id)
        achat.delete()
        return redirect('list_produit')
    if type == 'transfere':
        transfere = transferer.objects.get(transfere_ID=id)
        transfere.delete()
        return redirect('list_produit')
    if type == 'vente':
        vente = ventes.objects.get(vente_ID=id)
        vente.delete()
        return redirect('list_produit')



def search_product(request):

    if request.method == 'POST' :
        search = request.POST['passed']
        types = {'searched':search}

        product = produit.objects.filter(prod_NAME__contains=search)
        if product.exists() :
            types.update({'produits' : product })
    
        
        centres = centre_pv.objects.filter(centre_NAME__contains=search)
        if centres.exists() :
            types.update({'centre' : centres})
        
        teams = team.objects.filter(employer_NOM__contains=search)
        if teams.exists() :
            types.update({'team' : teams})
        
        matiers = matiere_premiere.objects.filter(matiere_NAME__contains=search)
        if matiers.exists() :
            types.update({ 'matiere_premiere' : matiers})
        
        clients = client.objects.filter(client_NAME__contains=search)
        if clients.exists() :
            types.update({ 'client' : clients})
        
        fournisseurs = fournisseur.objects.filter(fournisseur_NAME__contains=search)
        if fournisseurs.exists() :
            types.update({'fournisseur' : fournisseurs})
        
        if len(types) > 1 :
            return render(request, 'search.html' , types)
        
        msg = 'no search found :('
        return render(request, 'search.html' , {"searched" : search , "message":msg})


                            
    
    
    
    
                                
def afficher(request,type):
    if type == 'achats':
        achat = achats.objects.all()
        if achat.exists() :
            return render(request, 'search.html' , { 'achats' : achat}) 
        else: 
            return render(request, 'search.html' , { 'achats' : achat}) 
    else :
        if type == 'transfere':
            transfere = transferer.objects.all()
            if transfere.exists() :
                return render(request, 'search.html' , { 'transfere' : transfere})  
            else: 
                return render(request, 'search.html' , { 'transfere' : transfere})  
        if type == 'vente':
            vente = ventes.objects.all()
            if vente.exists() :
                return render(request, 'search.html' , { 'vente' : vente})  
            else : 
                return render(request, 'search.html' , { 'vente' : vente})  

def choosing(request):
    return render(request,'adding_home.html')



def regler_fournisseur(request):
    if request.method == 'POST' :
        search = request.POST['passed']
        fournisseurs_reglage = fournisseur.objects.filter(fournisseur_NAME__contains=search)
        if fournisseurs_reglage.exists() :
            return render(request, 'search.html' , { "searched" : search , 'fournisseurs_reglage' : fournisseurs_reglage})
        else:
            form = trancheform()
            warning ='aucun fournisseur contient ce nom'
            return render(request, 'achat_confirmer.html' , {"warning":warning,"form":form})
        
def regler_client(request):
    if request.method == 'POST' :
        search = request.POST['passed']
        client_reglage = client.objects.filter(client_NAME__contains=search)
        if client_reglage.exists() :
            return render(request, 'search.html' , { "searched" : search , 'client_reglage' : client_reglage})
        else:
            form = trancheform1()
            warning ='aucun client contient ce nom'
            return render(request, 'vente_confirmer.html' , {"warning":warning,"form":form})
            
            
        

       

def achat_matieres(request):
    
    if request.method == 'POST':
        form = achatsform(request.POST)

        if form.is_valid():
            QTE_achat = form.cleaned_data['QTE_achat']
            produit1 = form.cleaned_data['produit_exist']
            prix_unit = produit1.price
            produit1.quantite_stock= produit1.quantite_stock + QTE_achat
            produit1.save()
            montant_tot = prix_unit * QTE_achat
            write2 = "le montant totale a payer est : "
            form.save()  # Call the save method to save the product
            form = achatsform()  # Create a new empty form
            write = "Product added, you can add another."
            return render(request, 'achat.html', {'form': form, 'message': write,'message2': write2,'montant_tot': montant_tot})
        else:
            form = achatsform()
            write = "Make sure you have entered all fields."
            return render(request, 'achat.html', {'form': form, 'message': write})
    else:
        form = achatsform()
        write = "Make sure you have entered all fields."
        return render(request, 'achat.html', {'form': form, 'message': write})
    
def transferer_matieres(request):
    
    if request.method == 'POST':
        form = transfereform(request.POST)

        if form.is_valid():
            QTE_transfere = form.cleaned_data['QTE_transfere']
            produit1 = form.cleaned_data['produit_exist']
            prix_unit = produit1.price
            montant_tot = prix_unit * QTE_transfere
            produit1.quantite_stock = produit1.quantite_stock - QTE_transfere
            write2 = "le montant totale du tranfere : "
            produit1.save()
            form.save()  # Call the save method to save the product
            form = transfereform()  # Create a new empty form
            write = "transfere added, you can add another."
            return render(request, 'transfere.html', {'form': form, 'message': write,'message2': write2,'montant_tot': montant_tot})
        else:
            form = transfereform()
            write = "Make sure you have entered all fields."
            return render(request, 'transfere.html', {'form': form, 'message': write})
    else:
        form = transfereform()
        write = "Make sure you have entered all fields."
        return render(request, 'transfere.html', {'form': form, 'message': write})
    


def vente_matieres(request):
    
    if request.method == 'POST':
        form = venteform(request.POST)

        if form.is_valid():
            QTE_vente = form.cleaned_data['QTE_vente']
            prix_unit = form.cleaned_data['prix_unit_vente']
            produit1 = form.cleaned_data['produit_exist']
            produit1.quantite_stock = produit1.quantite_stock - QTE_vente
            montant_tot = prix_unit * QTE_vente
            write2 = "le montant totale a payer est : "
            form.save()  # Call the save method to save the product
            produit1.save()
            form = venteform()  # Create a new empty form
            write = "Product added, you can add another."
            return render(request, 'ventes.html', {'form': form, 'message': write,'message2': write2,'montant_tot': montant_tot})
        else:
            form = venteform()
            write = "Make sure you have entered all fields."
            return render(request, 'ventes.html', {'form': form, 'message': write})
    else:
        form = venteform()
        write = "Make sure you have entered all fields."
        return render(request, 'ventes.html', {'form': form, 'message': write})





def achat_confirmation(request):
    if request.method == 'POST':
        form_tranche = trancheform(request.POST)
        
        if form_tranche.is_valid():
            fournisseur1= form_tranche.cleaned_data['fournisseur_exist']
            QTE_achat = form_tranche.cleaned_data['QTE_achat']
            produit1 =form_tranche.cleaned_data['produit_exist']
            produit1.quantite_stock = produit1.quantite_stock + QTE_achat 
            prix_unit = produit1.price
            montant_tot = prix_unit * QTE_achat
            tranche = form_tranche.cleaned_data['tranche_val']
            montant_payer = montant_tot - tranche
            fournisseur1.fournisseur_SOLD = fournisseur1.fournisseur_SOLD + montant_payer
            fournisseur1.save()
            produit1.save()

            form_tranche.save()
            form_tranche = trancheform()
            
            write = "Product added, you can add another."
            write1 = "le montant totale a payer est : "
            return render(request, 'achat_confirmer.html', {'form': form_tranche, 'message': write,'message1': write1,'montant_tot':montant_tot})
        else:
            form_tranche = trancheform()
            write = "Make sure you have entered all fields."
            return render(request, 'achat_confirmer.html', {'form': form_tranche, 'message': write})
    else:
        form_tranche = trancheform()
        write = "Make sure you have entered all fields."
        return render(request, 'achat_confirmer.html', {'form': form_tranche, 'message': write})
    


def vente_confirmation(request):
    if request.method == 'POST':
        form_tranche = trancheform1(request.POST)
        
        if form_tranche.is_valid():
            client1 = form_tranche.cleaned_data['client_exist']
            QTE_vente = form_tranche.cleaned_data['QTE_vente']
            prix_unit = form_tranche.cleaned_data['prix_unit_vente']
            produit1 =form_tranche.cleaned_data['produit_exist']
            produit1.quantite_stock = produit1.quantite_stock - QTE_vente 
            montant_tot = prix_unit * QTE_vente
            tranche = form_tranche.cleaned_data['tranche_val']
            montant_payer = montant_tot - tranche
            client1.client_credit = client1.client_credit + montant_payer
            client1.save()
            produit1.save()
           
            form_tranche.save()
            form_tranche = trancheform1()
            
            write = "Product added, you can add another."
            write1 = "le montant totale a payer est : "
            return render(request, 'vente_confirmer.html', {'form': form_tranche, 'message': write,'message1': write1,'montant_tot':montant_tot})
        else:
            form_tranche = trancheform1()
            write = "Make sure you have entered all fields."
            return render(request, 'vente_confirmer.html', {'form': form_tranche, 'message': write})
    else:
        form_tranche = trancheform1()
        write = "Make sure you have entered all fields."
        return render(request, 'vente_confirmer.html', {'form': form_tranche, 'message': write})
    

def stock(request):
    
    produits = produit.objects.all()
    filtre_form = FiltreStockForm(request.GET)
    total_achats=0
    
    if filtre_form.is_valid() and filtre_form.is_bound:
            if produits.exists():
                fournisseur1 = filtre_form.cleaned_data.get('fournisseur')
                date_achat = filtre_form.cleaned_data.get('date_achat')

                achat = achats.objects.all()
                

                
                if fournisseur1:
                    achat = achats.objects.filter(fournisseur_exist=fournisseur1)
                    produits=produit.objects.filter(achats__in=achat).distinct()
                    
                if date_achat:
                    achat = achats.objects.filter(date_achats=date_achat)
                    produits=produit.objects.filter(achats__in=achat).distinct()

                if fournisseur1 and date_achat :
                    achat = achats.objects.filter(fournisseur_exist=fournisseur1 , date_achats=date_achat)
                    produits=produit.objects.filter(achats__in=achat).distinct()

                for purchase in achat:
                     total_achats += (purchase.QTE_achat*purchase.produit_exist.price)
               
                return render(request, 'stock.html', {'produit_stock': produits, 'filtre_form': filtre_form,'total_achats': total_achats}) 
            else:       

                return render(request, 'stock.html', { 'filtre_form': filtre_form ,'total_achats': total_achats})
    else:       

        return render(request, 'stock.html', {'produit_stock': produits, 'filtre_form': filtre_form ,'total_achats': total_achats})
     
            
def table_board(request):
    
    produits = produit.objects.all()
    filtre_form = FiltreStockForm(request.GET)
    total_achats=0
    
    if filtre_form.is_valid() and filtre_form.is_bound:
            if produits.exists():
                fournisseur1 = filtre_form.cleaned_data.get('fournisseur')
                date_achat = filtre_form.cleaned_data.get('date_achat')

                achat = achats.objects.all()
                

                
                if fournisseur1:
                    achat = achats.objects.filter(fournisseur_exist=fournisseur1)
                    produits=produit.objects.filter(achats__in=achat).distinct()
                    
                if date_achat:
                    achat = achats.objects.filter(date_achats=date_achat)
                    produits=produit.objects.filter(achats__in=achat).distinct()

                if fournisseur1 and date_achat :
                    achat = achats.objects.filter(fournisseur_exist=fournisseur1 , date_achats=date_achat)
                    produits=produit.objects.filter(achats__in=achat).distinct()

                for purchase in achat:
                     total_achats += (purchase.QTE_achat*purchase.produit_exist.price)
               
                return render(request, 'stock.html', {'produit_stock': produits, 'filtre_form': filtre_form,'total_achats': total_achats}) 
            else:       

                return render(request, 'stock.html', { 'filtre_form': filtre_form ,'total_achats': total_achats})
    else:       

        return render(request, 'stock.html', {'produit_stock': produits, 'filtre_form': filtre_form ,'total_achats': total_achats})
     
            
def details(request,id):
    pv = pvs.objects.filter(concerned_center__centre_ID=id)
    return render(request,'details.html',{'pv' : pv , 'id' : id})      


def afficher_team(request,id) :
   
    employe = team.objects.filter(centre_pnv__centre_ID = id)

    types={
           "team":employe
          }


    return render(request,"details_employe.html",types)

def select_team(request,id):
    

    employe = team.objects.get(employer_CODE = id)
    id_centre = employe.centre_pnv.centre_ID

    types = {'team' : employe,
             'id':id_centre
            }

    return render(request,"select_team.html",types)    


def pointage(request, id):
    employe = team.objects.get(employer_CODE = id )

    form = PointageForm(request.POST)
    if request.method == 'POST':
       

        if form.is_valid():
            present = form.cleaned_data['employer_Present']
            #absent = form.cleaned_data['employer_Absent']

            if present:
                employe.employer_SALAIRE_JR += 1000
            elif not present:
                employe.employer_SALAIRE_JR -= 500

            employe.save()
            return render(request, 'pointage.html', {'employe': employe, 'form': form})    
    else:
        form = PointageForm()
        return render(request, 'pointage.html', {'employe': employe, 'form': form})


def emprunt(request , id):
    employe = team.objects.get(employer_CODE = id )

    form = empruntform(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            
            total = form.cleaned_data['somme']
            form.save()

            employe.employer_SALAIRE_JR -= total

            employe.save()
            msg = "operation effectuer "
            return render(request, 'emprunt.html', {'employe': employe, 'form': form , 'message':msg})
    else:
        form = empruntform()
        return render(request, 'emprunt.html', {'employe': employe, 'form': form })