import random


def coin_toss():
    result = random.randint(0, 1)

    if result == 0:
        return "Орел"
    else:
        return "Решка"


def simulate_coin_tosses(num_tosses):
    
    heads_count = 0  # кількість орлів
    tails_count = 0  # кількість решок


    for _ in range(num_tosses):
        toss_result = coin_toss()
        print(toss_result)

        if toss_result == "Орел":
            heads_count += 1
        else:
            tails_count += 1


    # Виведення статистики
    print(f"Кількість орлів: {heads_count}")
    print(f"Кількість решок: {tails_count}")
    print(f"Відносна частота орла: {heads_count / num_tosses:.2f}")
    print(f"Відносна частота решки: {tails_count / num_tosses:.2f}")


# Введення кількості підкидань
num_tosses = int(input("Введіть кількість підкидань монети: "))


# Запуск симуляції
simulate_coin_tosses(num_tosses)