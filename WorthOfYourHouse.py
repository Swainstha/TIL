
def find_your_price():
    file = open('house-prices.csv','r')
    #file = open('test.csv','r')
    csv = file.read()
    csv_str = str(csv)
    lines = str.splitlines(csv_str)
    area_square_total = 0
    price_area_total = 0
    house_price_total = 0
    area_total = 0
    n = len(lines)
    for line in lines:
        price_area = line.split(',')
       # print(price_area[0] + " " +  price_area[1])
        house_price =int( price_area[0])
        area = int(price_area[1])
        house_price_total += house_price
        area_total += area
        area_square_total += (area * area)
        price_area_total += (house_price * area)
    global a,b
    a = ((house_price_total)*(area_square_total) - (area_total)*(price_area_total))/(n * area_square_total - (area_total**2))
    b = (n * price_area_total - area_total * house_price_total)/ (n * area_square_total - (area_total**2))
    print("a = ",a,"b = ",b)
find_your_price()
area = input("Enter the area of your house in square feet")
print(a,b)
price = a + b * int(area)
print("The price of your house is ", price)
        




