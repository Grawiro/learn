name = input("Hello! What's your name: ")
age = input('How old are you: ')
weight = input('What is your weighr: ')

print('OK, I call you {}, or you prefer {}, or better {}.'.format(
    name, name.upper(), name*5))
print('You live {:,} secound, or more.'.format(
    int(age)*365*24*60*60))
print('Your weight on moon is {:.1f}, and on the sun {:.1f}.'.format(
    int(weight)/6, int(weight)*27.1))

# \ allows you to continue the command on the next line
long_text = 'this is' \
    ' very long text'

# the first letter of each word is capital
long_text.title()
# the first letter of first word is capital
long_text.capitalize()
# change a small character to a large character and vice versa
long_text.swapcase()