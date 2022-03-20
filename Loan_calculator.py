print("Welcome to Global 4's Loan eligability calculator\n")
print("We offer loans ranging from $1000 to $15,000 USD\n")
print("Answer the following 22 questions to find out the maximum loan amount you are eligable for.\n")
print("*For multiple choice questions, answer by entering the letter corresponding to your chosen answer*\n")

Score = []

##################################################################################################################################################
#Minimum requirements
print("~Minimum requirements~\n")

#Question 1
while True:      # keep looping until we break out of the loop
    q1 = input("1. Are you currently in bankruptcy?\n" 
               + "A) Yes\n" + "B) No\n")
    if q1.upper() == "A":
        print("Unfortunately, you are not eligable for a loan.")
        raise SystemExit(0)    #Programme exits
    elif q1.upper() == "B":
        break     #Breaks out of the while loop
    else:
        print("Invalid choice")  #The while loop will repeat
        

#Question 2
while True:
    q2 = input("2. Have you received a violent or financial criminal conviction within the last 5 years?\n" 
               + "A) Yes\n" + "B) No\n")
    if q2.upper() == "A":
        print("Unfortunately, you are not eligable for a loan.")
        raise SystemExit(0)
    elif q2.upper() == "B":
        break
    else:
        print("Invalid choice")  
        
   
#Question 3
while True:
    q3 = input("3. Will you use the loan for:\n"
               + "-Selling drugs, pawn shops, weapons, MLM, or adult entertainment\n"
               + "-Refinancing debt\n" + "-Buying stock or equity\n"
               + "A) Yes\n" + "B) No\n")
    if q3.upper() == "A":
        print("Unfortunately, you are not eligable for a loan.")
        raise SystemExit(0)
    elif q3.upper() == "B":
        break
    else:
        print("Invalid choice")


##################################################################################################################################################
'''
#####THIS SECTION IS NOT TO BE INCLUDED#####
#Personal details
print("~Personal details~\n")

#Question 4
while True:
    q4 = input("4. What is your gender?\n" 
               + "A) Male\n" + "B) Female\n" + "C) Other\n")
    if q4.upper() == "A":
        Gender = "Male"
        break
    elif q4.upper() == "B":
        Gender = "Female"
        break
    elif q4.upper() == "C":
        Gender = "Other"
        break
    else:
        print("Invalid choice")
        
    
#Question 5
ethnic_groups = {"A":"Boran", "B":"Embu", "C":"Gabbra", "D":"Iteso",
                 "E":"Kalenjin", "F":"Kamba", "G":"Kikuyu", "H":"Kisii",
                 "I":"Kuria", "J":"Luhya", "K":"Luo", "L":"Maasai",
                 "M":"Mbere", "N":"Meru", "O":"Mijikenda/Swahili", "P":"Orma",
                 "Q":"Pokomo", "R":"Rendille", "S":"Samburu", "T":"Somali",
                 "U":"Taita/Taveta", "V":"Turkana", "W":"Other"}              #Dictionary for the choosable ethnicities 

while True:
    print("5. What is your ethnicity?")
    for ethnicity in ethnic_groups:
        print(ethnicity+") "+ethnic_groups.get(ethnicity))   #Prints the options
    q5 = input()
    val = ethnic_groups.get(q5.upper())
    if val is not None:        #If the value is a key in the dicitonary
        Ethnicity = val
        break
    else:
        print("Invalid choice\n")      #Repeats the while loop
'''

##################################################################################################################################################
#Business information
print("~Business information~\n")

#Question 4
while True:
    q4 = input("4. How many paid employees does your business have, not including the owner?\n"
               + "A) 0\n" + "B) 1 - 10\n" + "C) 11 - 50\n" + "D) 51 - 100\n" + "E) More than 100\n")
    if q4.upper() == "A":
        Score.append(0)
        break
    elif q4.upper() == "B":
        Score.append(1)
        break
    elif q4.upper() == "C":
        Score.append(3)
        break
    elif q4.upper() == "D":
        Score.append(5)
        break
    elif q4.upper() == "E":
        Score.append(7)
        break
    else:
        print("Invalid choice")
        

#Question 5
while True:
    q5 = input("5. How many years have you been working in the industry of your business?\n"
               + "A) Less than 1 year\n" + "B) 1 - 5 years\n" + "C) 5 - 10 years\n" + "D) More than 10 years\n")
    if q5.upper() == "A":
        Score.append(0)
        break
    elif q5.upper() == "B":
        Score.append(3)
        break
    elif q5.upper() == "C":
        Score.append(7)
        break
    elif q5.upper() == "D":
        Score.append(10)
        break
    else:
        print("Invalid choice")


