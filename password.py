import string
import hashlib
import json

password = input("Veuillez définir votre mot de passe: ")
maj = string.ascii_uppercase
min = string.ascii_lowercase
chiffre = string.digits
special_character = string.punctuation

def verify():
    lenght = 0
    upercase_letter = 0
    lowercase_letter = 0
    digit = 0
    symbole = 0
    condition = False
    for char in password:
        for i in maj :
            if char == i :
                upercase_letter +=1
        for j in min :
            if char == j :
                lowercase_letter += 1
        for k in chiffre:
            if char == k:
                digit += 1
        for l in special_character:
            if char == l:
                symbole += 1
        if len(password) >= 8:
            lenght += 1
    if lenght != 0 and upercase_letter != 0 and lowercase_letter != 0 and digit != 0 and symbole != 0:
        print("votre mot de passe est correct")
        condition = True
        if condition == True:
            hash = hashlib.sha256()
            hash.update(password.encode("utf-8"))
            hash.hexdigest()
            print(hash.hexdigest())

            with open ("password.json","w") as f:
                json.dump(hash.hexdigest(),f)

            data = json.dumps(hash.hexdigest())
            print(data)

    else:
        print("une des conditions n'est pas remplie")
    return condition



verify()