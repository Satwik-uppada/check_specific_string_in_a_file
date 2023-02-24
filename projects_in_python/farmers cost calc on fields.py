
def field_size():
 print("Types of field measurements:")
 print("1.Square meters")
 print("2.Acres")
 option=int(input("choose any one of the option: "))
 return option
def details_acre():
    cost_of_seeds = float(input("Enter the cost of seeds per acre: "))
    cost_of_fertilizers = float(input("Enter the cost of fertilizers per acre: "))
    cost_of_labour = float(input("Enter the cost of labour per acre: "))

    return cost_of_seeds,cost_of_fertilizers,cost_of_labour

def details_sqm():
    cost_of_seeds = float(input("Enter the cost of seeds per square metre: "))
    cost_of_fertilizers = float(input("Enter the cost of fertilizers per square metre: "))
    cost_of_labour = float(input("Enter the cost of labour per square metre: "))

    return cost_of_seeds,cost_of_fertilizers,cost_of_labour
selected_measurement=field_size()
if selected_measurement==1:
    square_meters=float(input("Enter the size of field in square meters: "))
    acres=square_meters*0.000247105
    seeds,fertilizers,labour=details_sqm()
    cost_of_planting=(seeds+fertilizers+labour)*acres
    print("Total cost of planting is: ",cost_of_planting)
elif selected_measurement==2:
    acres=float(input("Enter the size of field in acres: "))
    seeds, fertilizers, labour = details_acre()
    cost_of_planting = (seeds + fertilizers + labour) * acres
    print("Total cost of planting is: ", cost_of_planting)
else:
    print("Choose right option to perform calculation")






