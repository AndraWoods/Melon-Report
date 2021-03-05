#This is assigning the variable "the_file" to open the delivery file 
#This is saying for a line in "um-deliveries-20" but we want to make this more efficient
#We want to put this code into a function
    
def melon_counting(day_number, path):
#Here we made a function named "melon_orders" and set parameters called "day_number " and "path"
#What this does is that it calls two different functions that we will loop around to near the end.
    print("Day", day_number)
    delivery_log = open(path)
#What this says is that when the program is ran, it will print the day and the number of the day 
#delivery_log becomes a variable that is binded to an open function which will open "um-deliveries-20"
    for line in delivery_log:
#So this is saying for each line in delivery_log which is the um-deliveries-20 file
        line = line.rstrip()
        words = line.split('|')
#What .rstrip() is saying is that for each line to delete any characters at the end of a string 
#What .split is saying to split a string into a list separated by "|" 
#This is will make each word separated by "|". 

        melon = words[0]
        count = words[1]
        amount = words[2]
#So what the original problem was that printing the melon name over and over
#So what we just changed is so the program will print the count then the melon name then the total amount sold

        print(f"Delivered {count} {melon}s for total of ${amount}")
#Changed the format to an f.string so it would look cleaner
    delivery_log.close()
melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")
#So we did delivery_log.close to close the file once it printed the amount
#We put the melon_count in the outer scope to define the parameters in the function
#So bascially we were like "rememeber when we put day_number and path above?.. Yeah these are the actual values we are inserting into them"
#And we delete the rest! 

