csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = read_from_string(csv)
    data = sort_by_age_asc(data)
    data = filter_asc(data)
    return data


def read_from_string(string):
    return [i.split(';') for i in string.split('\n')]


def sort_by_age_asc(list):
    return sorted(list, key=lambda col: int(col[1]))


def filter_asc(list):
    return [i for i in list if int(i[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
