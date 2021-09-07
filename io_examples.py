import sys

a = 12.3456789
b = 42

print(a, b)
#                  ' '           '\n'
#  print(str(a) + sep + str(b) + end)

print(a, b, sep="=")
print(a, b, sep="")
print(a, end=' ')
print(b)

print(a, b, file=sys.stderr)

print(a, b, flush=True)

print(a, b, sep=' ', end='\n', file=sys.stdout, flush=False)

print(a)  #  print(str(a) + end)

print(f'{a:.2f}')  # python 3 improved AKA f-strings
print('{:.2f}'.format(a))  # python 3 original
print('%.2f' % (a,))  # python 2 legacy
print(f'A: {a} B: {b}')
print()

for x in 5, 19, 203, 14, 8, 77:
    print(f"{x:4d}")
print()

for x in 5, 19, 203, 14, 8, 77:
    print(f"{x:04d}")
print()

big_number = 29302938502398502392039938953845145987581384
print(f"{big_number:,d}")

value = 12_325_903.393_393

print(value)

status = input("How is class going so far? ")
print(status)








