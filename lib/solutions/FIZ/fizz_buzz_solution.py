# noinspection PyUnusedLocal
def fizz_buzz(number):
    output = ""
    if number % 3 == 0:
        output += "fizz "
    if number % 5 == 0:
        output += "buzz "
    if output == "":
        return str(number)
    return output.strip()


