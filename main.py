# Python program 
# FizzBuzz

texte =""
numero = int(input("Enter a number: "))


if numero % 3 == 0:
    texte += "Fizz"
if numero % 5 == 0:
    texte += "Buzz"
print(texte, "Your number is :", numero)