def greeting():
    a = (input("name?"))
    print("cool,", a)

    b = (input("Which color is the god of all colors, in your opinion?"))
    print(b,"You got problems man, i hope you go to church!")

    c = (input("what do you like to put in your mouth?"))
    print(c, "is nasty whats wrong with you?")

    d = (input("Soooo... U tryna come thru tn... i got netflix.... we can chillaxxx....?"))
    if (d == "no"):
        print(greeting())
    elif (d == "yes"):
        print ("Bet, im bringin' chocolate syrup...")
    else:
        print ("Ayyy uh-uh dont dodge the question!")

greeting()