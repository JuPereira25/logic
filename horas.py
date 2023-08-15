"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

now_hour = int(input('Enter type what time is it: '))

if 0 <= now_hour <= 11:
    print('Good Morning!')

elif 12 <= now_hour <= 17:
    print('Good Afternoon!')

elif 18 <= now_hour <= 23:
    print('Good Night!')

else:
    print('I dont know this time')

