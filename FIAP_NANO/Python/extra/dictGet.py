x = 1




actions = {
    1:print('a'),
    2:print('b'),
    3:print('c'),
}

action = actions.get(x,print('d'))

action()