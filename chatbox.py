print("Hello, I am an AI chatbox, ready for service!")

def generalQuest():
    print("Okay hello! My name is PookieGPT.")
    print("I was written in Python to make you feel at home.")
    
    health = input("How is your day?\n 1. It's good\n 2. Fine I guess\n 3. Not really good lmao\n")
    
    if health == "1":
        print("Yay! I'm happy you're doing well.")
    elif health == "2":
        print("Hmm, neutral vibe... wanna talk more?")
    elif health == "3":
        print("Aww... sending virtual hugs")
    else:
        print("I couldn't tell how you're feeling, but I'm here anyway.")

def userName():
    user_name = input("Okay! What is your name?\nMy name is: ")
    print("Okay, hello", user_name + "!")

# Main loop
while True:
    continue_now = input("\nWhat would you wanna do?\n 1. Talk\n 2. Ask\n 3. Quit\n")
    if continue_now == "1":
        generalQuest()
        userName()
    elif continue_now == "2":
        print("Sure! What do you wanna talk about?")
    elif continue_now == "3":
        print("Okay, bye bye~")
        break  # use break instead of quit() so the program ends cleanly
    else:
        print("I didn't understand that... try 1, 2, or 3 💬")
        break
