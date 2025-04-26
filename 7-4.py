from random import randint

group1 = ["Абраменко","Бурдейная", "Гиносян", "Григорьева", "Гафуров","Добров","Ершов","Кюлян","Капкайкина","Малахов"]
group2 = ["Смолин", "Суханов", "Пивунов", "Глебов","Овечкин","Свечников","Орлов","Козлов","Кириллов","Каменев"]
team = []

print("моя группа:", ", ".join(group1))
print("другая группа:", ", ".join(group2))


for i in range(5):
    index = randint(0, len(group1)-1)
    team += (group1.pop(index),)

for i in range(5):
    index = randint(0, len(group2)-1)
    team += (group2.pop(index),)

team_sort = tuple(sorted(team))

print("команда:", ", ".join(team))
print("количество участников:", len(team))
print("отсортированная команда:", ", ".join(team_sort))

if "Пивунов" in team:
    print("Пивунов в команде")
    print("Фамилия встречается", team.count("Пивунов"), "раз")
else:
    print("Пивунов не в команде")