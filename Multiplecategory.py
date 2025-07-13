class multicategory():
    def oddeven():
        num=int(input("Enter a number:"))
        if((num%2)==1):
            print("odd number")
            message="odd number"
        else:
            print("even number")
            message="even number"
        return message
        
    def BMI():
        BMI=int(input("Enter the BMI Index"))
        if(BMI<18.5):
            print("Underweight")
            message="Underweight"
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<34.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Obese")
            message="Obese"
        return message
        
    def age():
        age=int(input("Enter the Age:"))
        if(age<=18):
            print("children")
            message="children"
        elif(age<35):
            print("Adult")
            message="Adult"
        elif(age<59):
            print("Citizen")
            message="Citizen"
        else:
            print("Senior Citizen")
            message="Senior Citizen"
        return message