name = input('Enter your name: ')
age = input('Enter your age: ')

if name and age:
    print(f'his name is{name}')
    print(f'Your inverted name is {name[::-1]}')
 
    if ' ' in name:
       print('Your name contains spaces')

    else:
       print('your name does NOT contain spaces')
    
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is{name[0]}')
    print(f'The last letter of your name is {name[-1]}')

else:
    print('Sorry, you left fields empty')