import pickle


try:
    with open('man_file_pickle.txt', 'wb') as man_file, open('man_file.txt') as date:
        pickle.dump(date.readline(), man_file)
    with open('man_file_pickle.txt', 'rb') as man_file_restore:
        output = pickle.load(man_file_restore)
        print(output)
except IOError as io_err:
    print('File error.' + str(io_err))
except pickle.PickleError as pickle_err:
    pickle('pickle error:', pickle_err)
