# noinspection PyUnusedLocal
def fizz_buzz(number):
    output = ''
    conversions = {
        '3': 'fizz',
        '5': 'buzz',
    }
    for key in list(conversions.keys()):
        if number % int(key) == 0 or key in str(number):
            output += (conversions[key] + ' ')
    if len(str(number)) > 1:
        deluxe = True
        for i in range(len(str(number))):
            if str(number)[0] != str(number)[i]:
                deluxe = False
        if deluxe:
            if number % 2 == 1:
                output += 'fake '
            output += 'deluxe '
    if output == '':
        return str(number)
    return output.strip()


