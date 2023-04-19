from SKU import FileProcessor


if __name__ == '__main__':
    f_list = FileProcessor.open_list_files('list_files.txt')
    f_list1 = FileProcessor.append_f(f_list)
    for i in f_list1:
        print(i)
