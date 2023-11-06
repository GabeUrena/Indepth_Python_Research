def emoji_converter(message):
    words = message.split(" ") # split up the words and find emojis
    emojis = {
        ":)": "😊",
        ":(": "🙁"
    }

    output = "" # start blank
    for word in words: # for each word in the messag
        output += emojis.get(word,word) + " " # if it is an emoji convert it, add space after each word
                                              # add these words to output        
    return output # return the newly made sentence

message = input(">")
print(emoji_converter(message))