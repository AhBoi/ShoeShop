def menu1(a):
    print(" ")
    print(" ")
    print("//What would you like to do?")
    print("A) Check Shopping Cart list")
    print("B) Buy new shoes from our 'LARGE' selection")
    print("C) Check total price of the items in Shopping Cart")
    print("D) Checkout new promotions")
    print("E) Proceed to checkout")
    print("F) Remove item from Shopping Cart")
    print("G) Quit the shop")
    a = input("//Answer: ")
    return a;
def menu(a):
    a = menu1(a="A")
    if a == "A":
        print(" ")
        print(" ")
        i = 0
        x = len(shoppingcart)
        if x == 0:
            print("//Your Shopping Cart is empty!")
            a = menu2(a="A")
        else:
            print("//The items in your Shopping Cart:")
            while i < x:
                print(shoppingcart[i])
                i += 1
            a = menu2(a="A")
    elif a == "B":
        b = sure(a="A")
    elif a == "C":
        print(" ")
        print(" ")
        i = 0
        x = len(shoppingcart)
        if x == 0:
            print("//Your Shopping Cart is empty!")
            a = menu2(a="A")
        else:
            print("//The items in your Shopping Cart:")
            while i < x:
                print(shoppingcart[i])
                i += 1
            summ = sum(shoppingcart1)
            print("//Total Cost: $"+str(summ)+".")
            a = menu2(a="A")
    elif a == "D":
        a = random(a="A")
    elif a == "E":
        print(" ")
        print(" ")
        print("//Are you sure you want to proceed to checkout your items?(Y/N)")
        abc = input("//Answer: ")
        while abc != "Y" and "N":
            print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, Y/N")
            print("//Are you sure you want to proceed to checkout your items?(Y/N)")
            abc = input("//Answer: ")
        if abc == "N":
            sad = menu2(a="A")
        elif abc == "Y":
            print(" ")
            print(" ")
            i = 0
            x = len(shoppingcart)
            if x == 0:
                print("//Your Shopping Cart is empty!")
                a = menu2(a="A")
            else:
                print("//The items in your Shopping Cart are:")
                while i < x:
                    print(shoppingcart[i])
                    i += 1
                summ = sum(shoppingcart1)
                print("//The total cost of all the items are $"+str(summ)+".")
                sd = location1(a = "A")
                r = shoppingcart.clear()
                rr = shoppingcart1.clear()
    elif a == "F":
        a = menuremover1(a="A")
    elif a == "G":
        print(" ")
        print(" ")
        print("//Good Bye!Come Back Soon!")
        quit
    else:
        print(" ")
        print(" ")
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, A/B/C/D/E/F")
        a = menu2(a="A")
def menu2(a):
    a = menu1(a="A")
    if a == "A":
        print(" ")
        print(" ")
        i = 0
        x = len(shoppingcart)
        if x == 0:
            print("//Your Shopping Cart is empty.")
            a = menu1(a="A")
        else:
            print("//The items in your Shopping Cart:")
            while i < x:
                print(shoppingcart[i])
                i += 1
            a = menu1(a="A")
    elif a == "B":
        b = sure(a = "A")
    elif a == "C":
        print(" ")
        print(" ")
        i = 0
        x = len(shoppingcart)
        if x == 0:
            print("//Your Shopping Cart is empty!")
            a = menu1(a="A")
        else:
            print("//The items in your Shopping Cart:")
            while i < x:
                print(shoppingcart[i])
                i += 1
            summ = sum(shoppingcart1)
            print("//Total Cost: $"+str(summ)+".")
            a = menu1(a="A")
        a = menu(a="A")
    elif a == "D":
        a = random(a="A")
    elif a == "E":
        print(" ")
        print(" ")
        print("//Are you sure you want to proceed to checkout your items?(Y/N)")
        abc = input("//Answer: ")
        while abc != "Y" and "N":
            print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, Y/N")
            print("//Are you sure you want to proceed to checkout your items?(Y/N)")
            abc = input("//Answer: ")
        if abc == "N":
            sad = menu(a="A")
        elif abc == "Y":
            print(" ")
            print(" ")
            i = 0
            x = len(shoppingcart)
            if x == 0:
                print("//Your Shopping Cart is empty!")
                a = menu(a="A")
            else:
                print("//The items in your Shopping Cart are:")
                while i < x:
                    print(shoppingcart[i])
                    i += 1
                summ = sum(shoppingcart1)
                print("//The total cost of all the items are $"+str(summ)+".")
                sd = location1(a = "A")
                r = shoppingcart.clear()
                rr = shoppingcart1.clear()
    elif a == "F":
        a = menuremover1(a="A")
    elif a == "G":
        print(" ")
        print(" ")
        print("//Good Bye! Come back soon!!!")
        quit
    else:
        print(" ")
        print(" ")
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, A/B/C/D/E/F")
        a = menu(a="A")
