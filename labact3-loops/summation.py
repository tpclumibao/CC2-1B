n = int(input("Enter a number: "))
sum_of_numbers = 0
formula = ""
for i in range(1, n + 1):
    sum_of_numbers += i
    formula += str(i)
    if i < n:
        formula += "+"
print("Formula:", formula)
print("Result:", sum_of_numbers)
