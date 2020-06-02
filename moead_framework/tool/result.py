import numpy as np


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


def save_population_and_solution(file_name, population):
    file = open(file_name, "w")
    # file.write("Length of the list = " + str(len(population)) + "\n")
    for s in population:
        row = ""
        x = ""
        for coordinate in s.F:
            row += str(coordinate) + " "

        row += str(s.solution)

        row = row + "\n"
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
    hypervolume_class = HyperVolume(reference_point=ref_point)

    x = []
    for s in solutions:
        x.append(s.F[:])

    return hypervolume_class.compute(solutions=np.array(x))


class HyperVolume:
    """
    Code from https://github.com/jMetal/jMetalPy/blob/master/jmetal/core/quality_indicator.py

    Hypervolume computation based on variant 3 of the algorithm in the paper:
    * C. M. Fonseca, L. Paquete, and M. Lopez-Ibanez. An improved dimension-sweep
      algorithm for the hypervolume indicator. In IEEE Congress on Evolutionary
      Computation, pages 1157-1163, Vancouver, Canada, July 2006.
    Minimization is implicitly assumed here!
    """

    def __init__(self, reference_point: [float] = None):
        self.referencePoint = reference_point
        self.list: MultiList = []

    def compute(self, solutions: np.array):
        """Before the HV computation, front and reference point are translated, so that the reference point is [0, ..., 0].
        :return: The hypervolume that is dominated by a non-dominated front.
        """
        front = solutions

        def weakly_dominates(point, other):
            for i in range(len(point)):
                if point[i] > other[i]:
                    return False
            return True

        relevant_points = []
        reference_point = self.referencePoint
        dimensions = len(reference_point)
        for point in front:
            # only consider points that dominate the reference point
            if weakly_dominates(point, reference_point):
                relevant_points.append(point)
        if any(reference_point):
            # shift points so that reference_point == [0, ..., 0]
            # this way the reference point doesn't have to be explicitly used
            # in the HV computation
            for j in range(len(relevant_points)):
                relevant_points[j] = [relevant_points[j][i] - reference_point[i] for i in range(dimensions)]
        self._pre_process(relevant_points)
        bounds = [-1.0e308] * dimensions

        return self._hv_recursive(dimensions - 1, len(relevant_points), bounds)

    def _hv_recursive(self, dim_index: int, length: int, bounds: list):
        """Recursive call to hypervolume calculation.
        In contrast to the paper, the code assumes that the reference point
        is [0, ..., 0]. This allows the avoidance of a few operations.
        """
        hvol = 0.0
        sentinel = self.list.sentinel
        if length == 0:
            return hvol
        elif dim_index == 0:
            # special case: only one dimension
            # why using hypervolume at all?
            return -sentinel.next[0].cargo[0]
        elif dim_index == 1:
            # special case: two dimensions, end recursion
            q = sentinel.next[1]
            h = q.cargo[0]
            p = q.next[1]
            while p is not sentinel:
                p_cargo = p.cargo
                hvol += h * (q.cargo[1] - p_cargo[1])
                if p_cargo[0] < h:
                    h = p_cargo[0]
                q = p
                p = q.next[1]
            hvol += h * q.cargo[1]
            return hvol
        else:
            remove = self.list.remove
            reinsert = self.list.reinsert
            hv_recursive = self._hv_recursive
            p = sentinel
            q = p.prev[dim_index]
            while q.cargo is not None:
                if q.ignore < dim_index:
                    q.ignore = 0
                q = q.prev[dim_index]
            q = p.prev[dim_index]
            while length > 1 and (
                    q.cargo[dim_index] > bounds[dim_index] or q.prev[dim_index].cargo[dim_index] >= bounds[dim_index]):
                p = q
                remove(p, dim_index, bounds)
                q = p.prev[dim_index]
                length -= 1
            q_area = q.area
            q_cargo = q.cargo
            q_prev_dim_index = q.prev[dim_index]
            if length > 1:
                hvol = q_prev_dim_index.volume[dim_index] + q_prev_dim_index.area[dim_index] * (
                        q_cargo[dim_index] - q_prev_dim_index.cargo[dim_index])
            else:
                q_area[0] = 1
                q_area[1:dim_index + 1] = [q_area[i] * -q_cargo[i] for i in range(dim_index)]
            q.volume[dim_index] = hvol
            if q.ignore >= dim_index:
                q_area[dim_index] = q_prev_dim_index.area[dim_index]
            else:
                q_area[dim_index] = hv_recursive(dim_index - 1, length, bounds)
                if q_area[dim_index] <= q_prev_dim_index.area[dim_index]:
                    q.ignore = dim_index
            while p is not sentinel:
                p_cargo_dim_index = p.cargo[dim_index]
                hvol += q.area[dim_index] * (p_cargo_dim_index - q.cargo[dim_index])
                bounds[dim_index] = p_cargo_dim_index
                reinsert(p, dim_index, bounds)
                length += 1
                q = p
                p = p.next[dim_index]
                q.volume[dim_index] = hvol
                if q.ignore >= dim_index:
                    q.area[dim_index] = q.prev[dim_index].area[dim_index]
                else:
                    q.area[dim_index] = hv_recursive(dim_index - 1, length, bounds)
                    if q.area[dim_index] <= q.prev[dim_index].area[dim_index]:
                        q.ignore = dim_index
            hvol -= q.area[dim_index] * q.cargo[dim_index]
            return hvol

    def _pre_process(self, front):
        """Sets up the list front structure needed for calculation."""
        dimensions = len(self.referencePoint)
        node_list = MultiList(dimensions)
        nodes = [MultiList.Node(dimensions, point) for point in front]
        for i in range(dimensions):
            self._sort_by_dimension(nodes, i)
            node_list.extend(nodes, i)
        self.list = node_list

    def _sort_by_dimension(self, nodes, i):
        """Sorts the list of nodes by the i-th value of the contained points."""
        # build a list of tuples of (point[i], node)
        decorated = [(node.cargo[i], node) for node in nodes]
        # sort by this value
        decorated.sort(key=lambda n: n[0])
        # write back to original list
        nodes[:] = [node for (_, node) in decorated]

    def get_short_name(self) -> str:
        return 'HV'

    def get_name(self) -> str:
        return "Hypervolume (Fonseca et al. implementation)"