def menuremover1(a):
    print(" ")
    print(" ")
    i = 0
    x = len(shoppingcart)
    while i < x:
        print(shoppingcart[i])
        i += 1
    remove = int(input("//What item do you want to remove from the list(The first item that shows is 1 then 2 then so on): "))
    remover = remove - 1
    if remover >= x:
        print("//Sorry the number you put exceeded the number of items you have on the list")
        a = menuremover2(a="A")
    else:
        print("//"+str(shoppingcart[remover]),"has been removed from your Shopping Cart")
        shoppingcart.pop(remover)
        a = menu(a ="A")
        return a;
def menuremover2(a):
    print(" ")
    print(" ")
    i = 0
    x = len(shoppingcart)
    while i < x:
        print(shoppingcart[i])
        i += 1
    remove = int(input("//What item do you want to remove from the list(The first item that shows is 1 then 2 then so on): "))
    remover = remove - 1
    if remover >= x:
        print("//Sorry the number you stated exceeded the number of items you have on the list.")
        a = menuremover1(a="A")
    else:
        print("//"+str(shoppingcart[remover]),"has been removed from your Shopping Cart")
        shoppingcart.pop(remover)
        shoppingcart1.pop(remover)
        a = menu(a ="A")
        return a;

#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES#SIZES
def sizes(a):
    a = input("Please enter your shoe size: ")
    print("Are you sure your shoe size is",str(a)+"?")
    b = input("Answer(Y/N): ")
    while b != "Y" and "N":
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, Y/N")
        b = input("Answer(Y/N): ")
    if b == "Y":
        print("Confirmed!")
    if b == "N":
        print("OK! Try Again!")
        asd = size(a = "a")
def size(a):
    a = input("Please enter your shoe size: ")
    print("Are you sure your shoe size is",str(a)+"?")
    b = input("Answer(Y/N): ")
    while b != "Y" and "N":
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, Y/N")
        b = input("Answer(Y/N): ")
    if b == "Y":
        print("Confirmed!")
    if b == "N":
        print("OK! Try Again!")
        asd = sizes(a = "a")

#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION#LOCATION
def location(a):
    print(" ")
    print(" ")
    name = input("//Full Name: ")
    phno = int(input("//Mobile Number: "))
    pinnn = int(input("//Pincode: "))
    address = input("//Address: ")
    print("//SystemAre you sure you are",str(name),"number",str(phno),", and you stay at",str(pinnn)+","+str(address))
    a = input("//Answer(Y/N): ")
    return a;
def location1(a):
    a = location(a="A")
    if a == "Y":
        print("//Confirmed!")
        b =card(a="A")
    elif a == "N":
        print("//OK! Try again!")
        B = location2(a="A")
    else:
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, Y/N")
        B = location2(a="A")
def location2(a):
    a = location(a="A")
    if a == "Y":
        print("//Confirmed!")
        b = card(a="A")
    elif a == "N":
        print("//OK! Try again!")
        b = location1(a="A")
    else:
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, Y/N")
        b = location1(a="A")

#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT#PAYMENT
def payment(a):
    print(" ")
    print(" ")
    print("//Select a payment method:")
    print("A) Master Card")
    print("B) Credit Card")
    print("C) Debit Card")
    print("D) Net Banking")
    a = input("//Answer: ")
    return a;
def card(a):
    a = payment(a="A")
    print(" ")
    print(" ")
    while a != "A" and a != "B" and a != "C" and a != "D":
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, A/B/C/D")
        a = payment(a = "A")
    if a == "A":
        no = input("//Card Number: ")
        name = input("//Name on card(ALL CAPS): ")
        exd = input("//Expiry Date(MM/YY): ")
        cvv = input("//CVV Number: ")
        a= cardtroll(a="A")
    elif a == "B":
        no = input("//Card Number: ")
        name = input("//Name on card(ALL CAPS): ")
        exd = input("//Expiry Date(MM/YY): ")
        cvv = input("//CVV Number: ")
        passw = input("//Password: ")
        a= cardtroll(a="A")
    elif a == "C":
        no = input("//Card Number: ")
        name = input("//Name on card(ALL CAPS): ")
        exd = input("//Expiry Date(MM/YY): ")
        cvv = input("//CVV Number: ")
        passw = input("//Password: ")
        a= cardtroll(a="A")
    elif a == "D":
        bank = input("//What is your Bank(Full Name): ")
        username = input("//Username: ")
        password = input("//Password: ")
        a= cardtroll(a="A")

