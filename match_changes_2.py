first_1_min = int(input())
first_2_min = int(input())
second_1_min = int(input())
second_2_min = int(input())
changes_counter = 0
first_1_min = (first_1_min % 2 == 0) * first_1_min or first_1_min + 1
second_1_min = (second_1_min % 2 == 0) * second_1_min or second_1_min + 1
for f1 in range(first_1_min, 9, 2):
    for f2 in range(9, first_2_min - 1, -2):
        for s1 in range(second_1_min, 9, 2):
            for s2 in range(9, second_2_min - 1, -2):
                if s1 == f1 and s2 == f2:
                    print('Cannot change the same player.')
                    continue
                changes_counter += 1
                print(f'{f1}{f2} - {s1}{s2}')
                if changes_counter == 6:
                    exit('max changes')