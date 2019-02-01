import os, sys


def create_folder(path, prefix, counts, mode):
    for i in range(counts):
        os.mkdir(path + '/' + prefix + str(i+1), mode)
        os.name()


if __name__ == '__main__':
    print(os.name())
    # create_folder(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
