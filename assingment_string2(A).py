str=input("enter any string :")
vowels=consonants=others=0
for i in range(0,len(str)):   
    if(str[i].isvowels()):
      vowels=vowels+1
    elif(str[i].isconsonants()):
      consonants = consonants + 1
    else :
      others=others+1

print("The no of vowels :",vowels)
print("The no of consonants :",consonants)
print("others :",others)

        
