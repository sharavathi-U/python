# Menu Driven Program for Multiple Numbers
while True:
    print("\n--- MENU ---")
    print("1. Check Even or Odd (Multiple Numbers)")
    print("2. Check Prime or Not (Multiple Numbers)")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        numbers = list((int, input("Enter numbers separated by space: ").split()))
        
        for num in numbers:
            if num % 2 == 0:
                print(num, "is Even")
            else:
                print(num, "is Odd")

    elif choice == "2":
        numbers = list((int, input("Enter numbers separated by underscore: ").split('')))
        
        for num in numbers:
            if num <= 1:
                print(num, "is Not Prime")
            else:
                is_prime = True
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
                
                if is_prime:
                    print(num, "is Prime")
                else:
                    print(num, "is Not Prime")

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid choice. Please try again.")