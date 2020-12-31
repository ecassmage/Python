import random
import math
import time
SIZE = 10
ROUNDS = 100000


def make_random_pattern(size):
    sample = {}
    locations, paths = [], []
    for i_location in range(size):
        while True:
            rand_location = random.randrange(1, size + 1)
            if rand_location not in locations:
                locations.append(rand_location)
                break
        while True:
            rand_path = random.randrange(1, size + 1)
            if rand_path not in paths:
                paths.append(rand_path)
                break
        sample.update({rand_location: rand_path})
    return sample


def chain_rule(current_number, current_map):
    next_num = current_number
    for i in range(0, math.ceil(SIZE / 2)):
        # print(next_num)
        next_num = current_map[next_num]
        if current_number == next_num:
            return 1
    return 0


def random_guess(current_number, size):
    random_pick = []
    for _ in range(math.ceil(size / 2)):
        while True:
            current_num = random.randrange(1, size + 1)
            if current_num not in random_pick:
                random_pick.append(current_num)
                if current_number == current_num:
                    return 1
                else:
                    break
    return 0


def true_random(current_number):
    for i in range(math.ceil(SIZE / 2)):
        true_number = random.randrange(1, SIZE + 1)
        if current_number == true_number:
            return 1
    return 0


def play(sample_map, size):
    # chain_loss, random_loss, truly_random = False, False, False
    # win_chain, win_random, win_true_random = 0, 0, 0
    wins_and_losses = []
    for current_num in range(1, size + 1):
        # if chain_loss is False:
        win_chain = chain_rule(current_num, sample_map)
            # if win_chain == 0:
            #     chain_loss = True
        # if random_loss is False:
        win_random = random_guess(current_num, size)
            # if win_random == 0:
            #     random_loss = True
        # if truly_random is False:
        win_true_random = true_random(current_num)
            # if win_true_random == 0:
            #     truly_random = True
        wins = (win_chain, win_random, win_true_random)
        # print(wins)
        # if chain_loss and random_loss and truly_random:
        #     break
        wins_and_losses.append(wins)
    # print(wins_and_losses)
    return wins_and_losses


def control_panel(game_size, rounds):
    chain_rule_count, random_guess_count, true_random_count, wins_loss = 0, 0, 0, []
    for _ in range(rounds):
        i_truth, j_truth, k_truth = True, True, True
        sample_map = make_random_pattern(game_size)
        # print('helllo', repr(sample_map))
        wins_loss = play(sample_map, game_size)
        for i, j, k in wins_loss:
            if i == 0:
                i_truth = False
            if j == 0:
                j_truth = False
            if k == 0:
                k_truth = False
        if i_truth:
            chain_rule_count += 1
        if j_truth:
            random_guess_count += 1
        if k_truth:
            true_random_count += 1
        if _ % 10000 == 0:
            print('%d took' % _, format(time.process_time(), '.2f'), 'seconds to process.')
        # print(chain_rule_count, random_guess_count, true_random_count)
    return chain_rule_count, random_guess_count, true_random_count


if __name__ == "__main__":
    answer = control_panel(SIZE, ROUNDS)
    print('hello', answer)