def guess():
    b = randrange (0,10)
    a = int(input("pick btw 1-10"))
    validinput=b
    while (validinput==b):
        try:
            print("congrats")
            validinput = b
        except:
            if (a-b)==1:
                print ("hot")
            elif a-b==2:
                print ("warm")
            else:
                print ("cold")

guess()











