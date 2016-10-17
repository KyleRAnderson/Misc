import sys
a= str(input("Insert the valuw of a:"))
if a.isnumeric()== True: 
    a= int(a)
    if a > 0: print("Your porabola will open up")
    elif a == 0: print("That ain't a valid a value")
    else: print("Your porabola will open up")
else: 
    a= str(a)
    print("\""+ a + '\"' , 'is not a valid digit...')