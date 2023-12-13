

def gen_drum_bossa_track(track, beat, not_first_note, vel, enable, last):

    import midi
    #drum
    HH = 51
    SS = 37
    SD = 38
    BD = 35
    LT = 41
    HT = 48
    
    v = vel * enable
    v_end = vel

    if not last:
        on = midi.NoteOnEvent(tick = int(beat/2*not_first_note), velocity = v, channel=9, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v, channel=9, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v, channel=9, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v, channel=9, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v, channel=9, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v, channel=9, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v, channel=9, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v, channel=9, pitch = HH)
        track.append(on)
    else:
        #on = midi.NoteOnEvent(tick = beat*3/2, velocity = 0, pitch = HH)
        #track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v_end, channel=9, pitch = SS)
        track.append(on)
        on = midi.NoteOnEvent(tick = 0, velocity = v_end, channel=9, pitch = LT)
        track.append(on)
        on = midi.NoteOnEvent(tick = 0, velocity = v_end, channel=9, pitch = BD)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat*3/2), velocity = v_end, channel=9, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/8), velocity = v_end, channel=9, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/8), velocity = 0, channel=9, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/8), velocity = v_end, channel=9, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/8), velocity = 0, channel=9, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/7), velocity = v_end, channel=9, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/7), velocity = 0, channel=9, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/6), velocity = v_end, channel=9, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/6), velocity = 0, channel=9, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/5), velocity = v_end, channel=9, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/5), velocity = 0, channel=9, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/4), velocity = v_end, channel=9, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/4), velocity = 0, channel=9, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/3), velocity = v_end, channel=9, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/3), velocity = 0, channel=9, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/2), velocity = v_end, channel=9, pitch = HH)
        track.append(on)




    


#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

