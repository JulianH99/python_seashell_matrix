def main():
    print(step_mat(get_mat()))


def step_mat(mat):
    if len(mat) == 0:
        return []
    return mat[0] + step_mat(transpose_mat(mat[1:]))


def transpose_mat(mat):
    if len(mat) == 0 or mat[0] == []:
        return []
    return last_line(mat) + transpose_mat([f[0:-1] for f in mat])


def last_line(mat):
    if len(mat) == 0 or mat[0] == []:
        return []
    return [[f[len(f) - 1] for f in mat]]


def get_mat():
    return [x.split() for x in open("matrix.txt").readlines()]


if __name__ == '__main__':
    main()
