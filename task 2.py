salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
months_ = months
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
bank = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while months_ > 0:
    bank += salary - spend
    spend *= (increase+1)
    months_ -= 1
money_capital = bank * -1



print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
