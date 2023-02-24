course=input("Give the course name: ")
homework=float(input("Enter the home work marks(/25 marks): "))
exams=float(input("Enter the marks of exams(/50 marks): "))
projects=float(input("Enter marks in projects(/25 marks): "))

total_marks=homework+exams+projects
percentage=(total_marks/100)*100

if percentage>=95:
   print("Grade O in ",course)
elif percentage>=90 and percentage<95:
    print("Grade A+ in ",course)
elif percentage>=80 and percentage<90:
    print("Grade A in ",course)
elif percentage >= 70 and percentage < 80:
    print("Grade B+ ",course)
elif percentage>=60 and percentage<70:
    print("Grade B in ",course)
elif percentage>=50 and percentage<60:
    print("Grade C in ",course)
elif percentage>=40 and percentage<50:
    print("Grade D in ",course)
else:
    print("Grade F in ",course)


