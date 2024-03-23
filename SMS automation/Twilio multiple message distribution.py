# SENDING MESSAGES VIA TWILIO -> PERSONAL PHONE NUMBER 

from twilio.rest import Client
import time as t
from time import sleep  # Sets a delay to be added between inputs.
import os  # Grants access to environmental variables


def Ask_For_Number():
    upper_bound = int(input("Pick a number between 1-5: ")) # Input number is the amount of messages that will be sent to my phone number (assigned value for "to") 
    message_number = 0  # Starting message number, increments each time.

    Input_Checker(upper_bound, message_number)  # RUNS INPUT CHECKER FUNCTION FOR VALIDATION.

# --------------------------------- VALIDATION ---------------------------------------------------------------------------------------------------------- 
    # IFs: if input is too small, do X - if input is too large, do Y.
    # ELIFS: input is in specified range -> call function to send X volume of messages.
    # FINALLY else (any other input detected) - produce error message -> loop to Ask_for_Number until condition satisfied.

def Input_Checker(upper_bound, message_number): # Pasing in locals.
    if upper_bound < 1:
        print("ERROR: The number you have entered is smaller than than lower limit, try again.\n\n")    # Produce appropriate error message
        t.sleep(1)      # add 1 second delay before function call
        Ask_For_Number()    # Call func to re-ask for input until valid input is given by user.

    elif upper_bound > 5:
        print("ERROR: The number you have entered is bigger than than upper limit, try again.\n\n")
        t.sleep(1)
        Ask_For_Number()

    # Successful input - parameters are met.
    elif 1 < upper_bound < 6:
        Send_SMS(upper_bound, message_number)

    else:
        print(print("ERROR: Your input is not recognised, please type in a number between the range.\n\n"))
        t.sleep(1)
        Ask_For_Number()

# WORKING VALIDATION: IF CORRECT INPUT IS DETECTED WITH NUMBER BETWEEN THE RANGE, CARRY OUT SENDING FUNCTION.
def Send_SMS(upper_bound, message_number):
    for i in range(0, upper_bound):

        # APPLYING INCREMENT AT START TO REMOVE INDEX 0 MESSAGE NUMBER.
        message_number += 1 # Incrementing message number by one each time a message is sent.

        # TWILIO DETAILS FOR MY ACCOUNT TO SEND THROUGH MESSAGE.
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")  # USING ENVIRONMENTAL VARIABLES TO SECURE DATA.
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(       # Creating message connection.
        from_= os.environ.get("TWILIO_VIRTUAL_NUM"),
        body= f"Message number {message_number}: THIS IS A TEST MESSAGE.",  # Sending personalised message (for example given, "test message")
        to= os.environ.get("BEAU_PERSONAL_PHONE_NUMBER")
        )

        print(message.sid)      # Printing success message + individual message SID (Security Identifier) to verify that a message has been sent to my phone.

Ask_For_Number()    # Calls function to begin program.
