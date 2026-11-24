

sum = 0
count = 0

while True:
    number = int(input("Enter a number (-1 to stop):  "))
    if number == -1:
        break

    if number >= 0:
        sum += number
    count++
    
    
    average = sum / count
    
    print("Average: " + average)
    

    

