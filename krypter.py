key = 12
options = 0
letters = []

while True: #loop meny
    try:
        options = int(input("1 för kryptera\n2 för avkryptera\n3 för att avsluta\n>"))
    except:
        print("skriv 1-3 endast")
    if options == 1:
        letters = []
        word = input("input här\n>")
        for letter in word:
            letters.append(ord(letter) + key) #kryptera med key 12
        print(letters)
    elif options == 2:
        crypt = []
        for l in letters:
            crypt.append(chr(l -key)) #avkryptera
        print(crypt)
    elif options == 3:
        break