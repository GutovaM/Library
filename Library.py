import pandas as pd
from tabulate import tabulate


data = {
    'Main Genre': ['Non-Fiction', 'Fantasy', 'Science Fiction', 'Mystery', 'Thriller',
                   'Romance', 'Horror', 'Non-Fiction', 'Fantasy', 'Science Fiction',
                   'Mystery', 'Thriller', 'Romance', 'Horror', 'Non-Fiction', 'Fantasy',
                   'Science Fiction', 'Mystery', 'Thriller', 'Fantasy', 'Science Fiction', 'Mystery',
                   'Thriller','Romance', 'Non-Fiction', 'Fantasy', 'Science Fiction', 'Mystery',
                   'Thriller', 'Fantasy', 'Science Fiction', 'Mystery', 'Thriller',
                   'Romance','Horror', 'Fantasy', 'Romance', 'Mystery'],
    'Author': ['Bill Bryson', 'Neil Gaiman', 'Ray Bradbury', 'P.D. James', 'Harlan Coben',
               'Julia Quinn', 'Clive Barker', 'Stephen Hawkingv', 'Patrick Rothfuss', 'William Gibson',
               'Donna Tartt', 'Lisa Gardner', 'Nora Roberts', 'Stephen King', 'Atul Gawande', 'V.E. Schwab',
               'Octavia Butler', 'Liane Moriarty', 'Greg Iles', 'Terry Brooks', 'Orson Scott Card', 'Henning Mankell',
               'Karin Slaughter','Colleen Hoover', 'Eric Schlosser', 'N.K. Jemisin', 'Kim Stanley Robinson', 'Elizabeth George',
               'Mary Kubica', 'J.K. Rowling', 'Isaac Asimov', 'Agatha Christie', 'Stephen King',
               'Jane Austen','H.P. Lovecraft', 'George R.R. Martin', 'Nicholas Sparks', 'Raymond Chandler'],
    'Title': ['A Short History of Nearly Everything', 'American Gods', 'Fahrenheit 451', 'Cover Her Face', 'Tell No One',
              'The Duke and', 'Hellbound Heart', 'A Brief History of Time', 'The Name of the Wind', 'Neuromancer',
              'The Secret History', 'Fear Nothing', 'Vision in White', 'Pet Sematary', 'Being Mortal', 'Vicious',
              'Kindred', 'Big Little Lies', 'Natchez Burning', 'The Sword of Shannara', 'Ender\'s Game', 'Faceless Killers',
              'Pretty Girls', 'It Ends with Us', 'Fast Food Nation', 'The Fifth Season', 'Red Mars', 'A Great Deliverance',
              'The Other Mrs', 'Harry Potter and the Sorcerer\'s Stone', 'Foundation', 'Murder on the Orient Express', 'The Shining',
              'Pride and Prejudice','The Call of Cthulhu', 'A Game of Thrones', 'The Notebook', 'The Big Sleep']
}

df = pd.DataFrame(data)
df_list = df.values.tolist()

def quick_sort(unsorted, start, end):
    if start >= end:
        return

    i_pivot = partition(unsorted, start, end)
    quick_sort(unsorted, start, i_pivot - 1)  # Сортируем левую часть
    quick_sort(unsorted, i_pivot + 1, end)    # Сортируем правую часть

def partition(unsorted, start, end):
    """ Разделение массива на две части по опорному элементу """
    pivot = unsorted[end]  # Опорный элемент
    i_pivot = start

    for i in range(start, end):
        # Сравниваем по жанру, автору и названию
        if (unsorted[i][df.columns.get_loc('Main Genre')] < pivot[df.columns.get_loc('Main Genre')] or
            (unsorted[i][df.columns.get_loc('Main Genre')] == pivot[df.columns.get_loc('Main Genre')]
             and unsorted[i][df.columns.get_loc('Author')] < pivot[df.columns.get_loc('Author')]) or
            (unsorted[i][df.columns.get_loc('Main Genre')] == pivot[df.columns.get_loc('Main Genre')]
             and unsorted[i][df.columns.get_loc('Author')] == pivot[df.columns.get_loc('Author')]
             and unsorted[i][df.columns.get_loc('Title')] < pivot[df.columns.get_loc('Title')])):
            unsorted[i], unsorted[i_pivot] = unsorted[i_pivot], unsorted[i]  # Меняем местами
            i_pivot += 1

    unsorted[i_pivot], unsorted[end] = unsorted[end], unsorted[i_pivot]  # Ставим опорный элемент на его место
    return i_pivot

# Сортировка по жанру, автору и названию
quick_sort(df_list, 0, len(df_list) - 1)

sorted_df = pd.DataFrame(df_list, columns=df.columns)
print(tabulate(sorted_df, headers='keys', tablefmt='psql'))


# Распределение книг по полкам
shelf_capacity = 4  # емкость одной полки
shelves = []    # полки
current_shelf = []    # текущая полка

for book in df_list:
    current_shelf.append(book)  # Добавляем книгу на текущую полку

    # Если текущая полка заполнена
    if len(current_shelf) >= shelf_capacity:
        shelves.append(current_shelf)  # Добавляем полку в список полок
        current_shelf = []  # Начинаем новую полку

# Добавляем оставшиеся книги на последнюю полку, если есть
if current_shelf:
    shelves.append(current_shelf)

# Выводим результат распределения по полкам
for i, shelf in enumerate(shelves):
    print(f"\nShelf {i + 1}:")
    for book in shelf:
        print(f" {book[df.columns.get_loc('Main Genre')]}, {book[df.columns.get_loc('Author')]}, {book[df.columns.get_loc('Title')]}")
