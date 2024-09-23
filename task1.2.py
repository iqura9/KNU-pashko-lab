import random

def simulate_dice_rolls(N, K=11):
    total_counts = {i: 0 for i in range(1, 7)} 
    
    for i in range(K):
        counts = {i: 0 for i in range(1, 7)}
        for _ in range(N):
            roll = random.randint(1, 6)
            counts[roll] += 1 
        
        for j in range(1, 7):
            total_counts[j] += counts[j]

        print(f"Моделювання {i + 1}:")
        for number in range(1, 7):
            percentage = (counts[number] / N) * 100
            print(f"Цифра {number}: {counts[number]} разів ({percentage:.2f}%)")

    return total_counts

N = 100  # кількість підкидань кубика за один раз
K = 11   # кількість повторень моделювання

total_counts = simulate_dice_rolls(N, K)

total_rolls = N * K
print("\nЗагальна кількість випадків і відсотки для кожної цифри після всіх моделювань:")
for number, count in total_counts.items():
    percentage = (count / total_rolls) * 100
    print(f"Цифра {number}: {count} разів ({percentage:.2f}%)")
