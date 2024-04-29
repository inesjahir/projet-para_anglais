import random

x = random.randint(50, 100)
print("Voici un nombre aléatoire entre 50 et 100: "+ str(x))
 
y = int (input("choisis un nombre plus petit que ce dernier : "))

z = random.randint(y,x)
print("voici un nombre aleatoire entre le 1e nombre aleatoire et le nombre que vous avez choisis : " + str(z)) 
