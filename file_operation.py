from datetime import datetime
import pickle
import os


def file_read(target_file):
    with open(target_file, 'rb') as f:
        return pickle.load(f)


def file_write(target_file):
    current_time = datetime.now()
    with open(target_file, 'wb') as f:
        pickle.dump(current_time, f)


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    target_file = current_path + '/test_file'

    file_write(target_file)
    now = file_read(target_file)
    print(str(now))