#Question 6
while True:
    q6 = input("6. Do you have a structured business plan\n"
               + "A) Yes\n" + "B) No\n")
    if q6.upper() == "A":
        Score.append(10)
        break
    elif q6.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")
        
        
#Question 7
while True:
    q7 = input("7. Is your business incorperated\n"
               + "A) Yes\n" + "B) No\n")
    if q7.upper() == "A":
        Score.append(5)
        break
    elif q7.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")
        

#Question 8
while True:
    q8 = input("8. Has your businesses made a net profit in the last year?\n"
               + "A) Yes\n" + "B) No\n")
    if q8.upper() == "A":
        Score.append(10)
        break
    elif q8.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")
        

#Question 9
while True:
    q9 = input("9. Does your business have a social media/online presence?\n"
               + "A) Yes\n" + "B) No\n")
    if q9.upper() == "A":
        Score.append(3)
        break
    elif q9.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")
        

#Question 10
while True:
    q10 = input("10. Does/will your business have any positive social impacts?\n" + "For example:\n"
                + "-Clean/Renewable Energy\n"	
                + "-Provides Local Employment\n"
                + "-Workforce Training\n"
                + "-Housing/Shelter\n"
                + "-Natural Disaster Relief\n"	
                + "-Public Health\n"
                + "A) Yes\n" + "B) No\n")
    if q10.upper() == "A":
        Score.append(10)
        break
    elif q10.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")


#Question 11
while True:
    q11 = input("11. Have you completed a business planning course for your business?\n"
               + "A) Yes\n" + "B) No\n")
    if q11.upper() == "A":
        Score.append(7)
        break
    elif q11.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")


#Question 12
while True:
    q12 = input("12. Have you worked individually with a business advisor or mentor for 1 or more months for this business?\n"
               + "A) Yes\n" + "B) No\n")
    if q12.upper() == "A":
        Score.append(10)
        break
    elif q12.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")


##################################################################################################################################################
#Personal finances
print("~Personal finances~\n")
print("*Enter values in USD*\n")

#Question 13
while True:      
    try:
        q13 = int(input("13. Average monthly household income over the last 6 months:\n"))
        Income = q13
        break     # exit the loop if the input is an integer
    except ValueError:         #If the input is not an integer
        print("Invalid choice - Please enter a whole number")


#Question 14
while True:      
    try:
        q14 = int(input("14. Average personal monthly payments \n(including rent/mortgages, utility bills, debts, child support/alimony) over the last 6 months:\n"))
        Payments = q14
        break     # exit the loop if the input is an integer
    except ValueError:         #If the input is not an integer
        print("Invalid choice - Please enter a whole number")

#Calculating average monthly discretionary income
#Discretionary income is the money available to invest, save, or spend, after taxes and necessities are paid.
Dis_income = Income - Payments
if Dis_income < 75:
    Score.append(0)
elif 75 <= Dis_income < 120:
    Score.append(3)
elif 120 <= Dis_income < 180:
    Score.append(5)
elif 180 <= Dis_income < 300:
    Score.append(7)
else:
    Score.append(10)


#Question 15
while True:      
    try:
        q15 = int(input("15. Average balance in your savings accounts over the last 3 months\n"))
        Savings = q15
        break     # exit the loop if the input is an integer
    except ValueError:         #If the input is not an integer
        print("Invalid choice - Please enter a whole number")

if Savings < 1000:
    Score.append(0)
elif 1000 <= Savings < 3000:
    Score.append(2)
elif 3000 <= Savings < 5000:
    Score.append(4)
elif 5000 <= Savings < 10000:
    Score.append(6)
elif 10000 <= Savings < 20000:
    Score.append(8)
else:
    Score.append(10)
    
    
#Question 16
while True:
    q16 = input("16. Do you have unpaid personal bills, including collections items, that are more than 90 days past due \n(e.g. utility bills, medical bills, loan payments, rent, etc.)?\n"
               + "A) Yes\n" + "B) No\n")
    if q16.upper() == "A":
        Score.append(0)
        break
    elif q16.upper() == "B":
        Score.append(10)
        break
    else:
        print("Invalid choice")
    
    
#Question 17
while True:
    q17 = input("17. Have you ever filed for bankruptcy?\n"
               + "A) Yes\n" + "B) No\n")
    if q17.upper() == "A":
        Score.append(0)
        break
    elif q17.upper() == "B":
        Score.append(10)
        break
    else:
        print("Invalid choice")
    

