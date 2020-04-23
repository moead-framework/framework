from pygmo import hypervolume


def extract_coordinates(result_file):
    file = open(result_file, 'r')
    file_content = list(map(str.strip, file.readlines()))

    x = []
    y = []
    z = []
    for row in file_content[1:]:
        if "Length of the list" in row:
            break
        spl = row.split(" ")
        x.append(float(spl[0]))
        y.append(float(spl[1]))

        if len(spl) == 3:
            z.append(float(spl[2]))

    if len(z) > 0:
        return x, y, z

    return x, y


def result_file_to_list(result_file):
    file = open(result_file, 'r')
    file_content = list(map(str.strip, file.readlines()))
    result_list = []

    for row in file_content[1:]:
        if "Length of the list" in row:
            break
        spl = row.split(" ")
        result_list.append([float(spl[0]), float(spl[1])])

    return result_list


def save_population(file_name, population):
    file = open(file_name, "w")
    # file.write("Length of the list = " + str(len(population)) + "\n")
    for s in population:
        row = ""
        for coordinate in s.F:
            row += str(coordinate) + " "

        row = row[:-1] + "\n"
        file.write(row)

    file.close()


def save_value_file(file_name, evaluation, value):
    file = open(file_name, "a")
    file.write(str(evaluation) + " " + str(value) + "\n")
    file.close()


def save_checkpoint_file(file_name, evaluation, moead):

    file = open(file_name, "w")
    file.write("eval : " + str(evaluation) + "\n")

    file.write("pop : " + str(len(moead.population)) + "\n")
    file.write(population_to_str(moead.population) + "\n")

    file.write("ep : " + str(len(moead.ep)) + "\n")
    file.write(population_to_str(moead.ep) + "\n")

    file.close()


def population_to_str(population):
    result = ""

    for s in population:
        for bit in s.solution:
            result += str(int(bit)) + ","
        result += "/"

    return result


def save_front_file(file_name, points):
    file = open(file_name, "w")

    for point in points:
        file.write(str(point[0]) + " " + str(point[1]) + "\n")

    file.close()


def compute_hypervolume(solutions, ref_point):
    arr = []
    for s in solutions:
        arr.append(s.F)

    hv = hypervolume(arr)
    return hv.compute(ref_point)
