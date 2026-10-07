#Morse Codes
MORSE_CODE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.", "G": "--.",   "H": "....",
    "I": "..",    "J": ".---", "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",   "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",  "S": "...",   "T": "-",
    "U": "..-",   "V": "...-", "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}
# A function to accept a text message and convert it to morse code
def text_msg(text):
    result = []
    for char in text.upper():
        if char == " ":
            result.append("/")
        elif char in MORSE_CODE:
            result.append(MORSE_CODE[char])
    return " ".join(result)
#Enter message to be converted
text_code = input("Enter a message: ")
#Call the text_msg function to convert the text message
converted_text = text_msg(text_code)
print("Morse Code:")
print(converted_text)