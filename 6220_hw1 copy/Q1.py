import csv


def cardinality_items(filepath):
    unique_items = set()
    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for item in row:
                unique_items.add(item.strip())
    return len(unique_items)


print(cardinality_items('basket_data.csv'))
