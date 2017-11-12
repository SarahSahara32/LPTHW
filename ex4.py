# cars equals 100
cars = 100
#4 seats in a car
space_in_a_car = 4.0
#drivers equals 30
drivers = 30
#passengers equals 90
passengers = 90
#cars_not_driven equals cars minus drivers
cars_not_driven = cars - drivers
#cars_driven equals drivers
cars_driven = drivers
#carpool_capacity equals cars_driven multiploed with space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car equals passengers devided by cars_not_driven
average_passengers_per_car = passengers / cars_not_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
