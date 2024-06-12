import random
def shuffle (string):
    tempList = list(string) #converts the string into a list
    random.shuffle(tempList) #shuffles the list
    return ''.join(tempList) #converts the list back into a string


uppercaseLetters = chr(random.randint(65,90)) + chr(random.randint(65,90)) #Generates a random uppercase letters based on ASCII code
lowercaseLetters = chr(random.randint(97,122)) + chr(random.randint(97,122)) #Generates a random lowercase letters based on ASCII code
digits = str(random.randint(0,9)) + str(random.randint(0,9)) #generates random numbers
randomSymbols = chr(random.randint(33,126)) + chr(random.randint(33,126)) + chr(random.randint(33,126)) #generates random symbols
password = uppercaseLetters + lowercaseLetters + digits + randomSymbols
password = shuffle(password)
print(password)