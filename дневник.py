# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()

# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']

# заранее заданные оценки для каждого ученика и предмета
students_marks = {
    'Ангелина': {
        'Математика': [5, 4, 5],
        'Русский язык': [3, 4, 4],
        'Информатика': [5, 5, 5]
    },
    'Александра': {
        'Математика': [4, 3, 4],
        'Русский язык': [5, 5, 4],
        'Информатика': [4, 4, 3]
    },
    'Аполлон': {
        'Математика': [3, 2, 4],
        'Русский язык': [5, 5, 5],
        'Информатика': [4, 3, 4]
    },
    'Дарья': {
        'Математика': [5, 5, 5],
        'Русский язык': [4, 3, 4],
        'Информатика': [5, 4, 5]
    },
    'Ярослав': {
        'Математика': [2, 3, 3],
        'Русский язык': [5, 4, 3],
        'Информатика': [3, 3, 4]
    }
}

# основное меню
print('''
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Удалить ученика, предмет или оценку
5. Редактировать оценки ученика
6. Вывести все оценки по определенному ученику
7. Вывести средний балл по каждому предмету для определенного ученика
8. Добавить нового ученика или предмет
9. Выход из программы
''')

while True:
    try:
        command = int(input('Введите команду: '))
        if command == 1:
            print('1. Добавить оценку ученика по предмету')
            student = input('Введите имя ученика: ')
            class_ = input('Введите предмет: ')
            try:
                mark = int(input('Введите оценку: '))
                if mark < 1 or mark > 5:
                    print('Ошибка: оценка должна быть от 1 до 5.')
                    continue
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
            except ValueError:
                print('Ошибка: оценка должна быть числом.')

        elif command == 2:
            print('2. Вывести средний балл по всем предметам по каждому ученику')
            for student in students:
                print(student)
                for class_ in classes:
                    marks_sum = sum(students_marks[student][class_])
                    marks_count = len(students_marks[student][class_])
                    print(f'{class_} - {marks_sum / marks_count:2.2f}')
                print()

        elif command == 3:
            print('3. Вывести все оценки по всем ученикам')
            for student in students:
                print(student)
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                print()

        elif command == 4:
            print('4. Удалить ученика, предмет или оценку')
            action = input('Что вы хотите удалить? (ученика/предмет/оценку): ').strip().lower()
            if action == 'ученика':
                student = input('Введите имя ученика для удаления: ')
                if student in students_marks.keys():
                    del students_marks[student]
                    students.remove(student)
                    print(f'Ученик {student} удален.')
                else:
                    print('Ученик не найден.')
            elif action == 'предмет':
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    del students_marks[student][class_]
                    print(f'Предмет {class_} удален у ученика {student}.')
                else:
                    print('Ошибка: Неверное имя ученика или предмет.')
            elif action == 'оценку':
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    print(f'Оценки по {class_}: {students_marks[student][class_]}')
                    try:
                        mark = int(input('Введите оценку для удаления: '))
                        students_marks[student][class_].remove(mark)
                        print(f'Оценка {mark} удалена для {student} по предмету {class_}.')
                    except ValueError:
                        print('Ошибка: Указанной оценки нет.')
                else:
                    print('Ошибка: Неверное имя ученика или предмет.')

        elif command == 5:
            print('5. Редактировать оценки ученика')
            student = input('Введите имя ученика: ')
            class_ = input('Введите предмет: ')
            if student in students_marks.keys() and class_ in students_marks[student].keys():
                print(f'Текущие оценки: {students_marks[student][class_]}')
                new_marks = input('Введите новые оценки через пробел: ').split()
                try:
                    new_marks = list(map(int, new_marks))
                    students_marks[student][class_] = new_marks
                    print(f'Оценки обновлены для {student} по предмету {class_}.')
                except ValueError:
                    print('Ошибка: Оценки должны быть числами.')
            else:
                print('Ошибка: Неверное имя ученика или предмет.')

        elif command == 6:
            print('6. Вывести все оценки по определенному ученику')
            student = input('Введите имя ученика: ')
            if student in students_marks.keys():
                print(student)
                for class_ in students_marks[student]:
                    print(f'{class_} - {students_marks[student][class_]}')
            else:
                print('Ученик не найден.')

        elif command == 7:
            print('7. Вывести средний балл по каждому предмету для определенного ученика')
            student = input('Введите имя ученика: ')
            if student in students_marks.keys():
                for class_ in students_marks[student]:
                    marks_sum = sum(students_marks[student][class_])
                    marks_count = len(students_marks[student][class_])
                    print(f'{class_} - {marks_sum / marks_count:.2f}')
            else:
                print('Ученик не найден.')

        elif command == 8:
            print('8. Добавить нового ученика или предмет')
            action = input('Что вы хотите добавить? (ученика/предмет): ').strip().lower()
            if action == 'ученика':
                new_student = input('Введите имя нового ученика: ')
                if new_student not in students_marks.keys():
                    students.append(new_student)
                    students.sort()
                    students_marks[new_student] = {class_: [] for class_ in classes}
                    print(f'Ученик {new_student} добавлен.')
                else:
                    print('Такой ученик уже существует.')
            elif action == 'предмет':
                new_class = input('Введите название нового предмета: ')
                if new_class not in classes:
                    classes.append(new_class)
                    for student in students:
                        students_marks[student][new_class] = []
                    print(f'Предмет {new_class} добавлен.')
                else:
                    print('Такой предмет уже существует.')

        elif command == 9:
            print('9. Выход из программы')
            break

        else:
            print('Ошибка: неизвестная команда.')
    except ValueError:
        print('Ошибка: введите корректное число для команды.')