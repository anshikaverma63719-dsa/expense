#Expense Tracker
expenselist=[]
print("Hello!👋")

print("========Welcome to Expense Tracker 🙏=========")
print("press 1.Add expense:")
print("press 2. View all expense:")
print("press 3. View Total:")
print("press 4. Exit:")
print("========Let's Get Started=========")

choice=int(input("Enter a number:"))
#add expense...................
if(choice==1):
    date=input("Enter the date when the expense was incurred:")
    category=input("Select the category for your expense(e.g., Food,Travel,Shopping,Health,Education):")
    description=input("Enter a brief description of your expense:")
    amount=float(input("Enter the amount you spent:"))
    
    expense={
        "date":date,
        "category":category,
        "description":description,
        "amount":amount
    }
    expenselist.append(expense)
    print("\n -----Done 👍 Expense is added succesfully-----")
    #View all expense...........
elif(choice== 2):
        if(len(expenselist)==0):
            print("\n No expense")
        else:
            print("\n This is your expences:")
            count=1
            for each in expenselist:
                print(f"expense number{count}->{each["date"]},{each["category"]},{each["description"]},{each["amount"]}")
                count+=1
                #Total.....
elif(choice==3):
            total=0
            for each in expenselist:
                total+=each["amount"]

            print("\n your total expence:",total)
    #exit
elif(choice==4):
        print(" I hope you are doing well.\n Thankyou for using the 'Expense Tracker'.\n I hope it helps you manage your expenses more easily.\nHave a great Day!🙂")

else:
    print("invalid try again:")
