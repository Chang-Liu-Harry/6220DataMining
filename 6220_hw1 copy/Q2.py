def all_itemsets(items, k):

    def generate_combinations(arr, data, start, end, index, r):

        if index == r:
            output.append(data[:])
            return

        i = start
        while i <= end and end - i + 1 >= r - index:
            data[index] = arr[i]
            generate_combinations(arr, data, i + 1, end, index + 1, r)
            i += 1

    output = []
    data = [0] * k
    generate_combinations(items, data, 0, len(items) - 1, 0, k)
    return output


print(all_itemsets(["ham", "cheese", "bread"], 2))
