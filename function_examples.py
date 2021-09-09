
def filter_words_by_first_letter(letter):
    words = []
    with open('DATA/words.txt') as words_in:
        for line in words_in:
            if line[0] == letter:
                words.append(line.rstrip())
    return words

a_words = filter_words_by_first_letter('a')
b_words = filter_words_by_first_letter('b')

print(len(a_words), len(b_words))

def spam():
    print("Hello there!")

x = spam()
print(x)


def count_lines(s, *file_paths):
    count = 0
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if s in line:
                    count += 1
    return count

print(count_lines('pig', 'DATA/alice.txt'))
print(count_lines('pig', 'DATA/alice.txt', 'DATA/words.txt'))
print(count_lines('Alice', 'DATA/alice.txt'))
print(count_lines('bird', 'DATA/alice.txt', 'DATA/words.txt',
                  'DATA/parrot.txt'))


def config(**options):
    print(options)

config(file_name='DATA/alice.txt', text='pig', print_lines=True)

def count_lines2(*, file_name, text, print_lines=False):
    print(file_name, text, print_lines)

count_lines2(text="burger", file_name="DATA/words.txt")


def wacky(p1, p2, *p3, p4, p5, **p6):
    print("p1: {}\n".format(p1))
    print("p2: {}\n".format(p2))
    print("p3: {}\n".format(p3))
    print("p4: {}\n".format(p4))
    print("p5: {}\n".format(p5))
    print("p6: {}\n".format(p6))
    print()

wacky(1, 2, p4='a', p5='b')
wacky(1, 2, 3, 4, 5, 6, color='red',
      size='xxl', p4='a', p5='b')


def count_lines3(text, *file_names, print_lines=False):
    pass

count_lines3('bird', 'some_file')
count_lines3('bird', 'file1', 'file2', 'file3', print_lines=True)


def foo(a, b):
    return a + b

print(foo(10, 5))
print(foo(b=8, a=9))



