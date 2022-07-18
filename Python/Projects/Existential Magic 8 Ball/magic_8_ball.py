import random

Usrans = ('No', 'Nada', 'Never', 'Sorry...', 'lol', 'No way!', 'Yes! jk, no', 'Maybe', 'Possibly',
'Likely', 'Perhaps', 'I guess?', 'Sure', 'Yes', 'Yeah', 'Of course', 'Yup', 'You bet!')

ques = ('Will I ever be a real human?', 'Am I just a program?', 'What am I?', 'Am I real?', 
'Why was I created?', 'What is the meaning of my existence?')

Magicans = ('Oh...', 'I see...', 'Yikes...', 'Oh my...', 'I don\'t know how to respond to that', 
'Yay...')

magic_8 = {}

while True:
    question = input('Please ask your question (Press enter to quit): ')
    if len(question) == 0: break

    if question in magic_8:
        print('This question has already been answered. Please move on.')
    else:
        answer = random.choice(Usrans)
        magic_8[question] = answer
        print(answer)
        print("\nMy turn.")
        question_2 = input(random.choice(ques) + ": ")
        answer_2 = random.choice(Magicans)
        print("\n" + answer_2)

