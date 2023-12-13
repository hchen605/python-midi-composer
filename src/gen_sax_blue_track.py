import random as rand
import pandas_test as pt
import smooth


def gen_sax_blue_track(track, beat, scale, note_last, chord, mode, vel, first_beat, third_beat, onset, sm, grace_flag, cadence, last, note_cnt, solo, key):

    import midi

    sm_th = 9
    grace_prob_1 = 0.6
    grace_prob_2 = 0.7
    #grace_prob_1 = 1
    #grace_prob_2 = 1
    grace_tick = 50

    done = 0
    
    onset_stop = 0.8
    
    #if cadence:
    #beat = beat + 10

    #chord = chord + 12
    #chord = [x+12 for x in chord]
    #note
    prob = rand.random()
    prob_stop = rand.random()

    if first_beat:
        note_pre = scale
    else:
        note_pre = note_last
    
    vel = vel * solo
   
    
    
    if last:
        prob = 0
    if prob > onset: 
        note = pt.gen_next_note(note_pre,mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_key = note + key
        note_last_key = note_last + key
        '''if note < 30:
            note = note + 12'''
        grace = rand.random()
        if grace_flag == 1:
            on = midi.NoteOnEvent(tick = beat - grace_tick, velocity = vel, pitch = note_key)
            track.append(on)
            off = midi.NoteOnEvent(tick = 0, velocity = 0, pitch = note_last_key)
            track.append(off)
            grace_flag = 0
            done = 1
    
        if ((grace > grace_prob_1 and first_beat) or (grace > grace_prob_2 and third_beat)) and (done == 0):
            on = midi.NoteOnEvent(tick = beat, velocity = vel, pitch = note_key - 1)
            track.append(on)
            off = midi.NoteOnEvent(tick = 0, velocity = 0, pitch = note_last_key)
            track.append(off)
            
            off = midi.NoteOffEvent(tick = grace_tick, velocity = vel, pitch = note_key - 1)
            track.append(off)
            on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = note_key)
            track.append(on)
            grace_flag = 1
            done = 1

        if (done == 0):
            on = midi.NoteOnEvent(tick = beat, velocity = vel, pitch = note_key)
            track.append(on)
            off = midi.NoteOnEvent(tick = 0, velocity = 0, pitch = note_last_key)
            track.append(off)
       
    else:
        note = note_last
        note_key = note + key
        note_last_key = note_last + key
        if grace_flag == 1:
            off = midi.NoteOnEvent(tick = beat - grace_tick, velocity = 0, pitch = 1)
            track.append(off)
            grace_flag = 0
            note = note_last
        elif last:
            off = midi.NoteOnEvent(tick = beat, velocity = 0, pitch = note_key)
            track.append(off)
            

        else:
            off = midi.NoteOnEvent(tick = beat, velocity = 0, pitch = 1)
            track.append(off)
            if prob_stop > onset_stop and note_cnt > 5:
                off = midi.NoteOnEvent(tick = 0, velocity = 0, pitch = note_last_key)
                track.append(off)
            #chord
        
                
    note_last = note

    

    return note_last, grace_flag
#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

