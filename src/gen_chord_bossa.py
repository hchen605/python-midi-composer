import midi

def gen_chord_bossa(track, chord, key, short):

    on = midi.NoteOnEvent(tick = 0, velocity = 50, pitch = chord[1] + key)
    track.append(on)
    on = midi.NoteOnEvent(tick = 0, velocity = 50, pitch = chord[2] + key)
    track.append(on)
    on = midi.NoteOnEvent(tick = 0, velocity = 50, pitch = chord[3] + key)
    track.append(on)
    on = midi.NoteOnEvent(tick = 0, velocity = 50, pitch = chord[4] + key)
    track.append(on)
    
    if short:
        off = midi.NoteOnEvent(tick = 50, velocity = 0, pitch = chord[0] + key)
        track.append(off)
        off = midi.NoteOnEvent(tick = 0, velocity = 0, pitch = chord[1] + key)
        track.append(off)
        on = midi.NoteOnEvent(tick = 0, velocity = 0, pitch = chord[3] + key)
        track.append(off)
        off = midi.NoteOnEvent(tick = 0, velocity = 0, pitch = chord[4] + key)
        track.append(off)
    