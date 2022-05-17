first_question = f'Сколько библиотек можно импортировать в один проект?'
first_question_answers = {'first_answer': 'Не более 3',
                          'second_answer': 'Не более 10',
                          'third_answer': 'Не более 5',
                          'fourth_answer': 'Не более 23',
                          'current_answer': 'Неограниченное количество',
                          }

second_question = f'Какая функция отвечает за вывод информации в консоль'
second_question_answers = {'first_answer': 'write()',
                           'current_answer': 'print()',
                           'second_answer': 'log()',
                           'third_answer': 'out()',
                           }

third_question = f'Что покажет этот код?\n\nfor i in range(5):\n\tif i % 2 == 0:\n\t\tcontinue\n\tprint(i)'
third_question_answers = {'first_answer': 'Ошибку, т.к. i не присвоена',
                          'second_answer': 'Ошибку из-за неверного вывода',
                          'current_answer': 'Числа 1 и 3',
                          'third_answer': 'Числа 1, 3 и 5',
                          'fourth_answer': 'Числа 0, 2 и 4',
                          }

fourth_question = f'Что будет результатом выполнения этого кода?\n\nx = 23\nnum = 0 if x > 10 else 11\nprint(num)'
fourth_question_answers = {'first_answer': '23',
                           'second_answer': '10',
                           'fourth_answer': '11',
                           'third_answer': 'Ошибка',
                           'current_answer': '0',
                           }

fifth_question = f'Какие ошибки допущены в коде ниже?\n\ndef factorial(n):\n\tif n == 0:\n\t\treturn 1\n\telse:\n\t\t' \
                 f'return n * factorial(n - 1)\nprint(factorial(5))'
fifth_question_answers = {'first_answer': 'Функция не може возвращать сама себя',
                          'current_answer': 'Ошибок в коде нет',
                          'second_answer': 'Надо указать тип возвращаемого значения',
                          'fourth_answer': 'Функция всегда будет возвращать 1',
                          }

sixth_question = f'Где переменная создана правильно?'
sixth_question_answers = {'current_answer': 'num = float(2)',
                          'first_answer': 'Нет правильного ответа',
                          'second_answer': 'var num = 2',
                          'third_answer': '$num = 2',
                          'fourth_answer': 'int num = 2',
                          }

seventh_question = f'Какой метод отвечает за получение данных от пользователя?'
seventh_question_answers = {'current_answer': 'Использовать input()',
                            'first_answer': 'Использвоать cin()',
                            'second_answer': 'Использовать read()',
                            'third_answer': 'Использовать readLine()',
                            'fourth_answer': 'Использовать get()',
                            }
