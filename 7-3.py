arr = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

doffc = int(input("Сколько выходных в неделе вы хотите? "))

if doffc < 0 or doffc > 7:
    print ("Неверное значение")
elif doffc == 7:
    print ("Вы не работаете вовсе")
elif doffc == 0:
    print ("Вы работаете без выходных")
else:
    doff = arr[-doffc:]
    work = arr[:-doffc]

print ("Ваши выходные: ", doff)
print ("Ваши рабочие дни: ", work)