var = int(input("Which table number do you want?: "))

"""
print(f"|1 x {var} = {var*1}|")
print(f"|2 x {var} = {var*2}|")
print(f"|3 x {var} = {var*3}|")
print(f"|4 x {var} = {var*4}|")
print(f"|5 x {var} = {var*5}|")
print(f"|6 x {var} = {var*6}|")
print(f"|7 x {var} = {var*7}|")
print(f"|8 x {var} = {var*8}|")
print(f"|9 x {var} = {var*9}|")
print(f"|10 x{var} = {var*10}|")

Dont this away!!
"""

for i in range(1, 11):
    print(f"{i} x {var} = {i*var}")
# Do this away!!