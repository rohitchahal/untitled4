from car import Car

def main():
 limo = Car(137)
 limo.drive(115)
 limo.add_fuel(20)
 print("fuel =", limo.fuel)
 print("odometer =", limo.odometer)
 print(limo)

main()