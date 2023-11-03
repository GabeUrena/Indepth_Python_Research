#Emoji

message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "🙁"
}

output = ""
for word in words:
    output += emojis.get(word,word) + " "
    
print(output)

#Functions
#Break up code into reusable chuncks


def greeting():  # Define functions with def
    print("Hi there!")
    print("Welcome to this program")


print("Start")
greeting()
print("Finish")