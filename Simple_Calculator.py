class Calculator:

    def add(self,a,b): return a + b
    def substract(self,a,b): return a - b
    def multiply(self,a,b): return a * b
    def divide(self,a,b): return "Error! Division by Zero" if b == 0 else a / b

def main():
       calc = Calculator()

       while True:
            print("\nSimple Calculator")
            print("1. Adding")
            print("2. Substraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = input("Enter a choice(1-5):")

            if choice == "5":
                print("Exiting... The Calci")
                break

            if choice in ('1','2','3','4'):
                num1 = float(input("Enter the First Number:"))
                num2 = float(input("Enter the Second Number:"))

                operation = {
                    "1": calc.add,
                    "2": calc.substract,
                    "3": calc.multiply,
                    "4": calc.divide
                }

                result = operation[choice](num1,num2)

                print(f"Result: {result}")
            else: 
                print("Invalid Choice. Try Again")

if __name__=="__main__":
    main()