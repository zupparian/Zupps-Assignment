import random

#game toss coin
def toss_coin():
    # Memilih acak antara "tail" dan "head"
    result = random.choice(["tail", "head"])
    return result

def main():
    print("Welcome to the Coin Toss Game!")
    print("Can you guess the result? (tail or head)")

    # Memilih hasil acak
    result = toss_coin()

    # Loop untuk menebak
    while True:
        guess = input("Your guess: ").lower()
        if guess == result:
            print("Congratulations! You guessed correctly.")
            break  # Keluar dari loop jika tebakan benar
        else:
            print("Sorry, wrong guess. Try again!")

if __name__ == "__main__":
    main()