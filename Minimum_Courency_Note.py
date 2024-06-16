def minNotes(amount):
    notes =[500,200,100,50,20,10,5,2,1]
    

    print("Number of Currency Notes: ")
    for i in notes:
        if amount >= i:
            count = amount // i
            amount %= i
            print(f"{i} : {count}")

amount =int(input("enter your amount:"))
minNotes(amount)
