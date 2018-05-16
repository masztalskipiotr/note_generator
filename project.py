from random import randint, random

class Note:
    time_stamp = 4
    pitch = 'c'
    pass


header = '\\version "2.18.2" \
\paper {\
  #(set-paper-size "a4landscape") \
  print-all-headers = ##t \
} \
\layout{ \
  indent = 0\in \
  ragged-last = ##f \
  \context { \
    \Score \
  } \
}'

tempo = 4
bar_count = 12
# first_note =
# ambitus =

with open('p1.ly', 'w') as file1:
    file1.write(header)
    file1.write("\\relative c' { \\time %d/4" % tempo)
    for i in range(0, bar_count):
        while bar_count > 0:
            bar_count -= 1/16
            file1.write(' c16 ')
    file1.write('}')

