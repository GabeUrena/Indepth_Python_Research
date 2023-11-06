def emoji(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "🙁"
    }

    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
        
    print(output)


   
message = input(">")
emoji(message)