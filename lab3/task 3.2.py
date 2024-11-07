# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=","):
    set1 = set(participants_first_group.split(separator))
    set2 = set(participants_second_group.split(separator))
    common_participants = list(set1.intersection(set2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
