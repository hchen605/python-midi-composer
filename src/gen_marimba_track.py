import random
import pandas_test as pt
#import smooth

def gen_marimba_track(track, beat, note_last, chord, mode, vel, first_beat, third_beat, onset, key):

    import midi
    
    
    #note
    note = pt.gen_next_note(note_last, mode)
    note_key = note + key
    prob = random.random()
    if prob > onset:
        on = midi.NoteOnEvent(tick = beat, velocity = vel, pitch = note_key)
        track.append(on)
    else:
        off = midi.NoteOnEvent(tick = beat, velocity = 0, pitch = note_key)
        track.append(off)




#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

