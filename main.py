print("Hello! My name is Observer. Let me check your information!")
name=input("What's your name? ") # Ask name
print("")
print("Hi! ", name, ", Nice to meet you!") # Reply
print("")
birth=input("What is your birthday? ") # Ask birthday
print("")
print("Yeah, your bithday is", birth, "!") # Reply

print("")
quest=input("Can I ask your phone number? (yes or no) ") # Have a question
if quest=="yes": # If yes, ask the phone number
    flag=True
    print("")
    phone=input("Okay, what's your phone number? ") # Ask phone number
    print("")
    print("Now I know your name is", name, ", your birthday is", birth, ", and your phone number is", phone, "!") # Say the name, birthday and phone number
    print("Have a good day! Good bye!") # Say good bye
    print("")
    stop=input("Please type any key and enter it to close this program... ")
    while True:    
     if stop=="stop":
        break
     else:
        break
    
else: # If no, not ask the phone number
    print("")
    print("Uh... That's okay. Now I know your name is", name, ", and your birthday is", birth, ".") # Say the name and birthday
    print("Have a good day! Good bye!") # Say good bye
    stop=input("Please type any key and enter it to close this program... ")
    while True:    
     if stop=="stop":
        break
     else:
        break
    
