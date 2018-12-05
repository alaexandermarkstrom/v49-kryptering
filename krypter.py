word = "test"
key = 12 # här kan komplexiteten av programmet ökas, vilken chiffer är det?
letters = []
crypt = []
options = 0

while True: #loop meny
    try:
        options = int(input("1 för kryptera\n2 för avkryptera\n3 för att avsluta\n>"))
    except:
        print("skriv 1-3 endast")
    if options == 1:
        for letter in word:
            letters.append(ord(letter) + key) # (kryptera) ta en bokstav i taget från variabel "word" och omvandla den till ett nummer och + key (100 + 12 = 112)
        print(letters)
    elif options == 2:
        for l in letters:
            crypt.append(chr(l -key)) # avkryptera
        print(crypt) # hur skriver du ut det här som en sträng
    elif options == 3:
        break