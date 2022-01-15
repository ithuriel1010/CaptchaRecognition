import os

path = './data/train/'

files = os.listdir(path)
files_no_ext = [".".join(f.split(".")[:-1]) for f in os.listdir(path)]
print(files)

x = []

for f in files:
    print(f)
    x.append(".".join(f.split(".")[:-1]))



print(files_no_ext)
print(x)