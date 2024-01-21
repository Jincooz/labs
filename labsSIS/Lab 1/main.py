
import random

class Calculator:
    
    def generate_big_number(self, min_value = 10**49, max_value = 10**50):
        return random.randint(min_value,max_value)

    def sum(self, first, second):
        return first + second
    
    def mul(self, first,second):
        return first * second
    
    def mod(self, divisible, divider):
        return divisible % divider
    
    def pow(self, first,second):
        return first ** second

def main():
    run = True
    calculator = Calculator()
    while(run):
        print('\n1. sum\n2. multiply\n3. power\n4. take mod\n5. exit\nNumber: ', end = "")
        menu_pick = int(input())
        if menu_pick == 1:
            print("First number(g for generating long number): ", end = "")
            result = input()
            if (result == 'g'):
                first_num = calculator.generate_big_number()
            else:
                first_num = int(result)
            print("Second number(g for generating long number): ", end = "")
            result = input()
            if (result == 'g'):
                second_num = calculator.generate_big_number()
            else:
                second_num = int(result)
            print(f"{first_num} + {second_num} = ", calculator.sum(first_num,second_num))
        elif menu_pick == 2:
            print("First number(g for generating long number): ", end = "")
            result = input()
            if (result == 'g'):
                first_num = calculator.generate_big_number()
            else:
                first_num = int(result)
            print("Second number(g for generating long number): ", end = "")
            result = input()
            if (result == 'g'):
                second_num = calculator.generate_big_number()
            else:
                second_num = int(result)
            print(f"{first_num} * {second_num} = ", calculator.mul(first_num,second_num))
        elif menu_pick == 3:
            print("First number(g for generating long number): ", end = "")
            result = input()
            if (result == 'g'):
                first_num = calculator.generate_big_number()
            else:
                first_num = int(result)
            print("Second number(g for generating long number): ", end = "")
            result = input()
            if (result == 'g'):
                second_num = calculator.generate_big_number()
            else:
                second_num = int(result)
            print(f"{first_num} ^ {second_num} = ", calculator.pow(first_num,second_num))
        elif menu_pick == 4:
            print("")
            print("Divisible(g for generating long number): ", end = "")
            result = input()
            if (result == 'g'):
                divisible = calculator.generate_big_number()
            else:
                divisible = int(result)
            print("Divider(g for generating long number): ", end = "")
            result = input()
            if (result == 'g'):
                divider = calculator.generate_big_number()
            else:
                divider = int(result)
            print(f"{divisible} mod {divider} = ", calculator.mod(divisible,divider))
        elif menu_pick == 5:
            run = False
        input()

if (__name__ == "__main__"):
    main()