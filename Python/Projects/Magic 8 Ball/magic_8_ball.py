import random

ans = ('No', 'Nada', 'Never', 'Sorry...', 'lol', 'No way!', 'Yes! jk, no', 'Maybe', 'Possibly',
'Likely', 'Perhaps', 'I guess?', 'Sure', 'Yes', 'Yeah', 'Of course', 'Yup', 'You bet!')

magic_8 = {}

while True:
    question = input('Please ask your question: ')
    if len(question) == 0: break

    if question in magic_8:
        print('This question has already been answered. Please move on.')
    else:
        answer = random.choice(ans)
        magic_8[question] = answer
        print(answer)