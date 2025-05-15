# AMDG

#
# Developer: Justin Nguyen
# Last Edited: 05/14/2025
# Created: 05/13/2025
# Description: Takes the user's input, appends it as a Caesar's Cipher message according to a user-specified shift factor in a new file.
#

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import keyboard # This will be used later on.

# Variables are defined here.
letterShift = 0
userText = ""
option = 0
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This is the beginning of the actions of the program. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Hello World!")
print("")
print("Welcome to the Caesar's Cipher Site, or the Password Generator (that is 100% conceptual and I hope you don't actually use it for passwords).")
print("")
print("Please press 1 for the Caesar's Cipher site, or 2 for the Password Generator (that you should again not use for any actual password).")
# This block of code lets the user choose 1 of 2 options. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
while True:
    if keyboard.is_pressed("1"): # This sets the option to the Caesar's Cipher generator.
        print("")
        print("Great! You selected the Cipher Site.")
        option = 1
        break
    if keyboard.is_pressed("2"): # This breaks the news that the Password Generator actually doesn't exist and ends the program.
        print("")
        print("Nice! You selected the Password Generator (that should never be used for an actual password.).")
        print("Unfortunately, that has not been made yet. Tune in next time for that.")
        option = 2
        break
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This code will actually begin the Caesar's Cipher. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if option == 1:
    print("To begin, please enter, as an integer, how many letters up you want to shift. Negative numbers will be made positive.")
# This block of code records the user's value to be shifted as a positive integer and rejects non-integer inputs. - - - - - - - - - - - - - - - - - - -
    while True:
        try:
            letterShift = abs((int(input("Negative numbers will be made positive. \n")))) % 26 # Shift Amnt = Remainder when Input / 26
            break
        except ValueError:
            print("Please enter an integer value.")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Here, the user is asked to confirm their message to get translated. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print("")
    print("Please now enter your text.")
    userText = input()
    print("Please press Y to confirm that your message is \"" + userText + "\"")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The user is informed that the cipher translation is starting. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    while True:
        if keyboard.is_pressed("Y"):
            print("Beginning translation process...")
            break
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# This is where the translation process occurs. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for i, char in enumerate(userText): # This cycles through all the characters in the user text.
        if char.isalpha(): # This ensures only letters are getting shifted, and not #'s / symbols.
            newLetterValue = ord(char) + letterShift # Gets the ASCII value of the shifted letter.
            if char.isupper(): # This line makes a distinction between an uppercase and lowercase.
                if newLetterValue > 90: # Ensures the ASCII doesn't go beyond the character range.
                    newLetterValue = newLetterValue - 90 + 64 # This'll loop back to A, if needed.
                else: # The following occurs if shifted ASCII value is within the uppercase range.
                    newLetterValue = newLetterValue # That ASCII value would remain constant here.
            elif char.islower(): # If the letter is found to be lowercase, the code below happens.
                if newLetterValue > 122: # 122 is the ASCII value above the unaccented lowercases.
                    newLetterValue = newLetterValue - 122 + 96 # The letter goes back around to A.
                else: # However, if the ASCII value is within range, the letter can stay the same.
                    newLetterValue = newLetterValue # Here, the letter's ASCII # is set to itself.
            newLetter = chr(newLetterValue) # This'll change the ASCII value to the actual letter.
            userText = userText.replace(char, newLetter) # The input is then modified as demanded.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The new, modified message is printed and appended to a file, followed by a user-inputted message to end it. - - - - - - - - - - - - - - - - - - - - -
    print(userText) # This line prints out the modified message in the output space.
    newFile = open("the_message.txt", "a", encoding="utf-8") # A new file is opened.
    newFile.write(userText + "\n") # The modified message is then added to the file.
    print("How would you like to conclude your message?") # A prompt for conclusion.
    conclusion = str(input()) # The user's last word(s) is/are stored in a variable.
    newFile.write("\n" + conclusion) # That variable is appended to the opened file.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
