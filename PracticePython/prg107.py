#write a program to get parent folder of current directory
from pathlib import Path
p = Path('kumar.txt')
print(p.parent)
print(p.parent.parent)

print(p.name)
print(p.as_posix())
print(p.stat())

print(p.is_dir())
print(p.is_file())

