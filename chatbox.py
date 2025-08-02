print("Hello, I am an AI chatbox, ready for service!")

def continue_chat():
    continue_now = input("What would you wanna do? 1.Talk 2.Ask 3.Quit\n")

    if continue_now == "1":
        print("Hello! My name is PookieGPT 💖")
    elif continue_now == "2":
        print("Sure! What do you wanna talk about? 🧠")
    elif continue_now == "3":
        print("Okay, bye bye~ ✨")
        quit()
    else:
        print("I didn't understand that... try 1, 2, or 3 💬")

continue_chat()