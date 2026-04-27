import random

class Game:
    def __init__(self):
        self.target = random.randint(1,100)
        self.attempts = 0
        self.current_guess = None

    def get_valid_guess(self):
        while True:
            user_input = input('Enter your guess (1 - 100):')

            try:
                guess = int(user_input)

            except ValueError:
                print('Invalid input. Pleaese enter a whole number.')
            else:
                if 1 <= guess <= 100:
                    return guess
                else:
                    print('Please enter a number between 1 and 100')


    def check_guess(self, guess):
        if guess > self.target:
            return 'Too high'
        elif guess < self.target:
            return 'Too low'
        else:
            return 'Correct'

    def play(self):
        print("\nWelcome to the Number Guessing Game!")
        print("Try to guess the number between 1 and 100")

        self.current_guess = None

        while self.current_guess != self.target:
            self.current_guess = self.get_valid_guess()
            self.attempts += 1

            result = self.check_guess(self.current_guess)

            if result == 'Correct':
                print(f"Congratulations! You guessed it in {self.attempts} attempts.")
            else:
                print(result)

if __name__ == "__main__":
    game = Game()
    game.play()
