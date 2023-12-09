s = input('Podaj username> ')

if len(s) < 5:
    print('Za krótka nazwa; proszę wprowadzić co najmniej 5 znaków')
    print('---')
else:
    print(f'Ok, witaj {s}')

    if any(char.isupper() for char in s) and any(char.islower() for char in s):
        print('Napis zawiera zarówno duże, jak i małe litery.')
    else:
        print('Napis nie zawiera zarówno dużej, jak i małej litery.')
