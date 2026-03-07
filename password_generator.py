import random
import secrets
import string
import time

dev = False
while True:

    if dev == False:
# ---------------------------------------------------------------------------------------------------------------------
# Questions

# THE BEST BUGFIX EVER MADE IN THE HISTORY OF PROGRAMMING
        print('\n')
# --------------------------------------------------------------------------------------------------------------------------------------------------
        print('Generate new password? Yes or No')
        user = input('>')
        print('Enter the mode of generate password: numbers(N), letters(L) or all(A)')
        mode = input('>')
        print('How much symbols?')
        num = int(input('>'))
   



# -------------------------------------------------------------------------------------------------------------------------------------------------
# Generating password
        if user == 'yes' or user == 'Yes' or user == 'y' or user == 'Y':
            
            if mode == 'N' or mode == 'n':
                for i in range(num):
                    print(secrets.choice(string.digits), end='')

            elif mode == 'L' or mode == 'l':
                for i in range(num):
                    print(secrets.choice(string.ascii_letters), end='')

            elif mode == 'A' or mode == 'a':
                for i in range(num):
                    print(secrets.choice(string.ascii_letters + string.digits), end='')

        else: break

# -------------------------------------------------------------------------------------------------------------------------------
# dev mode(i created it for a joke)
# WORK ONLY AFTER QUESTIONS!!!!! in 20 line
    if user == 'dev=True':
        dev = True
        break

            
    else:
        pass

while dev:
    try:
        print(eval(input("Python3.12.3/>>>")))
    except:
        continue

