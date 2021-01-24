from custom import bubble_sort
list_of_adapters = [0]


def funky(x, num, list_of_done={}):
    total = 0
    if num in list_of_done:
        return list_of_done[num]
    for iteration in range(num + 1, num + 4):
        if iteration in x:
            total += funky(x, iteration)
            if iteration not in list_of_done:
                list_of_done.update({iteration: total})
        if iteration == x[-1]:
            return 1
    return total


for adapter in open('input.txt'):
    adapter = adapter.replace('\n', '')
    list_of_adapters.append(int(adapter))
list_of_adapters = bubble_sort(list_of_adapters)
list_of_adapters.append(list_of_adapters[-1] + 3)
print(list_of_adapters)
single_adapter, triple_adapter = 0, 0
for previous, current in enumerate(list_of_adapters[1:]):
    if current - list_of_adapters[previous] == 1:
        single_adapter += 1
    elif current - list_of_adapters[previous] == 3:
        triple_adapter += 1

answer = single_adapter * triple_adapter
print(f'The Answer to Part 1 is {answer}')
print(f'The Answer to Part 2 is {funky(list_of_adapters, 0)}')
