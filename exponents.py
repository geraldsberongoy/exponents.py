# # Exercise 15: Write a function called exponent(base, exp) 
# that returns an int value of base raises to the power of exp.

# Expected output

# Case 1:
# base = 2
# exponent = 5
# 2 raises to the power of 5: 32 
# i.e. (2 *2 * 2 *2 *2 = 32)

# Case 2:
# base = 5
# exponent = 4
# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)

# Def
def exponent(base, exp):
    result = base**exp
    long_form = "*".join(str(base) for _ in range(exp))
    print(f"{base} raises to the power of {exp} is: {result}")
    print(f"i.e. ({long_form} = {result})", "\n")

# Case 1
print("Base = 2")
print("Exponent = 5")
exponent(2, 5)

# Case 2
print("Base = 5")
print("Exponent = 4")
exponent(5, 4)

# User Input
base = int(input("Input a base: "))
exp = int(input("Input a exponent: "))
exponent(base, exp)