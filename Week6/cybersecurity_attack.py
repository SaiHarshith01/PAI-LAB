attacker_moves = {'Exploit': -3, 'Phishing': -2}
defender_moves = {'Patch': 2, 'Monitor': 1}
def minimax(state, depth, is_defender):
    if depth == 0:
        return state
    
    if is_defender:
        best_score = float('-inf')
        for move, value in defender_moves.items():
            score = minimax(state + value, depth - 1, False)
            best_score = max(best_score, score)
        return best_score
    else:
        worst_score = float('inf')
        for move, value in attacker_moves.items():
            score = minimax(state + value, depth - 1, True)
            worst_score = min(worst_score, score)
        return worst_score
initial_state = 10
score = minimax(initial_state, 2, True)
print("Optimal Security Outcome Score:", score)