

def gen_bass_bossa_track(track, beat, chord, vel, last, key):

    import midi

    
    #note
    bass_note_1 = chord[0] - 12 + key
    bass_note_2 = chord[2] - 24 + key
    
    if not last:
        on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note_1)
        track.append(on)
        off = midi.NoteOffEvent(tick = int(beat * 3/2), velocity = vel, pitch = bass_note_1)
        track.append(off)
        on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note_1)
        track.append(on)
        off = midi.NoteOffEvent(tick = int(beat/2), velocity = vel, pitch = bass_note_1)
        track.append(off)
        
        
        on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note_2)
        track.append(on)
        off = midi.NoteOffEvent(tick = int(beat * 3/2), velocity = vel, pitch = bass_note_2)
        track.append(off)
        on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note_2)
        track.append(on)
        off = midi.NoteOffEvent(tick = int(beat/2), velocity = vel, pitch = bass_note_2)
        track.append(off)
    else:
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = bass_note_2)
        track.append(on)
        off = midi.NoteOffEvent(tick = int(beat/2), velocity = vel, pitch = bass_note_2)
        track.append(off)
        on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note_1)
        track.append(on)
        off = midi.NoteOffEvent(tick = beat*2, velocity = vel, pitch = bass_note_1)
        track.append(off)
    
    #bass_last = bass_note


#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

