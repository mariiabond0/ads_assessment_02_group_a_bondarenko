"""
Simple Calculator
"""
def calculate(n1:int, n2:int, operator:str) -> str:
    if n2 == 0:
        print("Division by 0 is not allowed.")
    else:
        if operator == "+":
            print(n1+n2)
        elif operator == "-":
            print(n1-n2)
        elif operator == "*":
            print(n1*n2)
        elif operator == "/":
            print(n1/n2)
        else:
            print("Invalid operator.")


calculate(3,4, "+")
calculate(2,8, "-")
calculate(5,5, "*")
calculate(10,0, "/")
calculate(3,5, "/")
calculate(9,4, "?")

"""
Reverse Word
"""
def reverse_word(word:str) -> str:
    index = len(word) - 1
    while index >= 0:
        print(word[index])
        index -= 1


reverse_word("hello")
reverse_word("WORLD")
reverse_word("lEOn")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

