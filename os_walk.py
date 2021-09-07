import os

DIRS_TO_SKIP = ['.git', '.idea']

def main():
    start_folder = "."

    #  folder_name, dir_list, file_list
    for folder_name, dir_list, file_list in os.walk(start_folder):
        for folder in DIRS_TO_SKIP:
            if folder in dir_list:
                dir_list.remove(folder)

        print(folder_name)
        for file_name in file_list:
            if file_name.endswith('.py'):
                file_path = os.path.join(folder_name, file_name)
                file_size = os.path.getsize(file_path)
                print(f"    {file_size:6d} {file_name}")


if __name__ == '__main__':
    main()
