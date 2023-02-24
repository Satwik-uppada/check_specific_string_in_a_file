# Data will be input by the user
name=input("Enter the Name: \n")                   # user name(by default python consider input as string so we no need to give data type specially)

age=int(input("Enter age(1-8 years): \n"))                    # user age(by default python consider input as string .but age must in integer so that we need to give int() method
                                                   # while inputing the data so that compiler take it as int value)

gender=input("Enter Gender(Male/Female): \n")                   # user gender(by default python consider input as string so we no need to give data type specially)

height=float(input("Enter Height(in inches): \n")) # user height(by default python consider input as string .but height must in float so that we need to give float() method
                                                   # while inputing the data so that compiler take it as float value;because height in inches might be in decimal points as well)

weight=float(input("Enter Weight(in pounds): \n")) # user weight(by default python consider input as string .but weight must in float so that we need to give float() method
                                                   # while inputing the data so that compiler take it as float value;because weight in pound might be in decimal points as well)
def cal():
 print("1.calorie requirement calculater")
 print("2.BMI Calculater")
 option=int(input("Select your requirement option: "))
 return option

calc_option=cal()
if calc_option==1:
 # Taking input from user
 if age>0 and age<=8:
  milk=float(input("Enter how much quantity of milk will child take daily(in grams): \n"))             # Taking user's milk quantity intake in a day
  egg=float(input("Enter how much quantity of egg will child take daily(in grams): \n"))               # Taking user's egg quantity intake in a day
  rice=float(input("Enter how much quantity of rice will child take daily(in grams): \n"))             # Taking user's rice quantity intake in a day
  lentils=float(input("Enter how much quantity of lentils will child take daily(in grams): \n"))       # Taking user's ventils quantity intake in a day
  vegetables=float(input("Enter how much quantity of vegetables will child take daily(in grams): \n")) # Taking user's vegetables quantity intake in a day
  meat=float(input("Enter how much quantity of meat will child take daily(in grams): \n"))             # Taking user's meat quantity intake in a day


  if milk>0:
    print("Calorie consumption of milk is 100 cal/100 g\n")                                 # Displaying milk calories per 100 gm
    milk_cal=(milk*100)/100
    print("Daily calories on consumption of milk is {} calories \n".format(milk_cal))       # Displaying user's daily calories intake on milk

  else:
    print("{} must drink milk daily\n".format(name))                                        # Displaying the statement of user state

  if egg>0:
    print("Calorie consumption of egg is 155 cal/100 g\n")                                  # Displaying the egg calories per 100 gm
    egg_cal=(egg*155)/100
    print("Daily calories on consumption of egg is {} calories\n ".format(egg_cal))         # Displaying user's daily calories intake on egg

  else:
    print("{} must eat egg daily\n".format(name))                                           # If egg intake is less it will display this message

  if rice>0:
    print("Calorie consumption of rice is 130 cal/100 g\n")                                 # Displaying the rice calories per 100 gm
    rice_cal=(rice*130)/100
    print("Daily calories on consumption of rice is {} calories \n".format(rice_cal))       # Displaying user's daily calories intake on rice

  else:
    print("{} must eat rice daily\n".format(name))                                          # If rice intake is less it will display this message

  if lentils>0:
    print("Calorie consumption of lentils is 113 cal/100g \n")                              # Displaying the lentils calories per 100 gm
    lentils_cal=(lentils*113)/100
    print("Daily calories on consumption of lentils is {} calories \n".format(lentils_cal)) # Displaying user's daily calories intake on lentils

  else:
    print("{} must eat lentils daily\n".format(name))                                       # If lentils intake is less it will display this message

  if vegetables>0:
    print("Calorie consumption of vegetables is 85 cal/100g\n")                             # Displaying the vegetables calories per 100 gm
    veg_cal=(vegetables*85)/100
    print("Daily calories on consumption of vegetables is {} calories\n ".format(veg_cal))  # Displaying user's daily calories intake on vegetables

  else:
    print("{} must eat vegetables daily \n".format(name))                                   # If vegetables intake is less it will display this message

  if meat>0:
    print("Calorie consumption of  meat is 143 cal/100g \n")                                # Displaying the meat calories per 100 gm
    meat_cal=(meat*143)/100
    print("Daily calories on consumption of meat is {} calories\n".format(meat_cal))        # Displaying user's daily calories intake on meat

  else:
    print("{} must eat meat daily \n".format(name))                                         # If meat intake is less it will display this message

  daily_cal=milk_cal+egg_cal+rice_cal+lentils_cal+veg_cal+meat_cal                            # calculating total calories consumption of the user as per their intake


  if age>0 and age<=2:                                                                                        # if age is >0 and <=2 then this loop executes
    print("Minimum calories required to this age group(>0-2 years) children's are 800 calories per day.")               # Displaying minimum calories required per day for (0-2) age group
    print("Daily calories on food consumptions of your child({}) is {} calories\n".format(name,daily_cal))  # Displaying total calorie consumption per day of the user

    if daily_cal<800:                                                                                       # if total calories per day is <800 then this loop will execute
        required_cal=800-daily_cal                                                                          # if total calories < 800 so that user require some more calories for balanced diet .
                                                                                                            # here,we are calculating that required amount of calories
        print("Your child({}) need to consume more calories according to age group.".format(name))          # if total<800 then it prints this statement
        print("{} need to consume {} more calories per day\n".format(name,required_cal))                    # Displaying how many more no.of calories required to get balanced diet
    elif daily_cal==800:                                                                                    # if total calories per day is ==800 then this loop will is executes
        print("Your child ({}) reached minimum amount of calorie consumption per day ".format(name))        # Displaying state of calorie intake per day
        print("Congrats's...! Maintain this :)\n")
    else:                                                                                                   # if total calories per day is >800 then this loop will execute
        excess_cal=daily_cal-800                                                                            # if total calories > 800 so that user look after their diet and reduce calories for balanced diet .
                                                                                                            # here,we are calculating that excess amount of calories
        print("Your child({}) need to consume less calories according to age group.".format(name))          # if total>800 then it prints this statement
        print("It may leads to increase body weight. Please maintain balanced diet.")
        print("{} need to reduce {} calories per day\n".format(name,excess_cal))                            # Displaying how many calories need to reduce in intake for balanced diet

  elif age>2 and age<=4:                                                                                      # if age is >2 and <=4 then this loop executes
    print("Minimum calories required to this age group(>2-4 years) children's are 1400 calories per day")               # Displaying minimum calories required per day for (>2-4) age group
    print("Daily calories on food consumptions of your child({}) is {} calories\n".format(name,daily_cal))  # Displaying total calorie consumption per day of the user

    if daily_cal<1400:                                                                                      # if total calories is <1400 then this loop is will execute
        required_cal=1400-daily_cal                                                                         # if total calories < 1400 so that user require some more calories for balanced diet .
                                                                                                            # here,we are calculating that required amount of calories
        print("Your child({}) need to consume more calories according to age group.".format(name))          # if total<1400 then it prints this statement
        print("{} need to consume {} more calories per day\n".format(name,required_cal))                    # Displaying how many more no.of calories required to get balanced diet
    elif daily_cal==1400:                                                                                   # if total calories per day is ==1400 then this loop will execute
        print("Your child ({}) reached minimum amount of calorie consumption per day ")                     # Displaying state of calorie intake per day
        print("Congrats's...! Maintain this :) \n")
    else:                                                                                                   # if total calories is >1400 so then this loop will execute
        excess_cal=daily_cal-1400                                                                           # if total calories > 1400 so that user look after their diet and reduce calories for balanced diet .
                                                                                                            # here,we are calculating that excess amount of calories
        print("Your child({}) need to consume less calories according to age group.".format(name))          # if total>1400 then it prints this statement
        print("It may leads to increase body weight. Please maintain balanced diet.")
        print("{} need to reduce {} calories per day\n".format(name,excess_cal))                            # Displaying how many calories need to reduce in intake for balanced diet


  elif age>4 and age<=8:
    print("Minimum calories required to this age group(>4-8 years) children's are 1800 calories per day")               # Displaying minimum calories required per day for (>4-8) age group
    print("Daily calories on food consumptions of your child({}) is {}".format(name,daily_cal))             # Displaying total calorie consumption per day of the user

    if daily_cal<1800:                                                                                      # if total calories is <1800 then this loop is will execute
        required_cal=1800-daily_cal                                                                         # if total calories < 1800 so that user require some more calories for balanced diet .
                                                                                                            # here,we are calculating that required amount of calories
        print("Your child({}) need to consume more calories according to age group.".format(name))          # if total<1800 then it prints this statement
        print("{} need to consume {} more calories per day".format(name,required_cal))                      # Displaying how many more no.of calories required to get balanced diet
    elif daily_cal==1800:                                                                                   # if total calories per day is ==1800 then this loop will execute
        print("Your child ({}) reached minimum amount of calorie consumption per day ".format(name))        # Displaying state of calorie intake per day
        print("Congrats's...! Maintain this :)")
    else:
        excess_cal=daily_cal-1800                                                                           # if total calories > 1800 so that user look after their diet and reduce calories for balanced diet .
                                                                                                            # here,we are calculating that excess amount of calories
        print("Your child({}) need to consume less calories according to age group.\n".format(name))        # if total>1800 then it prints this statement
        print("It may leads to increase body weight. Please maintain balanced diet.\n")
        print("{} need to  reduce {} calories per day in food intake\n".format(name,excess_cal))            # Displaying how many calories need to reduce in intake for balanced diet

