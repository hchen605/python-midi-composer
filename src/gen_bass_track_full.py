

def gen_bass_track_full(track, beat, chord, vel, key):

    import midi

    
    #note
    bass_note = chord[0] - 12 + key
    
    on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = vel, pitch = bass_note)
    track.append(off)
    on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = vel, pitch = bass_note)
    track.append(off)
    on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = vel, pitch = bass_note)
    track.append(off)
    on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = vel, pitch = bass_note)
    track.append(off)
    #bass_last = bass_note


#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

