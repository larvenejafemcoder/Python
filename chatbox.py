print("Hello, I am an AI chatbox, ready for service!")

def whatsmyname():
    print("Hello! My name is PookieGPT")
    print("I was written in Python to make you feel at home ")
    
    health = input("How is your day?\n 1. It's good\n 2. Fine I guess\n 3. Not really good lmao\n")
    
    if health == "1":
        print("Yay! I'm happy you're doing well")
    elif health == "2":
        print("Hmm, neutral vibe... wanna talk more?")
    elif health == "3":
        print("Aww... sending virtual hugs")
    else:
        print("I couldn't tell how you're feeling, but I'm here anyway")

def continue_chat():
    while True:
        continue_now = input("\nWhat would you wanna do?\n 1. Talk\n 2. Ask\n 3. Quit\n")

        if continue_now == "1":
            whatsmyname()
        elif continue_now == "2":
            print("Sure! What do you wanna talk about?")
        elif continue_now == "3":
            print("Okay, bye bye~")
            quit()
        else:
            print("I didn't understand that... try 1, 2, or 3 💬")
            quit()

continue_chat()
