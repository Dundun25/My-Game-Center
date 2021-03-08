import os
from time import sleep
import random


def clear():
    blank_screen = os.system("clear")
    return blank_screen


class Game:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def dad_jokes(self):
        clear()
        print("Dad Jokes 1.0")
        sleep(2)
        clear()
        new_in_selected_game = True
        while new_in_selected_game:
            while True:  # language selection menu loop
                language = input(f"Welcome {self.name}\nselect a language or type 'exit' to back to menu "
                                 f":\n1.English\n2.Indonesia\n\n> ")
                clear()
                if language.lower().strip() != "exit":
                    try:
                        language = int(language)
                        break
                    except ValueError:
                        clear()
                        print("You dont input a number")
                break

            if language == 1:
                print("Press Enter to Continue")
                sleep(1)
                print("Get Ready For Laugh")
                sleep(1)
                input()
                clear()
                print('What do you get when you cross a snowman with a vampire?')
                input()
                sleep(1)
                print('Frostbite!')
                sleep(1)
                input()
                clear()
                print('What do dentists call an astronaut\'s cavity?')
                input()
                sleep(1)
                print('A black hole!')
                sleep(1)
                input()
                clear()
                print('Knock knock.')
                sleep(1)
                print("Who's there?")
                input("> ")
                sleep(1)
                clear()
                print("Thats it All! lol hope you enjoy")
                sleep(2)
                clear()
            elif language == 2:

                num_of_joke = 10

                print(f"selamat datang {self.name}, jokes bapak-bapak receh siap menghibur kamu ;)")
                sleep(3)
                clear()
                playing = True

                while playing:
                    continue_jokes = input(
                        "pencet tombol Enter buat lanjut atau ketik 'exit' buat balik ke menu pilih bahasa\n> ")
                    clear()

                    joke_list = []  # generate List of number for jokes
                    for joke in range(1, num_of_joke):
                        joke_list.append(joke)

                    while joke_list:
                        joke_random = random.choice(joke_list)
                        joke_list.remove(joke_random)

                        if continue_jokes.lower().strip() != "exit":

                            if continue_jokes.lower() == "exit":
                                joke_list = []
                            if joke_random == 1:
                                print("barusan saya ke apotek beli obat tidur")
                                sleep(1.5)
                                print("pas pulang saya bawa pelan-pelan, takut obatnya bangun\nxixixixi")
                                sleep(1)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                            elif joke_random == 2:
                                input("pasien yang terkena gejala rindu dilarikan kemana? ")
                                sleep(1.5)
                                print("ke ruang i see you\nxixixixi")
                                sleep(1)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                            elif joke_random == 3:
                                input("kendaraan apa yang imut kalo lagi jalan? ")
                                sleep(1.5)
                                print("kereta api. Cute, cute cute~\nxixixixi")
                                sleep(1.5)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(1.5)
                                clear()
                            elif joke_random == 4:
                                input("huruf huruf apa yang sering kedinginan?? ")
                                sleep(1.5)
                                print("Huruf B, karena berada di tengah-tengah AC\nxixixixi")
                                sleep(1.5)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                            elif joke_random == 5:
                                input("gula gula apa yang bukan gula? ")
                                sleep(1.5)
                                print("gula aren't")
                                sleep(1.5)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                            elif joke_random == 6:
                                input("Siapa artis hollywood yang bikin baper?  ")
                                sleep(1.5)
                                print("Jack sparrow.. sparrow jiwaku pergi~~")
                                sleep(1.5)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                            elif joke_random == 7:
                                input("Dimana Star-Lord diimunisasi? ")
                                sleep(1.5)
                                print("di pos Yondu")
                                sleep(1.5)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                            elif joke_random == 8:
                                input("Kenapa kalo zombi nyerangnya bareng? ")
                                sleep(1.5)
                                print("kalo sendiri namanya zomblo.")
                                sleep(1.5)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                            elif joke_random == 9:
                                print("kalo semua hal harus dipikirkan masak-masak,")
                                sleep(2)
                                print("gimana coba nasib orang-orang yang gak bisa masak..")
                                sleep(1.5)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                            elif joke_random == 10:
                                print("Pembeli : Bang ngapain ngobrol ama martabak?")
                                sleep(1.5)
                                print(
                                    "Penjual : Pesenanan pelanggan mas, dia bilang martabaknya jangan dikacangin.")
                                sleep(1.5)
                                continue_jokes = input("\nKetik exit kalau udah gak lucu: ")
                                sleep(0.5)
                                clear()
                        else:
                            del joke_random, joke_list, continue_jokes
                            playing = False
                            break
                del playing

            elif language.lower().strip() == 'exit':
                print("Thanks for playing, Please be Happy :)")
                sleep(2)
                clear()
                new_in_selected_game = False
                break

            else:
                print("Input a correct number please")

    def dragon_realm(self):
        def displayIntro():
            print("You are in a land full of dragons. In front of you,you see two caves. In one cave, the dragon is\n"
                  "friendly and will share his treasure with you. The other dragon is greedy and hungry, and will "
                  "eat\n"
                  "you on sight.\n")

        def chosen_Cave():
            cave = ''
            while cave != '1' and cave != '2':
                print(f"which cave will you enter, {self.name} ?")
                cave = input()
            return cave

        def checkCave(chosen_Cave):
            print('You approach the cave...')
            sleep(2)
            print('It is dark and spooky...')
            sleep(2)
            print('A large dragon jumps out in front of you! He opens his jaws and ...')
            print()
            sleep(2)
            friendly_cave = random.randint(1, 2)
            if chosen_Cave == str(friendly_cave):
                print('Gives you his treasure!')
            else:
                print('Gobbles you down in one bite!')

        play_again = 'yes'
        while play_again == 'yes' or play_again == 'y':
            sleep(1)
            displayIntro()
            sleep(5)
            cave_number = chosen_Cave()
            sleep(2)
            checkCave(cave_number)
            print('Do you want to play again? (yes or no)')
            play_again = input()
            clear()

        sleep(2)
        clear()

    def gura_adventure(self):
        import DaFluffyPotato
        DaFluffyPotato.run()
        del DaFluffyPotato
        clear()
        print(f"Welcome back {self.name}")
        sleep(5)
        clear()

    def guessing_game(self):
        sleep(1)
        menu = False
        new_in_selected_game = True

        while True:
            if not menu:
                clear()
                if new_in_selected_game:
                    print(f"Welcome {self.name}..\nOk, so I'm gonna Random a Number from 1 to 9 you must to guess it\n"
                          f"you got 10 point and each wrong number your score will reduce by 1")
                    input()
                    clear()
                    print("Ready?")
                    sleep(1)
                    clear()
                    print("3")
                    sleep(1)
                    clear()
                    print("2")
                    sleep(1)
                    clear()
                    print("1")
                    sleep(1)
                    clear()

                while True:

                    new_in_selected_game = False

                    if not menu:
                        random_number = random.randint(1, 9)
                        score = 10

                        while True:

                            while True:
                                player_guess = input("Guess a number(1-9): ")
                                try:
                                    player_guess = int(player_guess)
                                    break
                                except ValueError:
                                    clear()
                                    print("Input a number Please")

                            if player_guess < random_number:
                                clear()
                                print("Your Guess is too low.. ")
                                score -= 1
                            if player_guess > random_number:
                                clear()
                                print("Your Guess is too High.. ")
                                score -= 1
                            if player_guess == random_number:
                                clear()
                                print("You got it!")
                                print(f"Your score : {score}")
                                score = 10
                                break

                        while True:
                            again = input("(y/n)do you wanna play again?\n> ")
                            if again.lower().strip() == 'y' or again.lower().strip() == 'yes':
                                menu = False
                                clear()
                                break
                            if again.lower().strip() == 'n' or again.lower().strip() == 'no':
                                menu = True
                                del score, random_number, new_in_selected_game
                                clear()
                                print("Thanks for Playing\n")
                                sleep(2)
                                clear()
                                break
                            else:
                                print("Wrong Input..")
                                sleep(1)
                                clear()
                    else:
                        break

            else:
                break

    def hang_man(self):
        def get_secret_word(word_type):
            animal = ["ant", "elephant", "fish", "frog", "pig", "cat", "dog", "lion"]
            vehicle = ["car", "bus", "truck", 'airplane', 'ship', 'tractor']
            thing = ['mouse', 'pencil', 'ruler', 'monitor', 'keyboard']
            if word_type == "1":
                world = animal
                word_category = "Animal"
            elif word_type == "2":
                world = vehicle
                word_category = "Vehicle"
            elif word_type == "3":
                world = thing
                word_category = "Object Thing"
            else:
                world = animal + vehicle + thing
                word_category = "Animal/Vehicle/Object"
            word = random.choice(world)
            return word, word_category

        def display_board(missed_letter, correct_letter, secret_word, category):
            print(HANGMAN_PICS[len(missed_letter)])
            print()
            print(f"Category\t: {category}")
            print("Missed Letter\t:", end=" ")
            for letter in missed_letter:
                print(letter, end=" ")

            print()

            blanks = '_' * len(secret_word)
            for i in range(len(secret_word)):  # Replace Blanks with correct guess letter
                if secret_word[i] in correct_letter:
                    blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
            for letter in blanks:
                print(letter, end=" ")

        def get_guess(already_guessed):
            while True:
                print("\nGuess a letter : ")
                user_guess = input("> ")
                user_guess = user_guess.lower()
                if len(user_guess) != 1:
                    print("please insert only one number")
                elif user_guess in already_guessed:
                    print("you already guess that word, please guess another word")
                elif user_guess not in 'abcdefghijklmnopqrstuvwxyz':
                    print("please insert only Letter")
                else:
                    return user_guess

        def play_again():
            print("do you want to play again ?")
            return input().lower().startswith('y')

        def get_difficulty():
            HANGMAN = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\ |
      |
     ===''', '''
  +---+
  O   |
 /|\\ |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\ |
 / \\ |
     ===''']
            life = []
            while True:
                print("Select Difficulty (Easy/Normal/Hard) :")
                difficulty = input().lower().strip()
                if difficulty == "easy" or difficulty == "normal" or difficulty == "hard":
                    break
                else:
                    clear()
                    print("Wrong Input!")
                    sleep(1)
            if difficulty == "easy":
                for pic in HANGMAN:
                    for i in range(2):
                        life.append(pic)
            elif difficulty == "normal":
                for pic in HANGMAN:
                    for i in range(1):
                        life.append(pic)
            elif difficulty == "hard":
                life = HANGMAN
            return life

        clear()
        print(f"Welcome to Hangman Game, {self.name}..")
        sleep(3)
        clear()
        missed_letter = ''
        correct_letter = ''
        game_is_done = False
        # Randomized Secret Word
        while True:
            clear()
            choice = ["1", "2", "3", "4"]
            print("Hi, " + self.name + " Please Select Category first :\n1. Animal\n2. Vehicle \n3. Thing\n4. Anything")
            category = input("> ")
            if category in choice:
                clear()
                break
            else:
                print("Wrong Input")
                sleep(1)
                clear()
        secret_word, category_name = get_secret_word(category)  # Generate the secret word
        HANGMAN_PICS = get_difficulty()
        while True:
            clear()
            display_board(missed_letter, correct_letter, secret_word, category_name)

            # let the player enter the letter
            guess = get_guess(missed_letter + correct_letter)

            if guess in secret_word:
                correct_letter += guess

                found_all_letter = True
                for i in range(len(secret_word)):
                    if secret_word[i] not in correct_letter:
                        found_all_letter = False
                        break
                if found_all_letter:
                    print("Yes! the secret word is '" + secret_word + "' You have won the game, " + self.name)
                    game_is_done = True

            else:
                missed_letter += guess

                if len(missed_letter) == len(HANGMAN_PICS) - 1:
                    display_board(missed_letter, correct_letter, secret_word, category_name)
                    print(self.name + " ,You have run out of guesses!\n After " + str(
                        len(missed_letter)) + " missed guesses and " +
                          str(len(correct_letter)) + " correct guesses, the word was :" + str(secret_word))
                    game_is_done = True

            if game_is_done:
                if play_again():
                    missed_letter = ''
                    correct_letter = ''
                    game_is_done = False
                    while True:
                        clear()
                        choice = ["1", "2", "3", "4"]
                        print(
                            "Hi, " + self.name + " Please Select Category first :\n1. Animal\n2. Vehicle \n3. Thing\n4. Anything")
                        category = input("> ")
                        if category in choice:
                            clear()
                            break
                        else:
                            print("Wrong Input")
                            sleep(1)
                            clear()
                    secret_word, category_name = get_secret_word(category)  # Generate the secret word
                    get_difficulty()

                else:
                    clear()
                    print("Thanks For Playing, " + self.name + " !")
                    break


def game_menu():
    clear()
    name = input("What is Your Name?\n> ")
    clear()
    age = input("How old are you?\n> ")
    clear()
    gender = input("Describe Your Gender(F/M)\n> ")
    clear()
    new_game = True
    wrong_counter = 0

    while True:
        if new_game:
            print(f"Welcome to this game center, {name}\n")

        game_selection = input(f"Please Select a Game That You Wanna Play by calling the number or type 'exit' to "
                               f"quit:\n\n1. Guess a number\n2. Dad Jokes\n3. Dragon Realm\n4. Gura Adventure  "
                               f"\n5. Hangman\n\n> ")
        clear()
        game_selection = game_selection.lower()

        if game_selection == "1":
            wrong_counter = 0
            new_game = True
            game = Game(name, age, gender)
            game.guessing_game()
            del game
        elif game_selection == "2":
            wrong_counter = 0
            new_game = True
            game = Game(name, age, gender)
            game.dad_jokes()
            del game
        elif game_selection == "3":
            wrong_counter = 0
            new_game = True
            game = Game(name, age, gender)
            game.dragon_realm()
            del game
        elif game_selection == "4":
            wrong_counter = 0
            new_game = True
            game = Game(name, age, gender)
            game.gura_adventure()
            del game
        elif game_selection == "5":
            wrong_counter = 0
            new_game = True
            game = Game(name, age, gender)
            game.hang_man()
            sleep(2)
            clear()
            del game

        elif game_selection.lower().strip() == "exit":
            print("Thanks For Playing!")
            sleep(1)
            print("bye..")
            sleep(1)
            print("Sampai jumpa..")
            sleep(1)
            print("matane..")
            sleep(1)
            break

        else:
            wrong_counter += 1
            print(f"({wrong_counter}) I'm Sorry Wrong input \n")
            new_game = False

game_menu()
