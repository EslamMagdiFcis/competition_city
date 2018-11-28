import csv


def check_point_part_of_city(point):
        cities = read_cities()
        for city in cities:
            if city.top_left_x <= point.x <= city.bottom_right_x:
                if city.top_left_y <= point.y <= city.bottom_right_y:
                    return city.name

        return None


def read_cities():
    cities = list()
    with open('cities.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            city = CityCoordinates(row['Name'], row['TopLeft_X'], row['TopLeft_Y'],
                                   row['BottomRight_X'], row['BottomRight_Y'])
            cities.append(city)
    return cities


class CityCoordinates:
    def __init__(self, name, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        self.name = name
        self.top_left_x = int(top_left_x)
        self.top_left_y = int(top_left_y)
        self.bottom_right_x = int(bottom_right_x)
        self.bottom_right_y = int(bottom_right_y)


def read_points():
    points = list()
    with open('points.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            single_point = point(row['X'], row['Y'])
            points.append(single_point)

    return points


class point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


def write_result_incsvfile(result):
    result_file = open("output_points.csv", 'w')
    for item in result:
        result_file.write(str(item) + ',')
    result_file.close()


if __name__ == '__main__':
    points = read_points()
    result = list()
    for point in points:
        result.append(check_point_part_of_city(point))

    write_result_incsvfile(result)
