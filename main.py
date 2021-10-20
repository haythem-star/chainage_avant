from Data import Data
D=Data()
D.affiche_base_faits()
print('choisir par taper le numéro de votre choix :')
print('1-saturer la base de faits')
print('2-s\'arrêter si un but est précisé')
x=input()
if x =='2':
    b=input('entrer le but (par défaut : '+D.but+'): ')
    if(b != ''):
        D.but=b
    D.chainage_avant(False)
else:
    D.chainage_avant(True)
D.affiche_base_faits()