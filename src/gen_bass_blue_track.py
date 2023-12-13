

def gen_bass_blue_track(track, beat, chord, vel, chord_cnt, note_cnt, ending, key):

    import midi

    if chord_cnt % 2 == 0:
        bass_cnt = [0,1,2,3]
    else:
        bass_cnt = [4,3,2,1]
        
    beat_cnt = int(note_cnt / 2)
    #note
    bass_note = chord[bass_cnt[beat_cnt]] - 12 + key
    
    vel = vel * (ending == 0)
    
    on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = bass_note)
    track.append(on)
    off = midi.NoteOffEvent(tick = beat, velocity = vel, pitch = bass_note)
    track.append(off)
    


#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

