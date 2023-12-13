

def gen_string_track_full(track, beat, chord, vel, enable, last, key):

    import midi
    import random

    
    v = vel * enable
    if last:
        dur = 6
    else:
        dur = 4
    #note
    toss = random.random()
    if toss < 0.6:
        string_note = chord[0] + 12
    elif toss < 0.8:
        string_note = chord[1] + 12
    else:
        string_note = chord[2] + 12
    
    string_note_key = string_note + key
    on = midi.NoteOnEvent(tick = 0, velocity = v, pitch = string_note_key)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = v, pitch = string_note_key)
    track.append(off)
    on = midi.NoteOnEvent(tick = 0, velocity = v, pitch = string_note_key)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = v, pitch = string_note_key)
    track.append(off)
    on = midi.NoteOnEvent(tick = 0, velocity = v, pitch = string_note_key)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = v, pitch = string_note_key)
    track.append(off)
    on = midi.NoteOnEvent(tick = 0, velocity = v, pitch = string_note_key)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = v, pitch = string_note_key)
    track.append(off)
    
#bass_last = bass_note


#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

