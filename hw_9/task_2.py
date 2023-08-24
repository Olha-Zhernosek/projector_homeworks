'''Алгоритм для бабл:

1.Зчитати вхідні дані масиву чи array
2.Визначити довжину масиву, за якою ітеруватимемось
3.Для кожного і в діапазоні від 0 до n-1:
    3.1.Для кожного j у довжині масиву мінус
    i(ітерація зовнішнього циклу):
    3.2.Порівнюємо елементи за індексом j та j+1, якщо не
    впорядковані - міняємо місцями, так у кожній ітерації
    зменшується кількість елементів, за якими ітеруємось, тож
    можна записати як n**2/2, але все одно ігнорувати)
'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = input("Enter a list of numbers separated by spaces: ")
arr = list(map(int, arr.split()))
sorted_arr = bubble_sort(arr.copy())
print("Sorted array:", sorted_arr)
