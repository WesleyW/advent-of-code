
matchup_scores = [3, 0, 6] # draw, loss, win
shape_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def calc_score_1(opp, me):
    offset = - (ord(me) - ord('X'))
    opp_offset = ord(opp) - ord('A')
    shape_score = shape_scores[me]
    matchup_score = matchup_scores[(offset + opp_offset) % 3]
    return shape_score + matchup_score
1, 0, 2
def calc_score_2(opp, intention):
    matchup_scores = [0, 3, 6]
    shape_offset = (ord(opp) - ord('A') + ord(intention) - ord('Y')) % 3
    matchup_offset = (ord(intention) - ord('X')) % 3
    return shape_scores[chr(ord('X') + shape_offset)] + matchup_scores[matchup_offset]

score = 0
try:
    with open("input.txt") as f:
        for l in f:
            opp,  me = l.strip().split()
            score += calc_score_2(opp, me)
except Exception as e:
    print(f'Errored on line: {l}')
print(score)
