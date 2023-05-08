def repeating_heads(n, x):
    """
    param n: number of consecutive coin flips
    param x: number of bets attempts
    returns the probability of winning bet atleast once and the required winning payout
    """
    bet_size = 100
    heads_chance = 1/2
    trial_win_chance = heads_chance**n
    trial_loss_chance = 1 - trial_win_chance
    repeated_trial_loss_chance = trial_loss_chance**x
    repeated_trial_win_chance = 1 - repeated_trial_loss_chance
    break_even_point = bet_size / repeated_trial_win_chance
    return [repeated_trial_win_chance * 100, break_even_point]


if __name__ == "__main__":
    print(repeating_heads(3, 10))