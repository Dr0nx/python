from itertools import count
from itertools import cycle

for el in count(3):
    if el > 7:
        break
    else:
        print(el)

text = ['один', 'два', 'три']
it = cycle(text)

for c in range(0, 6):
    print(next(it))


