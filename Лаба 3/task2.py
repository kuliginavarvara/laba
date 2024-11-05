# TODO Напишите функцию find_common_participants

def find_common_participants(firstgroup, secondgroup, separator=","):
    participants_first_group = firstgroup.split(separator)
    participants_second_group = secondgroup.split(separator)

    common_particip = []
    for i in participants_first_group:
        if i in participants_second_group:
            common_particip.append(i)
    return sorted(common_particip)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))

# TODO Провеьте работу функции с разделителем отличным от запятой


