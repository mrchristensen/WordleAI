from operator import le
from re import L
import copy

def evaluate_uncertainty(guess, answer):
    # for letter in guess:
    #     print(letter)
    return 1

if __name__ == '__main__':
    possible_guesses = open("possible-guesses.txt").read().splitlines()
    all_possible_answers = open("possible-answers.txt").read().splitlines()
    LEN_POSSIBLE_ANSWERS = len(all_possible_answers)

    for guess in possible_guesses:
        print("Starting evaluation for guess: ", guess)
        score = 0

        for answer in all_possible_answers:
            letters_not_in_answer = set()  # Gray guesses
            letters_in_answer = set()  # Yellow or green guesses

            for letter in guess:
                if answer.count(letter) == 0:  # If the letter of our guess isn't in the answer
                    letters_not_in_answer.add(letter)
                else:  # If the letter of our guess is in the answer
                    letters_in_answer.add(letter)

            possible_answers = copy.deepcopy(all_possible_answers)

            print("Possible answers before '", guess, "' guess with '", answer, "' answer: ", len(possible_answers))

            for answer in list(possible_answers):
                removed = False
                for letter in letters_not_in_answer:
                    if answer.count(letter) > 0:
                        possible_answers.remove(answer)
                        removed = True
                        break

                if removed:
                    continue

                for letter in letters_in_answer:
                    if answer.count(letter) == 0:
                        possible_answers.remove(answer)
                        break  # Todo: make this jump out of both loops.  if we remove the answer we want to go right to the next one

            print("Possible answers after '", guess, "' guess: (len: ", len(possible_answers), ")", possible_answers)

            score += evaluate_uncertainty(guess, answer)

        score = score / LEN_POSSIBLE_ANSWERS

        print("Score for '", guess, "' is: ", score)

