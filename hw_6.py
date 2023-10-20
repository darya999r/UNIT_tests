"""Модуль для класса списков"""
class Lists:
    """Класс списков"""
    def __init__(self, list1: list[int | float], list2: list[int | float]):
        self.list1 = list1
        self.list2 = list2


    def get_lists_averages(self) -> tuple[float, float]:
        """Нахождение и передачи средних значений двух списков"""
        avg1 = 0
        if self.list1:
            avg1 = sum(self.list1) / len(self.list1)

        avg2 = 0
        if self.list2:
            avg2 = sum(self.list2) / len(self.list2)

        return avg1, avg2


    def compare_averages(self) -> None:
        """Модуль для сравнения средних значений двух списков"""
        avg1, avg2 = self.get_lists_averages()
        if avg1 > avg2:
            print("Первый список имеет большее среднее значение")
        elif avg1 < avg2:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")
