def find_common_participants(group1, group2, delimiter='|'):
    # Разбиваем строки на списки с использованием разделителя
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    common_participants = []  # Список для хранения общих участников

    # Ищем общих участников
    for participant in participants1:
        if participant in participants2:
            common_participants.append(participant)

    return common_participants


# Указанные группы участников
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызов функции
common = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", common)

# Проверка работы функции с другим разделителем
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# Вызов функции с запятой в качестве разделителя
common = find_common_participants(participants_first_group, participants_second_group, delimiter=',')
print("Общие участники с запятой:", common)
