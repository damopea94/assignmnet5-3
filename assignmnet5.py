import xlrd
import matplotlib.pyplot as plt


def read_data(name):
    workbook = xlrd.open_workbook(name)
    sheet = workbook.sheet_by_index(0)
    return sheet


def get_column_index(name):
    data = read_data("assign11-1-catering_sale_all.xls")
    for i in range(data.nrows):
        for j in range(data.ncols):
            print("j", j)
            if data.cell_value(i, j) == name:
                print("j", j)
                return j;
    return -1


def get_values(name):
    data = read_data("assign11-1-catering_sale_all.xls")
    values = []
    index = get_column_index(name)
    for i in range(data.nrows):
        for j in range(data.ncols):
            if j != 0 and i != 0:
                if j == index:
                    print(data.cell_value(i, j))
                    values.append(data.cell_value(i, j))
    return values


def main():
    name = input("Please Enter Name=:")
    value = get_values(name)
    if (len(value) > 0):
        plt.plot(value)
        plt.show()
    else:
        print("No Data found")


main()

