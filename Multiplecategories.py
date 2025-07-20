class multiplecategories():
     def OddEven():
        num=int(input("Enter a number:"))
        if((num%2==1)):
            print(num,('is even number:'))
        else:
            print(num,('is odd number:'))

     def Eligible():
        Gender=(input("Your Gender:"))
        age=int(input("your Age:"))
        if(Gender=="male"or"Male") and(age<=20):
            print("NOT ELIGIBLE")
        elif(Gender==female) and(age<=18):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")

     def percentage():
        S1=int(input("SUBJECT1="))
        S2=int(input("SUBJECT2="))
        S3=int(input("SUBJECT3="))
        S4=int(input("SUBJECT4="))
        S5=int(input("SUBJECT5="))
        Tot=(S1+S2+S3+S4+S5)
        print("Total:",Tot)
        percent=Tot/5
        print("percentage:",percent)

     def triangle():
        Ht=int(input("Height:"))
        Br=int(input("Breadth:"))
        print("Area Fromula:(Height*Breadth)/2")
        print("Area of triangle:",(Ht*Br/2))
        Ht1=int(input("Height1:"))
        Ht2=int(input("Height2:"))
        Br1=int(input("Breadth:"))
        print("perimeter formula:Height1+Height2+Breadth")
        print("perimeter of traingle:",Ht1+Ht2+Br1)
