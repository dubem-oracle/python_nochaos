text = input("Enter a string: ");
reversed = ""

for letter in range(len(text) -1, -1, -1):
    reversed += text

if text == reversed:
print("This is a Palindrome.");

    else:
    print("This is not a Palindrome.");
    

    
    

