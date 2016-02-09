import random


# object that represents the user's guess
# guess: user guess value
class GuessNum(object):
    def __init__(self, guess):
        self.guess = list(guess)


# object that represents the answer
# value: randomly generated digits put together into a string
class Answer(object):
    guesses = 0

    # instantiates the value of the answer
    def __init__(self):
        self.value = list(self.generate_number())

    # generates a digit from 0-9 to be concatenated in generate_number
    # returns a random digit
    def generate_digit(self):
        return str(random.randrange(0, 9))

    # generates a number sequence based on randomly generated digits
    # returns 'key', the generated answer
    def generate_number(self):
        key = ''
        for i in range(4):
            key += self.generate_digit()
        return str(key)


# obtains the user's guess
# returns the guess value from user
def user_guess():
    while True:
        guess = str(raw_input('Guess the number: '))
        if len(guess) == 4:
            return guess
        print 'That\'s not a 4-digit number! \n'


# compares user's guess to the answer and reports cows and bulls
# returns the number of cows and bulls in an array
def evaluate_guess(answer, guess):
    cowbull = [0, 0]
    # iterates through all digits in the answer
    for i in range(4):
        if answer[i] == guess[i]:
            cowbull[0] += 1
            continue
        if guess[i] in answer:
            cowbull[1] += 1
            continue
    return cowbull

# Initiating the game
ans = Answer()
ans.value = ['1', '1', '2', '2']
print 'Welcome to the Cows and Bulls Game! \n'
cows = 0
bulls = 0
# Playing the game
while cows != 4:
    usr = GuessNum(user_guess())
    result = evaluate_guess(ans.value, usr.guess)
    cows = result[0]
    bulls = result[1]
    ans.guesses += 1
    print 'you have %d cows, and %d bulls.' %(cows, bulls)
    print '(key: %s guess: %s) \n' % (ans.value, usr.guess)

# After the game is completed
print 'You completed the game! It took you %d guesses!' % ans.guesses