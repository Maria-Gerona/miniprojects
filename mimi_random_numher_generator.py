import random

print("Bien venido a CENEDOGE!\n")
print("Si quiere que se le asigne un numero pulse uno y para atencion al cliente pulse dos:\n ")
number = int(input("Introduja el numero aqui: "))
num1 = 1
num2 = 2
rand= random.randrange(1, 100)
if number == num1:
   print("Su numero de usuario es: ",rand)

elif number == num2:
    print("Para atencion al cliente dirijase a la primera ventanilla. ")
    print("Gracias y que tenga unn buen dia!!")

else:
    print("Ha pulsado un numero o caracter equivocado.\n" + "Solo puede pulsar el dijito 1 o el digito 2.")
