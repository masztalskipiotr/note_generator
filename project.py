from random import randint, random

class Note:
    time_stamp = 4
    pitch = 'c'


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
}\\new Voice \with { \
  \\remove "Note_heads_engraver" \
  \\consists "Completion_heads_engraver" \
  \\remove "Rest_engraver" \
  \\consists "Completion_rest_engraver" \
}'

all_notes = [' a,,', ' b,,', ' c,,', ' d,,', ' e,,', ' f,,', ' g,,',
             ' a,', ' b,', ' c,', ' d,', ' e,', ' f,', ' g,',
             ' a', ' b', ' c', ' d', ' e', ' f', ' g',
             " a'", " b'", " c'", " d'", " e'", " f'", " g'",
             " a''", " b''", " c''", " d''", " e''", " f''", " g''",
             " a'''", " b'''", " c'''", " d'''", " e'''", " f'''", " g'''"]

notes = all_notes[21:28]  # oktawa razkreślna dla testów
tempo = 5  # 3/4

if tempo == 2:
    rythmic_values = [[2, '2'], [8/3, '4.'], [4, '4'],
                      [16/3, '8.'], [8, '8'], [16, '16']]
elif tempo == 3:
    rythmic_values = [[4/3, '2.'], [2, '2'], [8/3, '4.'], [4, '4'],
                      [16/3, '8.'], [8, '8'], [16, '16']]
elif tempo == 4:
    rythmic_values = [[1, '1'], [4/3, '2.'], [2, '2'], [8/3, '4.'], [4, '4'],
                      [16/3, '8.'], [8, '8'], [16, '16']]
elif tempo == 5:
    rythmic_values = [[1, '1'], [4 / 3, '2.'], [2, '2'], [8 / 3, '4.'], [4, '4'],
                      [16 / 3, '8.'], [8, '8'], [16, '16']]

bar_count = 12
# first_note =
# ambitus =

# TODO: naprawić kod, tak żeby nuty kończyły się dokładnie na ostatnim takcie (ostatnia nuta nie może być dłuższa niż pozostały czas w takcie)

with open('p1.ly', 'w') as file1:
    file1.write(header)
    file1.write("{ \\time %d/4" % tempo)

    full_time = bar_count/(4/tempo)

    while full_time > 0:
        note = Note()
        note.pitch = notes[randint(0, len(notes) - 1)]
        note.time_stamp, time_str = rythmic_values[randint(0, len(rythmic_values) - 1)]
        print(full_time, 1/note.time_stamp)

        if 1/note.time_stamp > full_time:
            note.pitch = ' R'
            time_str = ''

        full_time -= 1/note.time_stamp
        file1.write(note.pitch + time_str)

    file1.write('\\bar "||" }')

