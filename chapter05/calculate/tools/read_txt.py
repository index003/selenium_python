
def read_txt(filename):
    file_path = "../data/" + filename
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


if __name__ == '__main__':
    datas = read_txt("tmp.txt")
    arrs = []
    for data in datas:
        arrs.append(tuple(data.strip().split(",")))
    print(arrs)