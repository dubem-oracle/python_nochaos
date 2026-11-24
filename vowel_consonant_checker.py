sum = 0
for number in range (1,11):
    score = int(input("Enter a score between 0 and 100: "))
    if score < 0 or score > 100:
        print("INVALID SCORE")
        
    elif score > 0 and score < 100:
        sum += score
    

print(f"Sum: {sum}")

			
