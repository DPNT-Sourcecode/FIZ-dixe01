# noinspection PyUnusedLocal
def fizz_buzz(number):
    output = ""
    if number % 3 == 0 or '3' in str(number):
        output += "fizz "
    if number % 5 == 0 or '5' in str(number):
        output += "buzz "
    if output == "":
        return str(number)
    return output.strip()


