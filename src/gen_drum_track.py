

def gen_drum_track(track, beat, vel, first_beat, third_beat, enable):

    import midi
    #drum
    HH = 51
    SS = 37
    SD = 38
    BD = 35
    LT = 41
    HT = 48
    
    v = vel * enable

    if first_beat:
        on = midi.NoteOnEvent(tick = beat, velocity = v, channel=9, pitch = BD)
        track.append(on)
    elif third_beat:
        on = midi.NoteOnEvent(tick = beat, velocity = v, channel=9, pitch = SD)
        track.append(on)
    else:
        on = midi.NoteOnEvent(tick = beat, velocity = v, channel=9, pitch = HH)
        track.append(on)
        #on = midi.NoteOnEvent(tick = beat/2, velocity = 50, pitch = HH)
#track.append(on)


#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

