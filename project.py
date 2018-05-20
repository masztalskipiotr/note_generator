from random import randint, random

class Note:
    time_stamp = 4
    pitch = " c"
    degree = 0; #notes[0] = " c"
    distance = 0;

def count_interval(note, interval, semitones):
    #TODO create Interval class or struct and pass it to function instead of interval degree and semitones
    new_note = Note()
    new_note.degree = note.degree + interval - 1
    if new_note.degree > len(notes):
        new_note.degree = note.degree - interval + 1 #if exceeds one octave, goes down
        semitones = 0 - semitones
    result = notes[new_note.degree][0]
    semitone_diff = notes[new_note.degree][1] - note.distance

    while semitone_diff > semitones:
        result+="es"
        semitone_diff -= 1
    while semitone_diff < semitones:
        result += "is"
        semitone_diff += 1
    new_note.distance = semitone_diff + note.distance
    new_note.pitch = result
    return new_note

header = \
'\\version "2.18.2" \n\
\paper {\n\
#(set-paper-size "a4landscape") \n\
print-all-headers = ##t \n\
} \n\
\layout{ \n\
  indent = 0\in \n\
  ragged-last = ##f \n\
  \context { \n\
    \Score \n\
  } \n\
}\\new Voice \with { \n\
  \\remove "Note_heads_engraver" \n\
  \\consists "Completion_heads_engraver" \n\
  \\remove "Rest_engraver" \n\
  \\consists "Completion_rest_engraver" \n\
}\n'

notes = [[" c", 0], [" d", 2], [" e", 4], [" f", 5], [" g", 7], [" a",9], [" b",11]]
#TODO reconsider lower and upper octaves
tempo = 3  # 3/4

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

random_mode = False
bar_count = 12
first_note = ' c'
# ambitus =

rest_prob = 0.1  # prawdopodobieństwo wystąpienia pauzy

# prawdopodobieństwa wystąpienia poszczególnych interwałów
#TODO WTF create reasonable struct
unison_prob = 0
diminished_second_prob = 0
augmented_unison_prob = 0
minor_second_prob = 0
major_second_prob = 0
diminished_third_prob = 0
augmented_second_prob = 0
minor_third_prob = 0
major_third_prob = 0
diminished_fourth_prob = 0
augmented_third_prob = 0
fourth_prob = 0
augmented_fourth_prob = 0
diminished_fifth_prob = 0
fifth_prob = 0
diminished_sixth_prob = 0
augmented_fifth_prob = 0
minor_sixth_prob = 0
major_sixth_prob = 0
diminished_seventh_prob = 0
augmented_sixth_prob = 0
minor_seventh_prob = 0
major_seventh_prob = 0
diminished_octave_prob = 0
augmented_seventh_prob = 0
octave_prob = 0

with open('p1.ly', 'w') as file1:
    file1.write(header)
    file1.write("{ \\relative c' { \\time %d/4" % tempo)

    full_time = bar_count/(4/tempo)
    if random_mode==True:
        while full_time > 0:
            note = Note()
            rest_rand = random()

            if rest_rand <= rest_prob:
                note.pitch = 'r '
            else:
                note.degree = randint(0, len(notes) - 1)
                note.pitch = notes[note.degree][0]

            ind = randint(0, len(rythmic_values) - 1)
            note.time_stamp, time_str = rythmic_values[ind]

            while 1/note.time_stamp > full_time:
                ind += 1
                note.time_stamp, time_str = rythmic_values[ind]

            full_time -= 1/note.time_stamp
            file1.write(note.pitch + time_str)
    else:
        note = Note()
        note.pitch = first_note
        file1.write(note.pitch)
        while full_time > 0:
            note = count_interval(note, 3, 3) #just minor third for test
            ind = randint(0, len(rythmic_values) - 1)
            note.time_stamp, time_str = rythmic_values[ind]

            while 1 / note.time_stamp > full_time:
                ind += 1
                note.time_stamp, time_str = rythmic_values[ind]

            full_time -= 1 / note.time_stamp
            file1.write(note.pitch + time_str)

    file1.write('\\bar "||" } }')

