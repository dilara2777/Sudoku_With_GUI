import random

def main():

    possible_n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # for k in range(9):
    while possible_n:
        random_index = random.randint(0, len(possible_n) - 1)
        n = possible_n[random_index]
        print(n)
        possible_n.remove(n)

if __name__ == '__main__':
    main()