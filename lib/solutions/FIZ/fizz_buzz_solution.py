# noinspection PyUnusedLocal
def fizz_buzz(number):
    output = ""
    conversions = {
        '3': 'fizz',
        '5': 'buzz',
    }
    for key in list(conversions.keys()):
        if number % int(key) == 0 or key in str(number):
            output += (conversions[key] + ' ')
    if output == "":
        return str(number)
    return output.strip()
