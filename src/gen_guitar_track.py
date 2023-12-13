import random
#import pandas_test as pt
#import smooth

def gen_guitar_track(track, beat, note_last, chord, mode, vel, first_beat, third_beat, onset, key):

    import midi
    
    toss = random.random()
    if toss < 0.5:
        guitar_note = chord[0] + 12
    elif toss < 0.8:
        guitar_note = chord[1] + 12
    else:
        guitar_note = chord[2] + 12
    #note
    guitar_note_key = guitar_note + key
    prob = random.random()
    if prob > onset:
        #note = pt.gen_next_note(note_last, mode)
        on = midi.NoteOnEvent(tick = beat, velocity = vel, pitch = guitar_note_key)
        track.append(on)
    else:
        off = midi.NoteOnEvent(tick = beat, velocity = 0, pitch = guitar_note_key)
        track.append(off)




#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

