""" configuration file """

tempo = 5  # 3/4
first_note = "c'" # in lilypond notation
first_note_time_stamp = 16 # in lilypond notation
lowest_note = "c"
highest_note = "c''"
bar_count = 12


""" below it is possible to set probability of particular intervals and pitches """
""" you can choose whether intervals or pitches should be a priority by setting i and p parameters """
""" pitches priority set to 0 means that its probability values are not taken into account while generating """
""" when i and p are equal, both interval and pitches probabilities are considered which means that """
""" the most likely event would be very likely interval ending on very likely pitch """
""" you can play with i/p ratio to achieve desired effect """

""" intervals priority """
i = 1

""" pitches priority """
p = 1


""" specify intervals probabilty """
""" unison = i;     fifth = 2*i     means fifth are two times more likely than unison """

unison =      i
dim_second =  i
aug_unison =  i
min_second =  i
maj_second =  i
dim_third =   i
aug_second =  i
min_third =   i
maj_third =   10*i
dim_fourth =  i
aug_third =   i
fourth =      i
aug_fourth =  i
dim_fifth =   i
fifth =       50*i
dim_sixth =   i
aug_fifth =   i
min_sixth =   i
maj_sixth =   i
dim_seventh = i
aug_sixth =   i
min_seventh = i
maj_seventh = i
dim_octave =  i
aug_seventh = i
octave =      i


""" specify pitches probabilty """
""" c = p;  g = 2*p     means g is two times more likely than c """

c =   p
cis = p
d =   p
dis = p
e =   p
f =   100*p
fis = p
g =   p
gis = p
a =   p
ais = p
b =   p