#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL#CARDTROLL
def cardtroll(a):
    print(" ")
    print(" ")
    import random
    x = random.randint(1,2)
    if x == 1:
        print("//OH NO! Your card has been declined. Please try again with another care or change payment methods!")
        a = card(a="A")
    if x == 2:
        print("//Your items will be shipped to ur address within a week!")
        a = wow(a = "A")
def wow(a):
    print(" ")
    print(" ")
    print("//Would you like to buy again or quit the shop?")
    print("A) Shop Again")
    print("B) Quit")
    hi = input("//Answer: ")
    while hi != "A" and "B":
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, A/B")
        print("Would you like to buy again or quit the shop?")
        print("A) Shop Again")
        print("B) Quit")
        hi = input("//Answer: ")
    if hi == "A":
        a = menu(a="A")
    elif hi == "B":
        print("//Good Bye!Come Back Soon!")
        quit

#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM#RANDOM
def random(a):
    print(" ")
    print(" ")
    import random
    x = random.randint(1,5)
    if x == 1:
        print("//WOOO HOOO! It's yer' lucky day one for one shoes for the price of 2")
        a = menu(a="A")
    elif x == 2:
        print("//Wowzers! Yee lad got yee some god ol' promotion! 2 for one meal with a perchase over $1000!(Disclaimer! There is no meal)")
        a = menu(a="A")
    elif x == 3:
        print("//Wow you got a spawny outcome! You gon' get a free shoe for free. nah jokes u pay for the shoe and i get the shoe")
        a = menu(a="A")
    elif x == 4:
        print("//CONGRATS! You won a free 20% off any purchase using the code 'iambest'")
        a = menu(a="A")
    elif x == 5:
        print("//ERROR.....ERROR.....ERROR.....")
        a = menu(a="A")
        
#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM#DOUBLECFM
def sure(a):
    print(" ")
    print(" ")
    order = orderer(a="A")
    size = sizes(a="A")
    print("//Are you sure you want to add",str(order),"Size:",size,"into your shopping cart?")
    cart = input("//Answer(Y/N): ")
    if cart == "Y":
        shoppingcart.append(order)
        print("//"+str(order),"has been added into your shopping cart!")
        if order == N[0] or order == N[1] or order == N[2] or order == N[3]:
            shoppingcart1.append(NIKI[order])
        elif order == I[0] or order == I[1] or order == I[2] or order == I[3]:
            shoppingcart1.append(ISEEDADS[order])
        elif order == L[0] or order == L[1] or order == L[2] or order == L[3]:
            shoppingcart1.append(LANS[order])
        elif order == MM[0] or order == MM[1] or order == MM[2] or order == MM[3]:
            shoppingcart1.append(MATAM[order])
        elif order == MW[0] or order == MW[1] or order == MW[2] or order == MW[3]:
            shoppingcart1.append(MATAW[order])
        a = menu(a="A")
    elif cart =="N":
        print("//"+str(order),"has been cancelled!")
        print("//What would you like to do next?")
    else:
        print("//Sorry work in progress. Please restate your answer")
        a = sure1(a="A")
def sure1(a):
    print(" ")
    print(" ")
    order = orderer(a="A")
    size = sizes(a="A")
    print("//Are you sure you want to add",str(order),"Size:",size,"into your shopping cart?")
    cart = input("//Answer(Y/N): ")
    if cart == "Y":
        shoppingcart.append(order)
        print("//"+str(order),"has been added into your shopping cart!")
        if order == N[0] or order == N[1] or order == N[2] or order == N[3]:
            shoppingcart1.append(NIKI[order])
        elif order == I[0] or order == I[1] or order == I[2] or order == I[3]:
            shoppingcart1.append(ISEEDADS[order])
        elif order == L[0] or order == L[1] or order == L[2] or order == L[3]:
            shoppingcart1.append(LANS[order])
        elif order == MM[0] or order == MM[1] or order == MM[2] or order == MM[3]:
            shoppingcart1.append(MATAM[order])
        elif order == MW[0] or order == MW[1] or order == MW[2] or order == MW[3]:
            shoppingcart1.append(MATAW[order])
        a = menu(a="A")
    elif cart =="N":
        print("//"+str(order),"has been cancelled!")
        print("//What would you like to do next?")
    else:
        print("//Sorry work in progress. Please restate your answer")
        a = sure(a="A")

