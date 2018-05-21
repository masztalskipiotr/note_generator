import config
from config import first_note, first_note_time_stamp

notes = [["c", 0], ["d", 2], ["e", 4], ["f", 5], ["g", 7], ["a",9], ["b",11]]

class Note:
    def __init__(self):
        self.time_stamp = config.first_note_time_stamp
        self.pitch = config.first_note
        self.degree = count_degree(config.first_note)
        self.distance = count_distance(self)
        self.octave = ""

def count_degree(first_note):
    for idx, el in enumerate(notes):
        if first_note[:1] == notes[idx][0]:
            degree = idx
            break
    for char in first_note[1:]:
        if char == "'": degree += 7
        if char == ",": degree -= 7
    return degree


def count_distance(note):
    distance = notes[note.degree % 7][1]
    for char in note.pitch[1:]:
        if char == "'": distance += 12
        if char == ",": distance -= 12
    return distance

def lower_octave(note):
    for char in note.octave:
        if char == "'":
            return note.octave[:-1]
    return note.octave + ","

def raise_octave(note):
    for char in note.octave:
        if char == ",":
            return note.octave[:-1]
    return note.octave + "'"