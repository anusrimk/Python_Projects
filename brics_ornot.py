#WAP if the entered country belongs to bricks or not
brics=["BRAZIL","RUSSIA","INDIA","CHINA","SOUTH AFRICA"]
country=str(input("Enter a country: "))
if country.upper() in brics:
    print("Yes!", country, " is a member of BRICS")
else:
    print("No! you dont have IQ")