from Note import Note, notes

def count_interval(note, interval, semitones):

    new_note = Note()
    new_note.degree = (note.degree + interval)
    result = notes[new_note.degree % 7][0]
    semitone_diff = notes[new_note.degree % 7][1] - note.distance
    tmp = new_note.degree
    while tmp >= 7:
        new_note.octave += "'"
        semitone_diff += 12
        tmp -= 7
    while tmp < 0:
        new_note.octave += ","
        semitone_diff -= 12
        tmp += 7

    postfix_cnt = 0
    while semitone_diff > semitones:
        result+="es"
        semitone_diff -= 1
        postfix_cnt += 1
        if postfix_cnt > 2:
            result = notes[(new_note.degree - 1) % 7][0] \
                     + (3 - (notes[new_note.degree % 7][1] - notes[(new_note.degree-1) % 7][1]) % 3)*"es"
            new_note.degree = (new_note.degree - 1)
            #postfix_cnt -= notes[new_note.degree % 7][1] - notes[(new_note.degree-1) % 7][1]
    while semitone_diff < semitones:
        result += "is"
        semitone_diff += 1
        postfix_cnt += 1
        if postfix_cnt > 2:
            result = notes[(new_note.degree + 1) % 7][0] + \
                     (3 - (notes[(new_note.degree + 1) % 7][1] - notes[new_note.degree % 7][1]) % 3) * "is"
            new_note.degree = (new_note.degree + 1)
            #postfix_cnt -= notes[(new_note.degree + 1) % 7][1] - notes[new_note.degree % 7][1]

    new_note.distance = semitone_diff + note.distance
    new_note.pitch = result
    return new_note
