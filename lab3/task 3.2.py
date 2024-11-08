# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, separator=",") -> object:
    participants_first_group = set(participants1.split(separator))
    participants_second_group = set(participants2.split(separator))
    common_participants = participants_first_group.intersection(participants_second_group)
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(common_participants)
