class Sight:
    def __init__(self, name, value, duration):
        self.name = name
        self.value = value
        self.duration = duration

    def __repr__(self):
        return f"{self.name} (Value: {self.value}, Duration: {self.duration})"


def greedy_sightseeing(sights, total_days):
    """
    Жадная стратегия выбора достопримечательностей для посещения.

    Args:
        sights: Список объектов Sight, представляющих достопримечательности.
        total_days: Общее количество доступных дней.

    Returns:
        Список выбранных достопримечательностей.
    """

    # Сортируем достопримечательности по убыванию ценности
    sorted_sights = sorted(sights, key=lambda sight: sight.value, reverse=True)
    
    selected_sights = []
    remaining_days = total_days

    for sight in sorted_sights:
        if sight.duration <= remaining_days:
            selected_sights.append(sight)
            remaining_days -= sight.duration

    return selected_sights


def find_most_valuable_sight(sights, remaining_days):
    """
    Находит достопримечательность с наибольшей ценностью, которую можно посетить за оставшееся время.
    """
    best_sight = None
    max_value = 0

    for sight in sights:
        if sight.duration <= remaining_days and sight.value > max_value:
            best_sight = sight
            max_value = sight.value

    return best_sight


def greedy_sightseeing_step_by_step(sights, total_days):
    """
    Жадный алгоритм, который на каждом шаге выбирает наиболее ценную достопримечательность,
    которую можно посетить за оставшееся время.

    Args:
        sights: Список объектов Sight, представляющих достопримечательности.
        total_days: Общее количество доступных дней.

    Returns:
        Список выбранных достопримечательностей.
    """
    selected_sights = []
    remaining_days = total_days
    available_sights = sights[:]  # Создаем копию списка, чтобы изменять его

    while True:
        best_sight = find_most_valuable_sight(available_sights, remaining_days)

        if best_sight is None:
            break  # Нет достопримечательностей, которые можно посетить

        selected_sights.append(best_sight)
        remaining_days -= best_sight.duration
        available_sights.remove(best_sight)  # Удаляем посещенную достопримечательность из списка доступных

        print(f"Выбрана достопримечательность: {best_sight.name}. Осталось дней: {remaining_days}")

    return selected_sights

# Пример использования
sights = [
    Sight("Эйфелева башня", 10, 1),
    Sight("Колизей", 8, 2),
    Sight("Лувр", 9, 3),
    Sight("Собор Святого Семейства", 7, 2),
    Sight("Биг-Бен", 6, 1),
    Sight("Бранденбургские ворота", 5, 1),
    Sight("Музей Ватикана", 8, 2),
    Sight("Парк Гуэль", 6, 1)
]

total_days = 7

print("\n----- Жадный алгоритм (сортировка по ценности) -----")
selected_sights = greedy_sightseeing(sights, total_days)
print("Выбранные достопримечательности:", selected_sights)
total_value = sum(sight.value for sight in selected_sights)
print("Общая ценность:", total_value)

print("\n----- Жадный алгоритм (шаг за шагом) -----")
selected_sights_step = greedy_sightseeing_step_by_step(sights, total_days)
print("\nВыбранные достопримечательности:", selected_sights_step)
total_value_step = sum(sight.value for sight in selected_sights_step)
print("Общая ценность:", total_value_step)


print("\nДостопримечательность с наибольшей стоимостью, которую вы успеете посетить в оставшееся время:", find_most_valuable_sight(sights, total_days) )
print("Нет, такое решение оптимальным не будет.")