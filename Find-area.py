# Codded by: Kenil Chovatiya


choise = input("Choose shape from below to find the area and perimeter:\n"
               " c for circle \n"
               " s for Square \n"
               " r for Rectangle \n"
               " t for Triangle \n"
               )
choise = str(choise)
pie = 3.17  # declaring pi vlaue for circle

# applying condistion for circle and square 

if choise == 'c':
    radius = input("Enter radius of Circle: ")
    radius = float(radius)
    area = radius * radius * pie  # Calculating Area of Circe
    circum = int(2 * pie * radius)  # Calculating Circumference of Circle
    print("Area of Circle is : %.1f" % area)
    print("Circumference of circle is  : ", circum)


elif choise == 's':

    side = input("Enter Length of square :")
    side = float(side)
    area = side * side  # Calculating Area of Square
    perimeter = int(4 * side)  # Calculating perimeter of Square
    print("Area of Square is : %.1f" % area)
    print("Parimeter of Square is  : ", perimeter)

elif choise == 'r':
    length = input("Enter Length of Rectangle : ")
    width = input("Enter width of Rectangle : ")
    length = float(length) # Calculating Area of Rectangle
    width = float(width)   # Calculating Perimeter of a Rectangle
    area = length * width
    perimeter = 2 * (length + width)
    print("Area of Rectangle is : %.1f" % area)
    print("Perimeter of Rectangle is  : ", perimeter)

elif choise == 't':
    base = input("Enter base of Triangle : ")
    side1 = input("Enter side 1 of Triangle : ")
    side2 = input("Enter side 2 of Triangle : ")
    height = input("Enter height of Triangle : ")
    base = float(base)
    side1 = float(side1)
    side2 = float(side2)
    height = float(height)
    area = (height * base) / 2          # Calculating Area of Triangle
    perimeter = side1 + side2 + base    # Calculating Perimeter of a Triangle
    print("Area of Triangle is : %.1f" % area)
    print("Perimeter of Triangle is  : ", perimeter)


else:
    print("Wrong choice of input please select from given.")
