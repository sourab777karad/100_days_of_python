#bill divider and GST calculater

print("*************************WELCOME********************************")

bill = float(input("enter the total bill :"))
people = int(input("enter total members :"))
#bill perperson 
#tip given
GST = int(input("enter the percentage of GST for item : 10, 15, 20 :"))
#payment
payment = GST / 100 * bill + bill
print("final payment is :", payment)
each_person = payment / people
print("if dividing the bill each person has to pay :", each_person)
#payment of each person after adding the tip

print("*************************THANK YOU*******************************")


