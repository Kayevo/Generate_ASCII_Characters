import string
 
stringOfCharacters = ""
 
listOfCharacters = list(string.ascii_lowercase)
listOfCharacters += list(string.ascii_uppercase)
listOfCharacters += list(string.hexdigits)
listOfCharacters += list(string.octdigits)
listOfCharacters += list(string.punctuation)

for characterOnList in listOfCharacters:
    stringOfCharacters += characterOnList

print(stringOfCharacters)
