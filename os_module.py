import os

print(os.getcwd())
print(os.getuid())
print(os.getpid())
print(os.getlogin())

print(os.listdir('DATA'), '\n')
print(os.listdir('SETUP'), '\n')

os.mkdir('wombat')  # make a dir

print(os.stat('DATA/alice.txt'), '\n')


