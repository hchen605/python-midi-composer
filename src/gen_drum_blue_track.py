import random as rand

def gen_drum_blue_track(track, beat, vel, first_beat, third_beat, enable, note_cnt, ending, last):

    import midi
    #drum
    HH = 51
    SS = 37
    SD = 38
    BD = 35
    LT = 41
    HT = 48
    
    #int(beat_cnt = note_cnt / 2
    v = vel * enable * (ending == 0)
    v_end = vel
    prob1 = rand.random()
    prob2 = rand.random()
    

    if note_cnt == 3:
        if prob1 > 0.25:
            on = midi.NoteOnEvent(tick = int(beat), velocity = v, channel=9, pitch = SD)
            track.append(on)
        else:
            off = midi.NoteOffEvent(tick = int(beat), velocity = v, channel=9, pitch = SD)
            track.append(off)
    elif note_cnt == 7:
        if prob2 > 0.3:
            on = midi.NoteOnEvent(tick = int(beat), velocity = v, channel=9, pitch = SS)
            track.append(on)
        else:
            off = midi.NoteOffEvent(tick = int(beat), velocity = v, channel=9, pitch = SS)
            track.append(off)
    elif note_cnt%2 and note_cnt != 3 and note_cnt != 7:
        on = midi.NoteOnEvent(tick = int(beat), velocity = 0, channel=9, pitch = HH)
        track.append(on)
    else:
        on = midi.NoteOnEvent(tick = int(beat), velocity = v, channel=9, pitch = HH)
        track.append(on)
    
    if last:
        on = midi.NoteOnEvent(tick = int(beat), velocity = 0, pitch = HH)
        track.append(on)
        on = midi.NoteOnEvent(tick = int(beat/8), velocity = v_end, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/8), velocity = 0, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/8), velocity = v_end, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/8), velocity = 0, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/7), velocity = v_end, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/7), velocity = 0, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/6), velocity = v_end, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/6), velocity = 0, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/5), velocity = v_end, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/5), velocity = 0, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/4), velocity = v_end, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/4), velocity = 0, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat/3), velocity = v_end, pitch = HH)
        track.append(on)
        off = midi.NoteOnEvent(tick = int(beat/3), velocity = 0, pitch = HH)
        track.append(off)
        on = midi.NoteOnEvent(tick = int(beat), velocity = v_end, pitch = HH)
        track.append(on)
        
    
        #on = midi.NoteOnEvent(tick = int(beat, velocity = 50, pitch = HH)
#track.append(on)


#off = midi.NoteOffEvent(tick = int(beat+int(beat, velocity = 80, pitch = note)
#piano_track.append(off)

# 1---1---1---1