elif calc_option==2:
 BMI = weight / (height ** 2) * 703                                                                         # Formula for BMI
 print("BMI is : %0.2f "%BMI)                                                                               # Printing BMI value having only 2 decimal points

 if BMI<16:                                                                                                 # if BMI is <16 this loop will execute
    print("It's difficult to say that '{}' is severely Underweight.\n".format(name))                        # Displaying BMI state of user with their names
 elif BMI>=16 and BMI<18.5:                                                                                 # if BMI is >=16 and <18.5 this loop will execute
    print("It's difficult to say that '{}' is underweight\n".format(name))                                  # Displaying BMI state of user with their names
 elif BMI>=18.5 and BMI<25:                                                                                 # if BMI is >=18.5 and <25 this loop will execute
    print("Congrats.. !,{} is healthy\n".format(name))                                                      # Displaying BMI state of user with their names
 elif BMI>=25 and BMI<30:                                                                                   # if BMI is >=25 and <30 this loop will execute
    print("It's difficult to say that '{}' is overweight\n".format(name))                                   # Displaying BMI state of user with their names
 elif BMI>=30:                                                                                              # if BMI is >=30 this loop will execute
    print("It's difficult to say that '{}' is obese\n".format(name))                                        # Displaying BMI state of user with their names

 else:
    print("Sorry..! This calculater is used to calculate calorie count of children's upto 8 years only.\n") # if age is above 8 or below or equal to 0  then this statement prints

else:
   print("please,Select correct option as per context..")