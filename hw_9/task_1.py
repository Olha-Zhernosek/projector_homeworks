'''One day you decide to arrange all your cats in a giant circle.
Initially, none of your cats have any hats on. You walk around the
circle 100 times, always starting at the same spot, with the first
cat (cat # 1). Every time you stop at a cat, you either put a hat
on it if it doesn’t have one on, or you take its hat off if it has
one on.

    In The first round, you stop at every cat, placing a hat on each one.
    In The second round, you only stop at every second cat (#2, #4, #6,
    #8, etc.).
    In The third round, you only stop at every third cat(#3, #6, #9, #12,
    etc.).
    You continue this process until you’ve made 100 rounds around the cats
    (e.g.,
    you only visit the 100th cat).

Write a program that simply outputs which cats have hats at the end.
Optional: Make a function that can calculate hats with any amount of
rounds and cats.

Here you should write an algorithm, and after that, try to make pseudo code.
Only after that start to work. The code is simple here, but you might struggle
with the algorithm. Therefore don`t try to write a code from the first attempt.
Don't forget to calculate the complexity of your algorithm.'''


'''Алгоритм:

    Зчитати вхідні дані: кількість котів (array_of_cats) і кількість
    ітерацій (number_of_iterations).
    Створити порожній список cats_with_hats_on для зберігання котів
    із шапками.
    Для кожної ітерації від 1 до number_of_iterations:
    3.1. Для кожного кота cat від 1 до len(array_of_cats) із кроком
    num, тим самим зменшуємо кількість елементів в ітераціях
    3.1.1. Отримане за індексом cat змінюємо на протилежне
    4.1. Якщо array_of_cats[cat] дорівнює True, додати cat до списку
    cats_with_hats_on.
    Вивести список cats_with_hats_on.'''

'''Псевдокод:

    Функція get_cats_with_hats(array_of_cats, number_of_iterations):
    cats_with_hats_on = пустий список

    Для кожної ітерації num від 1 до number_of_iterations:
        Для кожного кота cat від 1 до довжини array_of_cats із кроком num:
            у array_of_cats за індексом cat змінюємо значення на протилежне
    Для кожного кота cat від 1 до довжини array_of_cats:
        Якщо array_of_cats[cat] дорівнює True:
            Додати cat до cats_with_hats_on

    Вивести cats_with_hats_on'''


def get_cats_with_hats(array_of_cats, number_of_iterations):
    cats_with_hats_on = []

    for num in range(1, number_of_iterations + 1):

        for cat in range(num, len(array_of_cats), num):

            array_of_cats[cat] = not array_of_cats[cat]

    for cat in range(1, len(array_of_cats)):

        if array_of_cats[cat]:
            cats_with_hats_on.append(cat)

    return cats_with_hats_on


array_of_cats = int(input("Enter a number of cats: "))
number_of_iterations = int(input("Enter a number of iterations: "))
cats = [False] * (array_of_cats + 1)
print(get_cats_with_hats(cats, number_of_iterations))


array_of_cats = int(input("Enter a number of cats: "))
number_of_iterations = int(input("Enter a number of iterations: "))
cats = [False] * (array_of_cats + 1)
print(get_cats_with_hats(cats, number_of_iterations))

'''Складність алгоритму:
1. Основний цикл ітерацій, що залежить від number_of_iterations, O(n)
   (де n - number_of_iterations).
   1.1 Вкладений цикл ітерацій, що залежить від len(array_of_cats), O(m)
       (де m - len(array_of_cats)), але тут щоітерації ми зменшуємо
       кількість перевіряємих котів, десь так: m/1+m/2+m/3+m/4, тож
       привудимо до log m і обидва цикли стають nlog_m
2. Додатковий цикл ітерацій, що залежить від len(array_of_cats), O(m).
   2.1 Умова із додаванням +1 в кінець списку, O(1).

Тож загальна складність: O(nlog_m + m)'''
