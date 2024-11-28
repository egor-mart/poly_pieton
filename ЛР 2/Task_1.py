money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

max_months = 12  
    (money_capital + salary) >= spend:
    month += 1
    money_capital = money_capital + salary - spend
    spend = spend + (spend * increase)
print("Количество месяцев, которое можно протянуть без долгов:", month)
