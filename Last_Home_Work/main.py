from Last_Home_Work import FileProcessor






if __name__ == '__main__':
    f_list = FileProcessor.open_list_files('list_files.txt')
    f_list1 = FileProcessor.append_f(f_list)
    index_sku = FileProcessor.index_tab(f_list1, 'sku')
    index_warehouse = FileProcessor.index_tab(f_list1, 'warehouse')
    index_operation = FileProcessor.index_tab(f_list1, 'operation')
    print(f'прибуток від усіх операцій типу sale скдладає: {FileProcessor.sale(f_list1):.2f}')




