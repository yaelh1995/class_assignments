def main():
    a = int(input("fahrenheit?"))
    c = int((a - 32)/1.8)
    print("celsius is", c )
    print("fahr is", a)
    reply = input("wanna continue?")
    if reply == ("yes"):
        main()
    else:
        print ("fine be that way")

main()



