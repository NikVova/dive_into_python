import csv
import math

"""Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых."""


class Student:
    def __init__(self, full_name, subjects_file):
        self.full_name = full_name
        self.subjects = self.load_subjects(subjects_file)
        self.grades = {subject: [] for subject in self.subjects}
        self.test_score = {subject: [] for subject in self.subjects}

    def load_subjects(self, subjects_file):
        """Чтение списка предметов"""
        with open(subjects_file, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            subjects = next(reader)
            return subjects

    class NameDescriptor:
        def __init__(self):
            self.value = ''

        def __get__(self, instance, owner):
            return self.value

        def __set__(self, instance, value):
            for name_word in value.split(' '):
                if not name_word.isalpha() or not name_word.istitle():
                    raise ValueError("ФИО должно начинаться с большой буквы и не содержать цифр: {}".format(value))
            self.value = value

    full_name = NameDescriptor()

    def add_grade(self, subject, grade):
        """"Проверка и хранение оценок по предмету"""
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' не найден.")
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть в диапазоне от 2 до 5.")
        self.grades[subject].append(grade)

    def add_test_score(self, subject, score):
        """Проверка и сохранение результатов теста по предметам"""
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' не найден.")
        if not 0 <= score <= 100:
            raise ValueError("Результат теста должен быть в диапазоне от 0 до 100.")
        self.test_score[subject].append(score)

    def average_test_score(self, subject):
        """Выдает результат среднего балла за тесты по предмету"""
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' не найден.")
        if not self.test_score[subject]:
            raise ValueError("Нет результатов тестов для этого предмета.")
        return f'Средний балл за тесты по предмету {subject}: {round(sum(self.test_score[subject]) / len(self.test_score[subject]), 2)}'

    def average_overall_grade(self):
        """Расчет среднего балла по всем предметам"""
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if not all_grades:
            raise ValueError("Нет оценок для расчета среднего балла.")
        return f'Средний балл по сумме всех предметов: {round(sum(all_grades) / len(all_grades), 2)}'


student = Student('Иванов Иван Иванович', 'subjects.csv')

student.add_grade("Математика", 4)
student.add_grade("Математика", 5)
student.add_test_score("Математика", 80)
student.add_test_score("Математика", 90)
student.add_grade("Литература", 5)
student.add_grade("Физика", 4)
student.add_grade("Физика", 5)
student.add_grade("Физика", 5)
student.add_grade("Физика", 5)
student.add_test_score("Физика", 70)
student.add_test_score("Физика", 80)
student.add_test_score("Физика", 90)

# Получаем средний балл за тест по предмету
math_test_average = student.average_test_score("Физика")
print(math_test_average)

# Получаем средний балл по всем предметам
all_average = student.average_overall_grade()
print(all_average)

# student.add_grade("Физкультура", 5) # ValueError: Предмет 'Физкультура' не найден.
# student.add_grade("Физика", 7) # ValueError: Оценка должна быть в диапазоне от 2 до 5.
# student.add_test_score("Физкультура", 70) # ValueError: Предмет 'Физкультура' не найден.
# student.add_test_score("Физика", 110) # ValueError: Результат теста должен быть в диапазоне от 0 до 100.
# student = Student('ванов Иван Иванович', 'subjects.csv') # ValueError: ФИО должно начинаться с большой буквы и
                                                           # не содержать цифр: ванов Иван Иванович