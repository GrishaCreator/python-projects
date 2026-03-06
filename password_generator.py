import random


dev = False
while True:

    if dev == False:
# ---------------------------------------------------------------------------------------------------------------------
# Questions
        print('Generate new password? Yes or No')
        user = input('>')
        print('How much numbers?(can generate only 4,6,8,10,15,20)')
        num = int(input('>'))
   



# -------------------------------------------------------------------------------------------------------------------------------------------------
# Generating password
        if user == 'Yes' or user == 'yes' or user == 'ok' or user == 'go' or user == 'yeah' or user == 'Yeah':
            if num == 4:
                print(random.randint(1111, 9999))
            elif num == 6:
                print(random.randint(111_111, 999_999))
            elif num == 8:
                print(random.randint(111_111_11, 999_999_99))
            elif num == 10:
                print(random.randint(111_111_111_1, 999_999_999_9))
            elif num == 15:
                print(random.randint(111_111_111_111_111, 999_999_999_999_999))
            elif num == 20:
                print(random.randint(111_111_111_111_111_111_11, 999_999_999_999_999_999_99))
            else:
                print('Sorry we cant generate this password. try use limit 4,6,8,10,15,20')

# -------------------------------------------------------------------------------------------------------------------------------
# dev mode(i created it for a joke)
# WORK ONLY AFTER QUESTION OF NUMBERS!!!!! in 12 line
    if user == 'dev=True':
        dev = True
        break

            
    else:
        pass

while dev:
    print(eval(input("Python3.12.3/>>>")))
