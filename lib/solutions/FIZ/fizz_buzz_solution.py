# noinspection PyUnusedLocal
def fizz_buzz(number):
    output = []
    conversions = {
        '3': 'fizz',
        '5': 'buzz',
    }
    deluxe = False
    for key in list(conversions.keys()):
        # rewrite here
        if number % int(key) == 0 or key in str(number):
            output.append((conversions[key]))
    if deluxe:
        if number % 2 == 1:
            output.append('fake')
        output.append('deluxe')
    if output == []:
        return str(number)
    return ' '.join(output)
