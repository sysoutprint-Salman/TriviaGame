import time

def new_game():

    question_and_answer_set_index = 0 #There are three sets of questions and answers (scroll down) this var keeps track of which sets are being used
    while question_and_answer_set_index < 3:  # To cycle through the three question sets
        questions = new_questions(question_and_answer_set_index) #Current questions (dictionary)
        answers = new_answers(question_and_answer_set_index) #Current questions (2D list)
        correct_guesses = 0
        total_questions = 0
        for question_num, (the_question, the_answer) in enumerate(questions.items(), start=1): #There is no such thing as a 0th question, so gotta start at 1
            print(the_question)
            for choice in answers[question_num-1]:  # Accesses the individual choices from each list
                print(choice)
            guess = input('Enter A-D:\n').upper()
            is_correct = check_answer(guess, question_num, question_and_answer_set_index) #Checks guess for True or False
            if is_correct:
                correct_guesses += 1
            total_questions += 1
            time.sleep(1) #A 1-sec delay after each question
        score_and_play_again = display_score_and_play_again(correct_guesses, total_questions)
        if score_and_play_again:
            question_and_answer_set_index += 1
        else:
            break

def check_answer(guess, ques_num, ques_answer_set_index):
    answers = [answer for answer in new_questions(ques_answer_set_index).values()] #Placed the correct answers for each question in a list
    if guess == answers[ques_num-1]: #If the players guess matches the the answer, it's true
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False

def display_score_and_play_again(score, num_of_questions):
    print(f'{score} out of {num_of_questions} correct, would you like to play again?')
    play_again_choice = input("Y/N\n").upper()
    if play_again_choice == "Y":
        return True
    else:
        print("Goodbye!")
        return False
def new_questions(ques_set_index): #Refreshes the questions after new game
    questions = [questions_set_one, questions_set_two, questions_set_three]
    return questions[ques_set_index]

def new_answers(answer_set_index): #Refreshes the answer choices after new game
    choices = [answer_choices_one, answer_choices_two, answer_choices_three]
    return choices[answer_set_index]


questions_set_one = {
    "In 1768, Captain James Cook set out to explore which ocean?": "A",
    "What is actually electricity?":"C",
    "Which of the following is not an international organisation??":"D",
    "Which of the following disorders is the fear of being alone?":"A",
}
questions_set_two = {
    "Which of the following is a song by the German heavy metal band “Scorpions”?": "B",
    "What is the speed of sound?":"B",
    "Which is the easiest way to tell the age of many trees?":"B",
    "What do we call a newly hatched butterfly?":"C",
}
questions_set_three = {
    "In total, how many novels were written by the Bronte sisters?": "D",
    "Which did Viking people use as money?":"B",
    "What was the first country to use tanks in combat during World War I?":"C",
    "What is the main component of the sun?":"B",
}

answer_choices_one = [
            ['A. Pacific Ocean', 'B. Atlantic Ocean', 'C. Indian Ocean', 'D. Arctic Ocean'],
           ['A. A flow of water', 'B. A flow of air', 'C. A flow of electrons', 'D. A flow of atoms'],
           ['A. FIFA', 'B. NATO', 'C. ASEAN', 'D. FBI'],
           ['A. Agoraphobia', 'B. Aerophobia', 'C. Acrophobia', 'D. Arachnophobia']
            ]
answer_choices_two = [
            ['A. Stairway to Heaven', 'B. Wind of Change', 'C. Don’t Stop Me Now', 'D. Hey Jude'],
           ['A. 120 km/h', 'B. 1,200 km/h', 'C. 400 km/h', 'D. 700 km/h'],
           ['A. To measure the width of the tree', 'B. To count the rings on the trunk', 'C. To count the number of leaves', 'D. To measure the height of the tree'],
           ['A. A moth', 'B. A butter', 'C. A caterpillar', 'D. A chrysalis']
            ]
answer_choices_three = [
            ['A. 4', 'B. 5', 'C. 6', 'D. 7'],
           ['A. Rune stones', 'B. Jewellery', 'C. Seal skins', 'D. Wool'],
           ['A. France', 'B. Japan', 'C. Britain', 'D. Germany'],
           ['A. Liquid lava', 'B. Gas', 'C. Molten iron', 'D. Rock']
            ]
new_game()