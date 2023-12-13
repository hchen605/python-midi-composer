import random as rand
import pandas_test as pt
import smooth

def gen_piano_blue_track(track, beat, note_last, chord, mode, vel, first_beat, third_beat, onset, sm, grace_flag, cadence, last, note_cnt, solo, key):

    import midi

    sm_th = 9
    grace_prob_1 = 0.7
    grace_prob_2 = 0.85
    grace_tick = 50
    grace_tick_offset = 0
    done = 0
    
    #if cadence:
    #beat = beat + 10

    #chord = chord + 12
    chord = [x+12+key for x in chord]
    #note
    prob = rand.random()
    prob_synco = rand.random()
    onset_piano_chord_back = 0.3
    onset_piano_chord_solo = 0.4
    
    if solo:
        onset_piano_chord = onset_piano_chord_solo
    else:
        onset_piano_chord = onset_piano_chord_back
    
    synco = note_cnt == 3 and prob_synco > onset_piano_chord
    vel_chord_1 = 60
    vel_chord_2 = 50
    vel_end = 90
    
    vel = vel * solo
    
    
    if last:
        prob = 0
    if prob > onset:
        note = pt.gen_next_note(note_last,mode)
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_key = note + key
        grace = rand.random()
        if grace_flag == 1:
            on = midi.NoteOnEvent(tick = beat - grace_tick, velocity = vel, pitch = note_key)
            track.append(on)
            grace_flag = 0
            done = 1
        
        if ((grace > grace_prob_1 and first_beat) or (grace > grace_prob_2 and third_beat)) and (done == 0):
            on = midi.NoteOnEvent(tick = beat, velocity = vel, pitch = note_key - 1)
            track.append(on)
            #chord
            if first_beat:
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_1, pitch = chord[0])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[1])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[2])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[3])
                track.append(on)
            off = midi.NoteOffEvent(tick = grace_tick, velocity = vel, pitch = note_key - 1)
            track.append(off)
            on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = note_key)
            track.append(on)
            grace_flag = 1
            done = 1

        if (done == 0):
            on = midi.NoteOnEvent(tick = beat, velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            if first_beat:
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_1, pitch = chord[0])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[1])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[2])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[3])
                track.append(on)
            elif synco:
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_1, pitch = chord[0])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[1])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[2])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[3])
                track.append(on)
    else:
        note = note_last
        note_key = note + key
        if grace_flag == 1:
            off = midi.NoteOnEvent(tick = beat - grace_tick, velocity = 0, pitch = note_key)
            track.append(off)
            grace_flag = 0
            note = note_last
        elif last:
            off = midi.NoteOnEvent(tick = beat, velocity = 0, pitch = note_key)
            track.append(off)
            if first_beat:
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_1, pitch = chord[0])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_end, pitch = chord[0]+24)
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = 40, pitch = chord[1])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = 40, pitch = chord[2])
                track.append(on)

            

                off = midi.NoteOffEvent(tick = beat*3, velocity = vel_chord_1, pitch = chord[0])
                track.append(off)
                off = midi.NoteOffEvent(tick = 0, velocity = vel_end, pitch = chord[0]+24)
                track.append(off)
                off = midi.NoteOffEvent(tick = 0, velocity = 40, pitch = chord[1])
                track.append(off)
                off = midi.NoteOffEvent(tick = 0, velocity = 40, pitch = chord[2])
                track.append(off)

                #on = midi.NoteOnEvent(tick = beat, velocity = 50, pitch = chord[2]+24)
                #track.append(on)
                #on = midi.NoteOnEvent(tick = beat, velocity = 50, pitch = chord[0]+36)
                #track.append(on)
                #off = midi.NoteOffEvent(tick = beat*2, velocity = 50, pitch = chord[0]+36)
                #track.append(off)

        else:
            off = midi.NoteOnEvent(tick = beat, velocity = 0, pitch = note_key)
            track.append(off)
            #chord
            if first_beat:
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_1, pitch = chord[0])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[1])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[2])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[3])
                track.append(on)
            elif synco:
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_1, pitch = chord[0])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[1])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[2])
                track.append(on)
                on = midi.NoteOnEvent(tick = 0, velocity = vel_chord_2, pitch = chord[3])
                track.append(on)
                
    note_last = note

    

    return note_last, grace_flag
#off = midi.NoteOffEvent(tick = beat+beat, velocity = 80, pitch = note)
#piano_track.append(off)

