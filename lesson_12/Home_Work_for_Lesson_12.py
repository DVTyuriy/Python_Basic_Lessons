import csv


def counter(dic: dict, br: str):
    population = dict()

    for category in dic:
        if category[br] not in population:
            population[category[br]] = 0
        population[category[br]] += 1
    printer(population)

def printer(dic_print: dict):
    for value in dic_print:
        print(value, dic_print.get(value, 0))


if __name__ == '__main__':
    with open('tech_inventory.csv',"r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        counter(reader, 'category')
        counter(reader, 'brand')



        # category_data = header[1]
        # category_index = dict()
        # brand_population = dict()
        # WORK


            # if category['model'] not in category_index:
            #     category_index[category['model']] = list()
            # category_index[category['model']].append(category)


        # WORK


        # print(category_index)




