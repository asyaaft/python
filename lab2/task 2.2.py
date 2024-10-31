salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_needed = 0
total_spend = spend

for month in range(10):
    if month > 0:
        total_spend *=  (1 + increase)
    if total_spend > salary:
        total_needed += total_spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total_needed))
