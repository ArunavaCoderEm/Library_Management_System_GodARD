# # Library Management Python

import datetime

nowdatetime = datetime.datetime.now()


print("\nWelcome To Our GodARD Library \n\n")
name = input("Enter Your Full Name - ")

# If You Want To Add More Books And Author Please Add In The Mentioned Format - 'author':['book1','book2',...,'author books'],
# HERE ----
BooksAuthor = {
    'sir arthur conan doyle'  : ['sherlock holmes','sir nigel'],
    'satyajit roy'            : ['feluda somogro', 'professor shonku'],
    'sharadindu bondopadhyay' : ['byomkesh somogro','tungabhodrar tire'],
    'agatha christie'         : ['hercule poirot', 'the pale horse']
}
# ----

author = []
for auth in list(BooksAuthor.keys()):
    author.append(auth)
books = []
for book in list(BooksAuthor.values()):
    for u in book:
        books.append(u)
checkoutbooks = []   
retbooks = []
RetOrTake = input("Hello ! Will You Take A Book Or Return ? (take // return) \n").lower()
if (RetOrTake != 'take' or RetOrTake != 'return'):
    while (RetOrTake != 'take' and RetOrTake != 'return'):
        print("Please provide us the correct answer")
        RetOrTake = input("Hello ! Will You Take A Book Or Return ? (take // return) \n").lower()
if (RetOrTake == 'take'):
    userpref = input("Okay ! What do you want ? Mention (book // author) \n").lower()
    if (userpref == 'book'):
        user = input("What Books Do You Want ?\n").lower()
        if (user not in books):
            while (user not in books):
                user = input("Not Available ! Any Other Books ?\n").lower()
        for bookh in books:
                if (user == bookh):
                    print(f"Yes we do have {user} book.")
                    checkoutbooks.append(user)
                    askagain = input("You okay with that or want some more ? (yes more // no more)\n").lower()
                    if (askagain == 'yes more'):
                        while (askagain != 'no more'):
                            agbook = input("Mention Book Name Or No More ? \n").lower()
                            if (agbook in books):
                                checkoutbooks.append(agbook)
                            elif (agbook == 'no more'):
                                break
                            else :
                                print("Not available")
                                askagain = input("Anything else ? (yes more // no more) - ").lower()
                    if (askagain == 'no more' or agbook == 'no more'):
                        print("Okay ! - The Books You Are Taking This Time Are Shown Below - ")
                        print(f"Name = {name} || Date & Time = {nowdatetime} || File Created")
                        bcd = (f"Name = {name} || Date & Time = {nowdatetime} || File Created")
                        with open (f'{name}.txt' , 'w') as file :
                            data1 = file.write(f"{bcd}\n")
                            for r in range (len(checkoutbooks)):
                                abc = (f"{r+1}. {checkoutbooks[r]}")
                                print(f"{r+1}. {checkoutbooks[r]}")
                                data = file.write(f"{abc} \n")
                            print("Signed By GodArd.")
                            cde = ("\n\tSigned By GodArd.")
                            data2 = file.write(f"{cde}\n")
    if (userpref == 'author'):
        authask = input("Please Name The Author - ").lower()
        if (authask not in author):
            while (authask not in author):
               authask = input("Author Not Available Name Any Other Author \n").lower()
        if (authask in author):
            print(f"Yes We Do Have {authask} 's Books And Here They Are -\n")
            print(BooksAuthor[authask])
            authbookask = input("Enter The Books You Want From The List -\n").lower()
            if (authbookask in list(BooksAuthor[authask])):
                checkoutbooks.append(authbookask)
            anyt = input("Okay ! Anything More ? (yes // no)\n").lower()
            if (anyt == 'yes'):
                while (anyt != 'no'):
                    anyt = input("Book Name From List Or No ?\n").lower()
                    if (anyt in list(BooksAuthor[authask])):
                        checkoutbooks.append(anyt)
                    elif (anyt not in list(BooksAuthor[authask])):
                        print("Not Available")
                        anyt = input("Anything More From The List ? Yes Or NO ?\n").lower()
            if (anyt == 'no'):
                print("Okay ! - The Books You Are Taking This Time Are Shown Below - ")
                print(f"Name = {name} || Date & Time = {nowdatetime} || File Created")
                bcd = (f"Name = {name} || Date & Time = {nowdatetime} || File Created")
                with open (f'{name}.txt' , 'w') as file :
                    data1 = file.write(f"{bcd}\n")
                    for r in range (len(checkoutbooks)):
                        abc = (f"{r+1}. {checkoutbooks[r]}")
                        print(f"{r+1}. {checkoutbooks[r]}")
                        data = file.write(f"{abc} \n")
                    print("Signed By GodArd.")
                    cde = ("\n\tSigned By GodArd.")
                    data2 = file.write(f"{cde}\n")
if (RetOrTake == 'return'):
    print("How Many Books Do You Want To Return ? \n")
    num = int(input())
    for iz in range (num):
        retb = input(f"Name Book Number {iz+1} And Give It To Me -\n").lower()
        retbooks.append(retb)
        books.append(retb)
    print(f"You, {name} Have Returned The Under Mentioned Books On {nowdatetime}-\n")
    zzz = (f"You, {name} Have Returned The Under Mentioned Books On {nowdatetime}-\n")
    with open (f'{name}.txt','w') as f1:
        data1 = f1.write(f'{zzz} \n')
        for yu in range (0, len(retbooks)):
            print(f"{yu+1}. {retbooks[yu]} (returned).")
            zzzz = (f"{yu+1}. {retbooks[yu]} (returned).")
            data2 = f1.write(f'{zzzz} \n')
        print("\n\tSigned By GodARD.")
        zzz_e = ("\n\tSigned By GodARD.")
        data3 = f1.write(f'{zzz_e} \n')
        
print("Thanks For Visiting Our Library , Do Visit Again.")