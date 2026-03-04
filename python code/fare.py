gross_fare = float(input("Gross Fare:"))
base_fare = float(input("Base Fare:"))
iata_com = float(input("IATA Commission:"))


AIT = (gross_fare*0.3)/100
IATA_Commission = (base_fare*iata_com)/100

net_fare = gross_fare+AIT-IATA_Commission


print("AIT:", AIT)
print("IATA Commission:", IATA_Commission)
print("Net Fare:", net_fare)

input("Press Enter to exit...")

