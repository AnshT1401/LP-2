responses = {
    "hi":"Hello, welcome to Enterprise Bot, How may I assist you?",
    "services":"following are the services we offer: \n1.Software Development\n2.Cloud Computing\n3.Data Analytics",
    "it support":"Great, Let me transfer you to our IT Support team",
    "software development":"Great, Let me transfer you to our software development team",
    "cloud computing":"Great, Let me transfer you to our cloud computing team",
    "data analytics":"Great, Let me transfer you to our data analytics team",
    "default":"Sorry, I did not understand your response, "
}

def get_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input:
        return responses["hi"]
    elif "it support" in user_input:
        return responses["it support"]
    elif "services" in user_input:
        return responses["services"]
    elif "software development" in user_input:
        return responses["software development"]
    elif "cloud computing" in user_input:
        return responses["cloud computing"]
    elif "data analytics" in user_input:
        return responses["data analytics"]
    elif "default" in user_input:
        return responses["default"]

    elif "bye" in user_input:
        return "Thank you for using Enterprise bot, Have a great day"

    else:
        return responses["default"]


print("Hello, welcome to Enterprise Bot, How may I assist you?")

while True:
    user_input = input("You:")

    if "bye" in user_input:
        print(get_response(user_input))
        break
    else:
        print(get_response(user_input))