class MultiList:
    """A special front structure needed by FonsecaHyperVolume.
    It consists of several doubly linked lists that share common nodes. So,
    every node has multiple predecessors and successors, one in every list.
    """

    class Node:

        def __init__(self, number_lists, cargo=None):
            self.cargo = cargo
            self.next = [None] * number_lists
            self.prev = [None] * number_lists
            self.ignore = 0
            self.area = [0.0] * number_lists
            self.volume = [0.0] * number_lists

        def __str__(self):
            return str(self.cargo)

    def __init__(self, number_lists):
        """ Builds 'numberLists' doubly linked lists.
        """
        self.number_lists = number_lists
        self.sentinel = MultiList.Node(number_lists)
        self.sentinel.next = [self.sentinel] * number_lists
        self.sentinel.prev = [self.sentinel] * number_lists

    def __str__(self):
        strings = []
        for i in range(self.number_lists):
            current_list = []
            node = self.sentinel.next[i]
            while node != self.sentinel:
                current_list.append(str(node))
                node = node.next[i]
            strings.append(str(current_list))
        string_repr = ""
        for string in strings:
            string_repr += string + "\n"
        return string_repr

    def __len__(self):
        """Returns the number of lists that are included in this MultiList."""
        return self.number_lists

    def get_length(self, i):
        """Returns the length of the i-th list."""
        length = 0
        sentinel = self.sentinel
        node = sentinel.next[i]
        while node != sentinel:
            length += 1
            node = node.next[i]
        return length

    def append(self, node, index):
        """ Appends a node to the end of the list at the given index."""
        last_but_one = self.sentinel.prev[index]
        node.next[index] = self.sentinel
        node.prev[index] = last_but_one
        # set the last element as the new one
        self.sentinel.prev[index] = node
        last_but_one.next[index] = node

    def extend(self, nodes, index):
        """ Extends the list at the given index with the nodes."""
        sentinel = self.sentinel
        for node in nodes:
            last_but_one = sentinel.prev[index]
            node.next[index] = sentinel
            node.prev[index] = last_but_one
            # set the last element as the new one
            sentinel.prev[index] = node
            last_but_one.next[index] = node

    def remove(self, node, index, bounds):
        """ Removes and returns 'node' from all lists in [0, 'index'[."""
        for i in range(index):
            predecessor = node.prev[i]
            successor = node.next[i]
            predecessor.next[i] = successor
            successor.prev[i] = predecessor
            if bounds[i] > node.cargo[i]:
                bounds[i] = node.cargo[i]
        return node

    def reinsert(self, node, index, bounds):
        """ Inserts 'node' at the position it had in all lists in [0, 'index'[
        before it was removed. This method assumes that the next and previous
        nodes of the node that is reinserted are in the list.
        """
        for i in range(index):
            node.prev[i].next[i] = node
            node.next[i].prev[i] = node
            if bounds[i] > node.cargo[i]:
                bounds[i] = node.cargo[i]