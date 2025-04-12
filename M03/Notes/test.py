def echo(anything):
    return anything + ' ' + anything

print(echo('Rumplestiltskin'))



def commentary(color):
    if color == 'red':
        return "it's a tomato."
    elif color == "green":
        return "Its a green pepper."
    elif color == 'bee purple':
        return "I dont know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."

comment = commentary('blue')
print(comment)