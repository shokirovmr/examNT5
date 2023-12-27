# Task2
# import threading
#
#
# def reverse_numbers(numbers):
#     def reverse_number(number):
#         reversed_num = int(str(number)[::-1])
#         print(reversed_num)
#
#     threadlar = []
#
#     for number in numbers:
#         thread = threading.Thread(target=reverse_number, args=(number,))
#         thread.start()
#
#         for thread in threadlar:
#             thread.join()
#
#
# if __name__ == '__main__':
#     numbers = input("Enter numbers to reverse it: ")
#     numbers = [int(num) for num in numbers.split()]
#     reverse_numbers(numbers)
