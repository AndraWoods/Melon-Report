#This is assigning the variable "the_file" to open the delivery file 
#This is saying for a line in "um-deliveries-20" but we want to make this more efficient
#We want to put this code into a function
    
def melon_counting(day_number, path)
#Here we made a function named "melon_orders" and set parameters called "day_number " and "path"
#What this does is that it calls two different functions that we will loop around to near the end.
    print("Day", day_number)
    delivery_log = open(path)
#What this says is that when the program is ran that it will print the day and the number of the day 
#delivery_log becomes a variable that is binded to an open function which will open "um-deliveries-20"
    the_file = open("um-deliveries-20140519.txt")
    for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()
