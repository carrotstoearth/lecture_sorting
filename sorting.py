import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data


def selection_sort(number_row):
    idx = 0
    while idx < (len(number_row) - 1):
        for number in number_row:
            local_row = number_row[idx:]
            local_minimum = min(local_row)
            if local_minimum < number:
                number_row[idx], number_row[local_row.index(local_minimum)+idx] = number_row[local_row.index(local_minimum)+idx], number_row[idx]
            idx += 1
    return number_row


def bubble_sort(number_row_2):
    for i in range(len(number_row_2)-1):
        for idx, number in enumerate(number_row_2):
            while idx < len(number_row_2) - 1:
                if number_row_2[idx] > number_row_2[idx+1]:
                    number_row_2[idx], number_row_2[idx+1] = number_row_2[idx+1], number_row_2[idx]
                break
    return number_row_2


def main():
    print(read_data("numbers.csv"))
    print(selection_sort([1, 8, 7, 6, 5, 2, 11, 4, 3, 9, 12]))
    print(bubble_sort([1, 8, 7, 6, 5, 2, 11, 4, 3, 9, 12]))


if __name__ == '__main__':
    main()
