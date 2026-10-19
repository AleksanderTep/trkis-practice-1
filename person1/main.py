from calculator import plus, minus, proizwedenie, delenie

print("Калькулятор")
print("2 + 2 =", plus(2, 2))
print("5 - 3 =", minus(5, 3))
print("4 * 3 =", proizwedenie(4, 3))
print("10 / 2 =", delenie(10, 2))
print("10 / 0 =", delenie(10, 0))
print()

print("Здесь был person2")
print("Это другие изменения, они не в стэше")
print("Это временное изменение для стэша")
