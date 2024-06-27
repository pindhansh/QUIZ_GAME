'''QUIZ GAME'''
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("---------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answers(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses , guesses )
def check_answers(answer , guess):
    if answer == guess:
        print("CORRRCT!")
        return 1
    else:
        print("WRONG!")
        return 0
    pass
def display_score(correct_guesses,  guesses):
    print("----------------------------")
    print("RESULT")
    print("----------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")



    score = int((correct_guesses/len(questions))*100)
    print("your score is  : " + str(score) + "%")

def play_again():
    pass

questions = {
    "who is the prime minister of india ? ": "A",
    "which of the following is a prime number ?": "B",
    "which is the most venomous? ": "D",
    "which year i was born ?": "C"
}
options = [["A.  Narendra modi", "B.  Rahul gandhi", "C.  Mamta banarjee", "D.  none"],
                ["A.  4", "B.  3", "C.  9", "D.  1"],
                 ["A.  Ex", "B.  cobra", "C.  blackmamba", "D.  python"],
                 ["A.  2004", "B.  2007", "C.  2003", "D.  2009"]]

new_game()