#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE#SURE
def cfm(a):
    print(" ")
    print(" ")
    print("//Are you sure you want to check out?")
    a= input("//Answer(Y/N): ")
    if a == "Y":
        a = card(a="A")
    if a == "N":
        a = menu(a="A")
    else:
        print("//Sorry work in progress. Please restate your answer")
        a = cfm1(a="A")
def cfm1(a):
    print(" ")
    print(" ")
    print("//Are you sure you want to check out?")
    a= input("//Answer(Y/N): ")
    if a == "Y":
        a = card(a="A")
    if a == "N":
        a = menu(a="A")
    else:
        print("//Sorry work in progress. Please restate your answer")
        a = cfm(a="A")

#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER#ORDER
def orderer(a):
    a = ANS(a="A")
    return a;

#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START#START
def ANSNASNAS(a):
    print(" ")
    print(" ")
    print("//What type of shoes would you like to buy?")
    print("A) Sports Shoe")
    print("B) Sneakers")
    print("C) Yeezys")
    print("D) Sandals")
    a = input("//Answer: ")
    return a;
def ANSANS(a):#Function 1.0
    a = ANSNASNAS(a="a")
    if a == "A":
        a = niki(a="a")
        return a;
    elif a == "B":
        a = lans(a="a")
        return a;
    elif a == "C":
        a =iseedads(a="A")
        return a;
    elif a == "D":
        a = mata1(a="A")
        return a;
    else:
        print("//Sorry work in progress,so i could not proess what you wrote.Please write either letters, A/B/C/D")
        a = ANS(a="a")
        return a;

def ANS(a):#Function 1.0 repeat
    a = ANSNASNAS(a="A")
    if a == "A":
        a = niki(a="a")
        return a;
    elif a == "B":
        a = lans(a="a")
        return a;
    elif a == "C":
        a = iseedads(a="A")
        return a;
    elif a == "D":
        a = mata1(a="A")
        return a;
    else:
        print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
        a = ANSANS(a="a")
        return a;

#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI#NIKI
def nikinikiniki(a):
    print(" ")
    print(" ")    
    print("//Choose from our 'large' selection of Sports Shoes!")
    print("A)",N[0])
    print("B)",N[1])
    print("C)",N[2])
    print("D)",N[3])
    print("E) $FREE Niki's New & Improved Self-Moving Shoes!")
    print("//To go back to the previous question,type 'BACK' in the answer below")
    a = input("//Answer: ")
    return a;
def nikiniki(a):
    a = nikinikiniki(a="a")
    if a == "A":
        return (N[0]);
    elif a == "B":
        return (N[1]);
    elif a == "C":
        return (N[2]);
    elif a == "D":
        return (N[3])
    elif a == "E":
        print("//Sorry product has been SOLD OUT!")
        print("//Please choose another option!")
        a = niki(a="a")
    elif a == "BACK":
        a = ANS(a = "a")
    else:
        print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
        a = niki(a="a")
        return a;
def niki(a):
    a = nikinikiniki(a="a")
    if a == "A":
        return (N[0]);
    elif a == "B":
        return (N[1]);
    elif a == "C":
        return (N[2]);
    elif a == "D":
        return (N[3]);
    elif a == "E":
        print("//Sorry product has been SOLD OUT!")
        print("//Please choose another option!")
        a = nikiniki(a="a")
    elif a == "BACK":
        a = ANS(a="a")
    else:
        print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
        a = nikiniki(a="a")
        return a;

#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS#LANS
def lanslanslans(a):
    print(" ")
    print(" ")
    print("//Choose from our 'large' selection of Sneakers!")
    print("A)",L[0])
    print("B)",L[1])
    print("C)",L[2])
    print("D)",L[3])
    print("E) $1 Lans' Spinning Shoe!")
    print("//To go back to the previous question,type 'BACK' in the answer below")
    a = input("//Answer: ")
    return a;
def lanslans(a):
    a = lanslanslans(a="a")
    if a == "A":
        return (L[0]);
    elif a == "B":
        return (L[1]);
    elif a == "C":
        return (L[2]);
    elif a == "D":
        return (L[3]);
    elif a == "E":
        print("//Sorry product has been SOLD OUT!")
        print("//Please choose another option!")
        a = lans(a="a")
    elif a == "BACK":
        a = ANS(a="a")
    else:
        print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
        a = lans(a="a")
        return a;