##################################################################################################################################################
#Business finances
print("~Business finances~\n")
print("*Enter values in USD*\n")

#Question 18
while True:
    q18 = input("18. Does your business have a bank account separate from your personal bank account?\n"
               + "A) Yes\n" + "B) No\n")
    if q18.upper() == "A":
        Score.append(10)
        break
    elif q18.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")


#Question 19
while True:
    q19 = input("19. Do you have an emergency fund for your business in case of an emergency?\n"
               + "A) Yes\n" + "B) No\n")
    if q19.upper() == "A":
        Score.append(10)
        break
    elif q19.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")


#Question 20
while True:
    q20 = input("20. Is your business currently earning revenue (or was earning revenue before COVID-19)?\n"
               + "A) Yes\n" + "B) No\n")
    if q20.upper() == "A":
        Score.append(10)
        break
    elif q20.upper() == "B":
        Score.append(0)
        break
    else:
        print("Invalid choice")


#Question 21
while True:      
    try:
        q21 = int(input("21. Average monthly business revenue over the last 12 months?\n"))
        Revenue = q21
        break     # exit the loop if the input is an integer
    except ValueError:         #If the input is not an integer
        print("Invalid choice - Please enter a whole number")



#Question 22
while True:      
    try:
        q22 = int(input("22. Average monthly business costs over the last 12 months \n(including rent/mortgages, utility bills, debts, employee salaries):\n"))
        Costs = q22
        break     # exit the loop if the input is an integer
    except ValueError:         #If the input is not an integer
        print("Invalid choice - Please enter a whole number")

#Calculating average monthly profit
Profit = Revenue - Costs
if Profit < 100:
    Score.append(0)
elif 100 <= Profit < 1000:
    Score.append(2)
elif 1000 <= Profit < 3000:
    Score.append(4)
elif 3000 <= Profit < 5000:
    Score.append(5)
elif 5000 <= Profit < 10000:
    Score.append(6)
elif 10000 <= Profit < 20000:
    Score.append(7)
elif 20000 <= Profit < 50000:
    Score.append(9)
else:
    Score.append(10)


##################################################################################################################################################
#Score
print("Thank you for completing the questionair!\n")

print("~Results~\n")

Total = sum(Score)    #Total score

if  Total < 57:
    print("Unfortunately, you are not eligable for a loan.")
    raise SystemExit(0)
elif 57 <= Total < 63:
    Max = 1000
elif 63 <= Total < 69:
    Max = 2000
elif 69 <= Total < 75:
    Max = 3000
elif 75 <= Total < 81:
    Max = 4000
elif 81 <= Total < 87:
    Max = 5000
elif 87 <= Total < 93:
    Max = 6000
elif 93 <= Total < 99:
    Max = 7000
elif 99 <= Total < 105:
    Max = 8000
elif 105 <= Total < 111:
    Max = 9000
elif 111 <= Total < 117:
    Max = 10000
elif 117 <= Total < 123:
    Max = 11000 
elif 123 <= Total < 129:
    Max = 12000 
elif 129 <= Total < 135:
    Max = 13000 
elif 135 <= Total < 140:
    Max = 14000 
else:
    Max = 15000

#Max loan amount available
print("You are eligable to borrow up to", Max, "USD\n")
    

##################################################################################################################################################
#Loan repayment plans

#Plan information stored in functions
def plan_a():
  print("Plan A \n-Fixed monthly payments \n-Paid over a shorter time period \nAdvantages: \n-Faster repayment \n-Lower interest paid in total \nDisadvantages: \n-Larger monthly payments \n")

def plan_b():
  print("Plan B \n-Fixed monthly payments \n-Paid over a longer time period \nAdvantages: \n-Smaller monthly payments \nDisadvantages: \n-Slower repayment \n-Higher interest paid in total \n")

def plan_c():
  print("Plan C \n-Monthly payments of 10% - 15% of your discretionary income \n-Payments are updated every year based on your income \nAdvantages: \n-Payments adjusted for changes in income \n-Payments are capped at 15% \nDisadvantages: \n-Possibly slower repayment (if income is low relative to monthly loan payments) \n")  
 

if (Dis_income + Savings + Profit) < (Max / 2):      #Lower income
    print("You qualify for Repayment Plan B or C\n")
    plan_b()
    plan_c()
else:                                                #Higher income
    print("You qualify for Repayment Plan A or B\n")
    plan_a()
    plan_b()













    
    