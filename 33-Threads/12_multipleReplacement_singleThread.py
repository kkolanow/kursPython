from time import perf_counter


def replace(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    # get the contents of the file
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)


def main():
    filenames = [
        'C:/tmp/thread/test1.txt',
        'c:/tmp/thread/test2.txt',
        'c:/tmp/thread/test3.txt',
        'c:/tmp/thread/test4.txt',
        'c:/tmp/thread/test5.txt',
        'c:/tmp/thread/test6.txt',
        'c:/tmp/thread/test7.txt',
        'c:/tmp/thread/test8.txt',
        'c:/tmp/thread/test9.txt',
        'c:/tmp/thread/test10.txt',
    ]

    for filename in filenames:
        replace(filename, 'ids', 'id')


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time- start_time } second(s) to complete.')
