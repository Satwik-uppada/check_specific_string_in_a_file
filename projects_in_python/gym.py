print("Track Your Progress:")
type_ = {}


def wgt_lift(name, weight, sets):
    type_[name] = {}
    type_[name]["weight"] = weight
    type_[name]["sets"] = sets


num = eval(input("Enter the number of exercises:"))
for i in range(0, num):
    print(f"Enter the name of the exercise {i+1}:")
    name= input()
    print(f"Enter the value of weight you lifted with {name}(in kgs) :")
    weight_=eval(input())
    print(f"Enter the number of sets of {name}:")
    sets_=eval(input())
    wgt_lift(name,weight_,sets_)