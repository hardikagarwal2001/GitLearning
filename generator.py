char=['a','b','c','d','e','f','g','h','i',
'j','k','l','m','n','o','p','q','r','s','t',
'u','v','w','x','y','z','A', 'B', 'C','D', 
'E', 'F', 'G', 'H','I', 'J', 'K','M', 'N',
'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W',
 'X', 'Y', 'Z']
Digits=[1,2,3,4,5,6,7,8,9]
Sp_char=['@','#','$','%','^','*']
f=[1,2,3,4]
import random
h='y'
while h=='y':
    password=""
    print("PASSWORD GENERATOR")
    print("1.Alpha numeric")
    print("2.Alpha Numeric with special charachters")
    k=int(input("Enter Choice"))
    if k==1:
        for i in f:
            randdigit=str(random.choice(Digits))
            randchar=random.choice(char)
            password=password+randdigit+randchar
    if k==2:
        for i in f:
            randdigit=str(random.choice(Digits))
            randchar=random.choice(char)
            randsp=random.choice(Sp_char)
            password=password+randdigit+randchar+randsp
    print(password)
    j=input("Do you want to save this password[y/n]")
    if j=='y':
        fh=open('savedpass.txt','a')
        fh.write(password+"\n")
        fh.close()
    h=input("Do you want to continue")        

