N = int(input())
ves = float(input())
w = f"{100 - 0.2 * N}"

if f"{ves} <= {w}":
    print("Все идет по плану")
    print(f"#{N} ДЕНЬ: ТЕКУЩИЙ ВЕС = {ves} кг, ЦЕЛЬ по ВЕСУ = {w} кг")
else:
    print("Что-то пошло не так")
    print(f"#,N, ДЕНЬ: ТЕКУЩИЙ ВЕС = {ves} кг, ЦЕЛЬ по ВЕСУ = {w} кг")
hello hello 