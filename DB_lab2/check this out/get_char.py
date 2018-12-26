# class switch(object):
#     def __init__(self, value):
#         self.value = value  # значение, которое будем искать
#         self.fall = False   # для пустых case блоков
#
#     def __iter__(self):     # для использования в цикле for
#         """ Возвращает один раз метод match и завершается """
#         yield self.match
#         raise StopIteration
#
#     def match(self, *args):
#         """ Указывает, нужно ли заходить в тестовый вариант """
#         if self.fall or not args:
#             # пустой список аргументов означает последний блок case
#             # fall означает, что ранее сработало условие и нужно заходить
#             #   в каждый case до первого break
#             return True
#         elif self.value in args:
#             self.fall = True
#             return True
#         return False
#
# x = int(input())
#
# for case in switch(x):
#     if case(1): pass
#     if case(2): pass
#     if case(3):
#         print('Число от 1 до 3')
#         break
#     if case(4):
#         print('Число 4')
#     if case(): # default
#         print('Другое число')