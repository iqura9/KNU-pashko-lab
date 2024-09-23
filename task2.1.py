import random

def simulate_discrete_random_variable(N):
    outcomes = {i: 0 for i in range(1, 7)} 
    total_sum = 0
    
    for _ in range(N):
        roll = random.randint(1, 6)
        outcomes[roll] += 1
        total_sum += roll
    
    empirical_mean = total_sum / N
    
    return outcomes, empirical_mean

N = 100

outcomes, empirical_mean = simulate_discrete_random_variable(N)

print("Кількість випадків для кожного значення:")
for number, count in outcomes.items():
    print(f"Цифра {number}: {count} разів")

theoretical_mean = 3.5

print(f"\nЕмпіричне середнє значення: {empirical_mean:.2f}")
print(f"Теоретичне середнє значення: {theoretical_mean}")
