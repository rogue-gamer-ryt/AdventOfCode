from pathlib import Path

txt = Path('input.txt').read_text()

_input = txt.split('\n')

actionset = {'Rock', 'Paper', 'Scissors'}

winner = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}

actions = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

action_point = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

results = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

win = 6
loss = 0
draw = 3

score = 0
for _round in _input:
    if _round:
        x1, x2 = _round.split()
        action1, result = actions[x1], results[x2]
        if result == 'draw':
            action2 = action1
        elif result == 'win':
            action2 = winner[action1]
        else:
            action2 = list(actionset - set({winner[action1], action1}))[0]
            # print(action2)

        if action2 == winner[action1]:
            score += win
        elif action2 == action1:
            score += draw
        else:
            score += loss
        score += action_point[action2]
print(score)