def lans(a):
    a = lanslanslans(a="a")
    if a == "A":
        return (L[0]);
    elif a == "B":
        return (L[1]);
    elif a == "C":
        return (L[2]);
    elif a == "D":
        return (L[3]);
    elif a == "E":
        print("//Sorry product has been SOLD OUT!")
        print("//Please choose another option!")
        a = lanslans(a="a")
    elif a == "BACK":
        a = ANS(a="a")
    else:
        print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
        a = lanslans(a="a")
        return a;

#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS#ISEEDADS
def iseedadsiseedadsiseedads(a):
    print(" ")
    print(" ")
    print("//Choose from our 'large' selection of Yeezys!")
    print("A)",I[0])
    print("B) $1500 Iseedads' Yacht Club Yezys!")
    print("C)",I[1])
    print("D)",I[2])
    print("E)",I[3])
    print("//To go back to the previous question,type 'BACK' in the answer below")
    a = input("//Answer: ")
    return a;
def iseedadsiseedads(a):
    a = iseedadsiseedadsiseedads(a="a")
    if a == "A":
        return (I[0]);
    if a == "B":
        print("//Sorry product has been SOLD OUT!")
        print("//Please choose another option!")
        a = iseedads(a="a")
    if a == "C":
        return (I[1]);
    if a == "D":
        return (I[2]);
    if a == "E":
        return (I[3]);
    if a == "BACK":
        a = ANS(a="a")
    else:
        print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
        a = iseedads(a="a")
        return a;
def iseedads(a):
    a = iseedadsiseedadsiseedads(a="a")
    if a == "A":
        return (I[0]);
    elif a == "B":
        print("//Sorry product has been SOLD OUT!")
        print("//Please choose another option!")
        a = iseedadsiseedads(a="a")
    elif a == "C":
        return (I[1]);
    elif a == "D":
        return (I[2]);
    elif a == "E":
        return (I[3]);
    elif a == "BACK":
        a = ANS(a="a")
    else:
        print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
        a = iseedadsiseedads(a="a")
        return a;

#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA#MATA
def mata1(a):
    print(" ")
    print(" ")
    print("//Which gender you would like to buy the sandals for?(Male/Female)")
    print("//OR")
    print("//Type 'BACK' in the Answers and go back to the main menu")
    mati = input("//Answer: ")
    if mati == "MALE":
        print(" ")
        print(" ")
        print("//Choose from our 'large' selection of Mens Sandals!")
        print("A)",MM[0])
        print("B)",MM[1])
        print("C)",MM[2])
        print("D)",MM[3])
        print("E) $DEATH Mens Mata's Mati Sandals")
        print("//To go back to the previous question,type 'BACK' in the answer below")
        a = input("//Answer: ")
        if a == "A":
            return (MM[0]);
        elif a == "B":
            return (MM[1]);
        elif a == "C":
            return (MM[2]);
        elif a == "D":
            return (MM[3]);
        elif a == "E":
            print(" ")
            print(" ")
            print("//Sorry product has been SOLD OUT!")
            print("//Please choose another option!")
            a = mata2(a="a")
        elif a == "BACK":
            a = ANS(a="a")
        else:
            print(" ")
            print(" ")
            print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
            a = mata2(a="a") 
    elif mati == "FEMALE":
        print(" ")
        print(" ")
        print("//Choose from our 'large' selection of Womens Sandals!")
        print("A) $43 Mata's Ladies Bushy Sandals")
        print("B)",MW[0])
        print("C)",MW[1])
        print("D)",MW[2])
        print("E)",MW[3])
        print("//To go back to the previous question,type 'BACK' in the answer below")
        a = input("//Answer: ")
        if a == "A":
            print(" ")
            print(" ")
            print("//Sorry product has been SOLD OUT!")
            print("//Please choose another option!")
            a = matia1(a="a")
        elif a == "B":
            return (MW[0]);
        elif a == "C":
            return (MW[1]);
        elif a == "D":
            return (MW[2]);
        elif a == "E":
            return (MW[3]);
        elif a == "BACK":
            a = ANS(a="a")
        else:
            print(" ")
            print(" ")
            print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
            a = mata2(a="a")
    elif mati == "BACK":
        a = ANS(a="A")
    else:
        print("//Sorry i do not understand what you are trying to say, please try again!")
        b = mata2(a="a")
        return b;
