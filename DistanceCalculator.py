#jeepney simulator

#added git

#distance from start to end
point_a = 0
point_b = 3
point_c = 5
point_d = 8
point_e = 11

#conditions
additional_charges = 0
minimum_fare = 8
total_fare = minimum_fare
a_student = True

#a function that calculates amount of km
def distance_calculator ( where_from, where_to):
    return (where_to - where_from)

print("------------------------------")

amount_of_km = distance_calculator(point_a, point_e)

if a_student == True:
    #this is for discounted people
    if  amount_of_km > 5:
        print("amount of km: " + str(amount_of_km))
        additional_charges = (int(amount_of_km-5)) * 0.70
else:
    #this is for regular rates
    if  amount_of_km > 5:
        print("amount of km: " + str(amount_of_km))
        additional_charges = (int(amount_of_km-5)) * 0.90
    

print("additional Charges: " + str(additional_charges))
print("Minimum Fare " + str(minimum_fare))
print("Student, PWD, Senior Citezen:" + str(a_student))

print("------------------------------")
#sums up total amount
total_fare += additional_charges
print("total payment: Php." +  str(total_fare))



