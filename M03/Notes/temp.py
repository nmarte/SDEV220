def print_more(required1, required2, *params):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', params)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
