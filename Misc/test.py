import cars


print("Loading cars in a list ...")
car_list = cars.load_car_list("car_data")
print("Number of cars loaded:", len(car_list))

print()
print("Loading cars in a dictionary ...")
car_dict = cars.load_car_dict("car_data")
print("Number of cars loaded:", len(car_dict.keys()))

print()
print("Cars with make Cadillac in the list:")
list1 = cars.cars_with_make(car_list, "Cadillac")
for car in list1:
    print(car)

print()
print("Cars with make color Green:")
list1 = cars.cars_with_color(car_list, "Green")
for car in list1:
    print(car)

print()
print("Sorting the car list by year ...")
cars.sort_by_year(car_list)
print("The first 10 cars are:")
for i in range(10):
    print(car_list[i])

print()
id = "373071578"
print("Removing the car with id " + id + " from the dictionary ...")
cars.remove_car(car_dict, id)

print()
print("Number of cars for each make: ")
cars.print_make_count(car_list)

print()
output_name = "car_data1"
print("Writing the dictionary to the file " + output_name)
cars.write_to_file(car_dict, output_name)