def mata2(a):
    print(" ")
    print(" ")
    print("//Which gender you would like to buy the sandals for?(MALE/FEMALE)")
    print("//OR")
    print("//Type 'BACK' in the Answers and go back to the main menu")
    mati = input("//Answer: ")
    if mati == "MALE":
        print(" ")
        print(" ")
        print("//Choose from our 'large' selection of Mens Sandals!")
        print("A)",MM[0])
        print("B)",MM[1])
        print("C)",MM[2])
        print("D)",MM[3])
        print("E) $DEATH Mens Mata's Mati Sandals")
        print("//To go back to the previous question,type 'BACK' in the answer below")
        a = input("//Answer: ")
        if a == "A":
            return (MM[0]);
        elif a == "B":
            return (MM[1]);
        elif a == "C":
            return (MM[2]);
        elif a == "D":
            return (MM[3]);
        elif a == "E":
            print(" ")
            print(" ")
            print("//Sorry product has been SOLD OUT!")
            print("//Please choose another option!")
            a = mata1(a="a")
        elif a == "BACK":
            a = ANS(a="a")
        else:
            print(" ")
            print(" ")
            print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
            a = mata1(a="a")
    elif mati == "FEMALE":
        print(" ")
        print(" ")
        print("//Choose from our 'large' selection of Womens Sandals!")
        print("A) $43 Mata's Ladies Bushy Sandals")
        print("B)",MW[0])
        print("C)",MW[1])
        print("D)",MW[2])
        print("E)",MW[3])
        print("//To go back to the previous question,type 'BACK' in the answer below")
        a = input("//Answer: ")
        if a == "A":
            print(" ")
            print(" ")
            print("//Sorry product has been SOLD OUT!")
            print("//Please choose another option!")
            a = matia1(a="a")
        elif a == "B":
            return (MW[0]);
        elif a == "C":
            return (MW[1]);
        elif a == "D":
            return (MW[2]);
        elif a == "E":
            return (MW[3]);
        elif a == "BACK":
            a = ANS(a="a")
        else:
            print(" ")
            print(" ")
            print("//Sorry work in progress,so i could not prcoess what you wrote.Please write either letters, A/B/C/D")
            a = mata1(a="a")
    elif mati == "BACK":
        a = ANS(a="A")
    else:
        print(" ")
        print(" ")
        print("//Sorry i do not understand what you are trying to say, please try again!")
        a = mata1(a="a")
        return a;

#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL#NORMAL
N = ["$240 Niki's Earth Force","$150 Niki's Earth Max","$250 Niki's Yboc IV","$110 Niki's Flexor"]
NIKI = {N[0]:240,N[1]:150,N[2]:250,N[3]:110}
L = ["$60 Lans' New Flaming Seoul","$65 Flaming Checkers Sky-Hi","$60 Lans' New Boat Group Seoul","$55 Popping Camels Authentic"]
LANS = {L[0]:60,L[1]:65,L[2]:60,L[3]:55}
I = ["$400 Iseedads' Yeezy Booster 701 'Waver sprint'","$225 Iseedads' Yeezy energyphazer 'Calabrating'","$1,190 Iseedads' Yeezy 005 'Pepper'","$326 Iseedads' Yeezy Seasoning 6 'Andesite'"]
ISEEDADS = {I[0]:400,I[1]:225,I[2]:1190,I[3]:326}
MM = ["$20 Mata's Men Octuple Strappy Cork Sandals","$20 Mata's Men Winter Sandals","$39 Brenwin Men Opened Toe Sandals","$35 Brenwin Men Sports Thong"]
MATAM = {MM[0]:20,MM[1]:20,MM[2]:39,MM[3]:35}
MW = ["$44 Mata's Ladies Flat Sandals","$39 Mata's Comfortable Ladies Sandals","$44 Mata's Ladies Cage Sandals","$39 Mata's Ladies Octuple Strap Mules Sandals"]
MATAW = {MW[0]:44,MW[1]:39,MW[2]:44,MW[3]:39}
shoppingcart = []
shoppingcart1 = []
print("//Welcome to Shooeee!") #For Copyright issues we changed the name a little...
print("We have many different Brands of shoes in stock:")
print("From Niki to Iseedads!")
print("From Vanys to Mata!")
print("From Sports shoes to Sneakers!")
print("From Yeezys to Sandals!")
ab = menu(a="A")
