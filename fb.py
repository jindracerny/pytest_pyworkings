def fizzbuzz(number):
    retrn = ''
    if not(number % 3):
        retrn += 'fizz'
    if not(number % 5):
        retrn += 'buzz'
    return retrn or str(number)
