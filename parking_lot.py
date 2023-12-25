#TO CALCULATE PARKING CHARGES OF A VEHICLE, ENTER THE TYPE OF VEHICLE AS A CHARACTER
#(C FOR CAR, B FOR BUS ETC) AND NO OF HOURS THEN CALCULATE CHARGES AS GIVEN BELOW
#TRUCK/BUS= 20RS PER HOUR
#CAR 10 10 RS PER HOUR
#SCOOTER,CYCLE, BIKE= 5 rs per hour
#modify the above program

# print("------------------------------------ PARKING LOT ----------------------------------")
# print("                 ----------------------------------------------")
# print("                                    PRICE PER HOUR             ")
# print("                 |Truck/Bus                |            Rs.20 |")
# print("                 |Car                      |            Rs.10 |")
# print("                 |Scooter/Cycle/Bike       |            Rs.05 |")

# vehicletype = {'SCOOTER': 2, 'CYCLE': 2, 'BIKE': 2, 'CAR': 4, 'TRUCK': 8, 'BUS': 8}

# vehicle_type = input("Enter Vehicle type: ").upper()
# intime = float(input(" Enter the enter time in 12 hour format: "))#*60)
# inampm=input("Enter AM or PM: ").upper()
# outtime=float(input(" Enter the out time in 12 hour format: "))
# outampm=input("Enter AM or PM: ").upper()
# #time=(outtime-intime)*60
# if intime=='PM':
#     ttime=(12-intime)*60
# else:
#     ttime=outtime*60
# if outtime=='PM':
#     tiime=(outtime)*60
# else:
#     tiime=(12-intime)*60
# #ampm=input("Enter AM or PM: ").upper()
# time=
# if vehicle_type in vehicletype:
#     print("Vehicle type: ", vehicle_type)
#     if vehicletype[vehicle_type] == 2:
#         #print("The cost you have to pay is: ", (5/60) * time)
#         if ampm=='AM':
#             cost=(5/60) * time
#         else:
#             cost=(5/60) * time*2
#     elif vehicletype[vehicle_type] == 4:
#         #print("The cost you have to pay is: ", (1/6) * time)
#         if ampm=='AM':
#             cost=(1/6) * time
#         else:
#             cost=(1/6) * time*2
#     else:
#         #print("The cost you have to pay is: ", (1/3) * time)
#         if ampm=='AM':
#             cost=(1/3) * time
#         else:
#             cost=(1/3) * time*2
# else:
#     print("Invalid vehicle type.")
    
# print("--------------------------------------")
# print("|            RECIEPT                 |")
# print("|Vehicle Type:       ",vehicle_type)
# print("|No of ours :        ",time,ampm)
# print("|In Time:            ",intime)
# print("|Out Time:           ",outtime)
# print("Total Cost:          ",cost)

#--------------------------------------------------------------------------------------------------------



print("------------------------------------ PARKING LOT ----------------------------------")
print("                 ----------------------------------------------")
print("                                    PRICE PER HOUR             ")
print("                 |Truck/Bus                |            Rs.20 |")
print("                 |Car                      |            Rs.10 |")
print("                 |Scooter/Cycle/Bike       |            Rs.05 |")

vehicletype = {'SCOOTER': 2, 'CYCLE': 2, 'BIKE': 2, 'CAR': 4, 'TRUCK': 8, 'BUS': 8}

vehicle_type = input("Enter Vehicle type: ").upper()
intime = float(input(" Enter the enter time in 12 hour format: "))#*60)
inampm=input("Enter AM or PM: ").upper()
outtime=float(input(" Enter the out time in 12 hour format: "))
outampm=input("Enter AM or PM: ").upper()
#time=(outtime-intime)*60
if intime=='PM':
    ttime=12-intime*60
else:
    ttime=intime
if outtime=='PM':
    tiime=(outtime)*60
else:
    tiime=(intime)*60
#ampm=input("Enter AM or PM: ").upper()
time=ttime+tiime
if vehicle_type in vehicletype:
    print("Vehicle type: ", vehicle_type)
    if vehicletype[vehicle_type] == 2:
        #print("The cost you have to pay is: ", (5/60) * time)
            cost=(5/60) * time
        
    elif vehicletype[vehicle_type] == 4:
        #print("The cost you have to pay is: ", (1/6) * time)
       
            cost=(1/6) * time
    else:
        #print("The cost you have to pay is: ", (1/3) * time)
        
            cost=(1/3) * time
        
else:
    print("Invalid vehicle type.")
    
print("--------------------------------------")
print("|            RECIEPT                 |")
print("|Vehicle Type:       ",vehicle_type)
print("|No of hours :        ",time/60)
print("|In Time:            ",intime," ",inampm)
print("|Out Time:           ",outtime," ",outampm)
print("Total Cost:          ",cost)