import datetime


def file_interaction(filename, filemode, list_of_additions):
    if filemode == "r":
        try:
            with open(filename, "r") as file:
                return file.readlines()
        except Exception as error_message:
            print(f'Something went wrong when trying to open and read {filename}:\n{error_message}')
    elif filemode == "a":
        try:
            with open(filename, "a") as file:
                for elem in list_of_additions:
                    file.write(elem)
        except Exception as error_message:
            print(f'Something went wrong when trying to open and append {filename}:\n{error_message}')

    elif filemode == "w":
        try:
            with open(filename, "w") as file:
                for elem in list_of_additions:
                    file.write(elem)
        except Exception as error_message:
            print(f'Something went wrong when trying to open and write {filename}:\n{error_message}')

    else:
        print(f'The file mode you entered is "{filemode}".'
              f'\nPlease enter try again and enter "r", "a", or "w".')
    return None


def start_time(filename):
    now = datetime.datetime.now()
    result = f'start {now}\n'
    list_of_additions = [result]
    file_interaction(filename, "a", list_of_additions)


def stop_time(filename):
    now = datetime.datetime.now()
    result = "stop " f'{now}\n'
    list_of_file_additions = [result]

    list_file_lines = file_interaction(filename, "r", [])
    most_recent_start = ""
    for line in list_file_lines[::-1]:
        list_for_line = line.split(" ")
        if "start" in list_for_line:
            most_recent_start = f'{list_for_line[1]} {list_for_line[2]}'.replace("\n", "")
            break
    if most_recent_start != "":
        duration = now - datetime.datetime.fromisoformat(most_recent_start)
        list_of_file_additions.append(f'duration {duration}\n')
    file_interaction(filename, "a", list_of_file_additions)