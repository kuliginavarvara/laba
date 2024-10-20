numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers[4] = 0
summ = sum(numbers)
lenn = len(numbers)
average = summ/lenn

numbers[4] = average
new_lenn = len(numbers)


# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
