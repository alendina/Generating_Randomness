# please work with the variable children
children = {'Emily': {'profession': 'artist', 'age': 5},
            'Adam': {'profession': 'astronaut', 'age': 9},
            'Nancy': {'profession': 'programmer', 'age': 14}}

# print(children)
for (k, v), a in zip(children.items(), (5, 9, 14)):
    children[k] = {'profession': v, 'age': a}
