if __name__ == '__main__':
    # відкриваємо файл
    with open('text.txt', 'r', encoding='utf-8') as f:
        # зчитуємо інформацію з файла, перетворюємо та виводимо на екран
        print([line[line.find('a'):].title().strip() for line in f.readlines() if 'a' in line])
