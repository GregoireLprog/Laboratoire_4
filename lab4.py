#continuer de travailler sur votre code
#possible de changer
# deux for et deux while
# trois input de l'utilisateur
# des print, genre beaucoup
# trois bloc de if, nombre de "if" 

#break
#continue
# else (boucle)
# si on viens au lab en sachant ce que le mot "pass" veut dire


import random # dit a l'ordi de choisir une valeur au hasard q'on vas définir

print("inscrivez 3 nombres")
# Demander trois entrées utilisateur
try:
    input1 = float(input("Entrez le premier nombre : "))
    input2 = float(input("Entrez le deuxième nombre : "))
    input3 = float(input("Entrez le troisième nombre : "))
except ValueError: # si l'utilisateur entre autre chose qu'un nombre
    print("Veuillez entrer un nombre valide.")
    exit()
# Utiliser un opérateur logique pour vérifier les conditions
if input1 > input2 and input1 > input3: # si 1 est plus grand que 2 et 3
    result = f"Le premier nombre {input1} est le plus grand."
elif input2 > input1 and input2 > input3: # si 2 est plus grand que 1 et 3
    result = f"Le deuxième nombre {input2} est le plus grand."
else:
    result = f"Le troisième nombre {input3} est le plus grand." # si 3 est le plus grand 
if input1 == input2 and input2 == input3: # si les 3 nombres sont égaux
    result = "Les trois nombres sont égaux, prépare toi."
print(result)
input4 = str(input("Voulez vous jouer a roche papier sciscaux? (oui/non) : "))
if input4 == "non": # si l'utilisateur choisi non, le programme se ferme
    print("Au revoir!")
    exit()
if input4 == "oui": # si "oui" est entré, le programme continue
    print("Choisissez entre roche, papier ou ciseaux.") # roche papier ciseaux classique, (une partie)
options = ["roche", "papier", "ciseaux"] # répertoire des choix possibles de l'ordinateur et utilisateur


user_choice = input("Choose roche, papier, or ciseaux:") # demande a l'utilisateur de choisir
computer_choice = random.choice(options)
print("You chose: ", user_choice) # affiche ce que l'utilisateur a choisi
print("Computer chose: ", computer_choice) # affiche ce que l'ordinateur a choisi
# condition pour déterminer le gagnant
if user_choice == computer_choice: # si l'ordi a le meme choix que l'utilisateur
        print("It's a tie!")
elif user_choice == "roche" and computer_choice == "ciseaux": # roche bat ciseaux, utilisateur gagne
        print("You win!")
elif user_choice == "papier" and computer_choice == "roche": # papier bat roche, utilisateur gagne
        print("You win!")
elif user_choice == "ciseaux" and computer_choice == "papier": #  ciseaux bat papier, utilisateur gagne
        print("You win!")
else: # si contraire, ordi gagne
        print("Computer wins!")
        print("Merci d'avoir joué!")

# fin du programme