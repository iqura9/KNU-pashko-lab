import random

def simulate_coin_flips(N, K):
    total_heads = 0 
    
    for i in range(K):
        heads = 0
        for _ in range(N):
            if random.choice(['герб', 'решка']) == 'герб':
                heads += 1 
        total_heads += heads
        heads_percentage = (heads / N) * 100 
        print(f"Моделювання {i + 1}: {heads} гербів з {N} підкидань ({heads_percentage:.2f}%)")

    return total_heads

N = 100  # кількість підкидань монети за один раз
K = 10   # кількість повторень моделювання

total_heads = simulate_coin_flips(N, K)
average_heads = total_heads / (N * K) * 100
print(f"\nЗагальна кількість гербів після {K} моделювань по {N} підкидань: {total_heads}")
print(f"Середній відсоток гербів за всі моделювання: {average_heads:.2f}%")
