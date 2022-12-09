import uuid

total_sizes = 0
current_directory = None


class Directory:
    def __init__(self, name, directories, upper_directory_id, files, directory_size, new_id):
        self.name = name
        self.directories = directories
        self.upper_directory_id = upper_directory_id
        self.files = files
        self.directory_size = directory_size
        self.id = new_id


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def add_directory_to_directory(directory, subdirectory):
    directory.directories.append(subdirectory)


def create_directory(name, upper_directory_id):
    return Directory(name, [], upper_directory_id, [], 0, uuid.uuid4())


def create_file(name, size):
    return File(name, size)


def get_directory_by_name(directory, name):
    for d in directory.directories:
        if d.name == name:
            global current_directory
            current_directory = d
            return d


def get_directory_by_id(directory, upper_directory_id):
    global current_directory
    if directory.id.int == upper_directory_id.int:
        current_directory = directory
        return directory
    elif len(directory.directories) != 0:
        for direc in directory.directories:
            d = get_directory_by_id(direc, upper_directory_id)
            if d is not None:
                return d
    return None


def print_directory_tree(directory, level=0):
    print(" " * level + directory.name)
    for subdirectory in directory.directories:
        print_directory_tree(subdirectory, level + 1)


def calculate_directory_folder_size(directory):
    global total_sizes
    folder_size = 0
    if len(directory.files) == 0 and len(directory.directories) == 0:
        return 0

    if len(directory.files) != 0:
        for file in directory.files:
            folder_size += int(file.size)

    if len(directory.directories) != 0:
        for d in directory.directories:
            folder_size += d.directory_size
    directory.directory_size = folder_size

    # add to total_sizes if folder_size is smaller than 100000
    if folder_size <= 100000:
        total_sizes += folder_size
    return folder_size


def recursive_directory_size_calculation(directory):
    for d in directory.directories:
        recursive_directory_size_calculation(d)
        calculate_directory_folder_size(d)
    return


def main():
    global current_directory
    with open("input.txt", "r") as f:
        lines = f.readlines()

    initial_directory = create_directory("root", None)
    current_directory = initial_directory

    for line in lines:
        line_elements = line.split(" ")
        first_argument = line_elements[0].strip()
        second_argument = line_elements[1].strip()
        third_argument = line_elements[2].strip() if len(line_elements) > 2 else None

        if first_argument == "$" and second_argument == "cd" and third_argument != "/" and third_argument != "..":
            get_directory_by_name(current_directory, third_argument)
        elif first_argument == "$" and second_argument == "cd" and third_argument == "..":
            get_directory_by_id(initial_directory, current_directory.upper_directory_id)
        elif first_argument == "dir":
            new_directory = create_directory(second_argument, current_directory.id)
            add_directory_to_directory(current_directory, new_directory)
        elif first_argument != "$":
            new_file = create_file(second_argument, first_argument)
            current_directory.files.append(new_file)

    # print_directory_tree(initial_directory)
    recursive_directory_size_calculation(initial_directory)
    print(total_sizes)


main()
