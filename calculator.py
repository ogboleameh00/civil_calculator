# My Civil Calculator - Blocks and Cement

length = float(input("Enter wall length in metres: "))
height = float(input("Enter wall height in metres: "))

wall_area = length * height
blocks = wall_area * 12.5
cement_bags = blocks / 60

print("Wall Area:", wall_area, "sqm")
print("Blocks needed:", int(blocks))
print("Cement bags needed:", round(cement_bags, 1))
