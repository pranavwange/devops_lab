def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time))

def main():
    while True:
        print("\nInterest Calculator:")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Exit")
        choice = int(input("Enter choice (1/2/3): "))

        if choice == 1:
            principal = float(input("Enter Principal amount: "))
            rate = float(input("Enter rate of interest: "))
            time = float(input("Enter time (in years): "))
            simple_interest = calculate_simple_interest(principal, rate, time)
            print("Simple Interest:", simple_interest)

        elif choice == 2:
            principal = float(input("Enter Principal amount: "))
            rate = float(input("Enter rate of interest: "))
            time = float(input("Enter time (in years): "))
            compound_interest = calculate_compound_interest(principal, rate, time)
            print("Compound Interest:", compound_interest)

        elif choice == 3:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
