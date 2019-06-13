# noinspection PyUnusedLocal
def fizz_buzz(number):
    output = []
    conversions = {
        '3': 'fizz',
        '5': 'buzz',
    }
    deluxe = False
    for key in list(conversions.keys()):
        criteria_count = 0
        if number % int(key) == 0:
            criteria_count += 1
        if key in str(number):
            criteria_count += 1
        if criteria_count > 0:
            output.append((conversions[key]))
        if criteria_count == 2:
            deluxe = True
    if deluxe:
        if number % 2 == 1:
            output.append('fake')
        output.append('deluxe')
    if output == []:
        return str(number)
    return ' '.join(output)



