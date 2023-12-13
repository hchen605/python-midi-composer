import random as rand
import pandas_test as pt
import smooth
import gen_chord_bossa

def gen_piano_bossa_track(track, beat, chord, scale, chord_cnt, mode, sm, grace_flag, cadence, last, key):

    import midi

    sm_th = 9
    grace_prob_1 = 0.65
    grace_prob_2 = 0.8
    grace_tick = 50
    grace_tick_offset = 0
    done = 0
    onset = 0.45
    vel = 80
    note_last = scale
    note = note_last
    short_chord = 0
    short_tick = 50
    
    odd = chord_cnt % 2
    #if cadence:
    #beat = beat + 10
    chord = [x+key for x in chord]
    if chord_cnt == 0:
        beat_0 = 0
    else:
        beat_0 = 1
    
    #note
    
   
    if not odd:
        
        if last:
            off = midi.NoteOffEvent(tick = int(beat/2), velocity = vel, pitch = note_last)
            track.append(off)
            note = pt.gen_next_note(scale, mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_key = note + key
            on = midi.NoteOnEvent(tick = beat, velocity = vel, pitch = note_key)
            track.append(on)
            gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
            
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = chord[2]+24)
            track.append(on)
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = chord[0]+24)
            track.append(on)
            off = midi.NoteOffEvent(tick = beat*2, velocity = vel, pitch = chord[0]+24)
            track.append(off)
        else:
            
            #0
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(scale, mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            note_key = note + key
                
            grace = rand.random()
            if grace > grace_prob_1:
                on = midi.NoteOnEvent(tick = int(beat/2) * beat_0, velocity = vel, pitch = note_key - 1)
                track.append(on)
                #chord
                short_chord = 0
                gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
                
                off = midi.NoteOffEvent(tick = grace_tick, velocity = vel, pitch = note_key - 1)
                track.append(off)
                on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = note_key)
                track.append(on)
                grace_flag = 1
                
            else:
                on = midi.NoteOnEvent(tick = int(beat/2) * beat_0, velocity = vel, pitch = note_key)
                track.append(on)
                #chord
                short_chord = 0
                gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
        
            #1
            note_last = note
            prob = rand.random()
            if grace_flag == 1:
                grace_tick_offset = grace_tick
            else:
                grace_tick_offset = 0
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note_last,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2) - grace_tick_offset, velocity = vel, pitch = note_key)
            track.append(on)
            grace_flag = 0
            
            #2
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note_last,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            short_chord = 0
            gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
            
            #3
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
            track.append(on)
            
            #4
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(scale, mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            grace = rand.random()
            if grace > grace_prob_2:
                on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key - 1)
                track.append(on)
                #gen_chord_bossa.gen_chord_bossa(track, chord)
                
                off = midi.NoteOffEvent(tick = grace_tick, velocity = vel, pitch = note_key - 1)
                track.append(off)
                on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = note_key)
                track.append(on)
                grace_flag = 1
                
            else:
                on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
                track.append(on)
                #gen_chord_bossa.gen_chord_bossa(track, chord)
        
            #5
            note_last = note
            prob = rand.random()
            if grace_flag == 1:
                grace_tick_offset = grace_tick
            else:
                grace_tick_offset = 0
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2) - grace_tick_offset, velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            short_chord = 0
            gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
            grace_flag = 0
            
            #6
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
            track.append(on)
        
            #7
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            short_chord = 0
            gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
        
    else:
        
        if last:
            off = midi.NoteOffEvent(tick = int(beat/2), velocity = vel, pitch = note_last)
            track.append(off)
            note = pt.gen_next_note(scale, mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_key = note + key
            on = midi.NoteOnEvent(tick = beat, velocity = vel, pitch = note_key)
            track.append(on)
            gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
            
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = chord[2]+24)
            track.append(on)
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = chord[0]+24)
            track.append(on)
            
        else:
        
            #0
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(scale, mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            note_key = note + key
            grace = rand.random()
            if grace > grace_prob_1:
                on = midi.NoteOnEvent(tick = int(beat/2) * beat_0, velocity = vel, pitch = note_key - 1)
                track.append(on)
                #chord
                #gen_chord_bossa.gen_chord_bossa(track, chord)
                
                off = midi.NoteOffEvent(tick = grace_tick, velocity = vel, pitch = note_key - 1)
                track.append(off)
                on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = note_key)
                track.append(on)
                grace_flag = 1
                
            else:
                on = midi.NoteOnEvent(tick = int(beat/2) * beat_0, velocity = vel, pitch = note_key)
                track.append(on)
                #chord
                #gen_chord_bossa.gen_chord_bossa(track, chord)
        
            #1
            note_last = note
            prob = rand.random()
            if grace_flag == 1:
                grace_tick_offset = grace_tick
            else:
                grace_tick_offset = 0
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note_last,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2) - grace_tick_offset, velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            short_chord = 0
            gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
            grace_flag = 0
            
            #2
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note_last,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            #gen_chord_bossa.gen_chord_bossa(track, chord)
            
            #3
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
            track.append(on)
            
            #4
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(scale, mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            grace = rand.random()
            if grace > grace_prob_2:
                on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key - 1)
                track.append(on)
                #gen_chord_bossa.gen_chord_bossa(track, chord)
                #chord
                short_chord = 0
                gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
                
                off = midi.NoteOffEvent(tick = grace_tick, velocity = vel, pitch = note_key - 1)
                track.append(off)
                on = midi.NoteOnEvent(tick = 0, velocity = vel, pitch = note_key)
                track.append(on)
                grace_flag = 1
                
            else:
                on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
                track.append(on)
                #gen_chord_bossa.gen_chord_bossa(track, chord)
                #chord
                short_chord = 0
                gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
        
            #5
            note_last = note
            prob = rand.random()
            if grace_flag == 1:
                grace_tick_offset = grace_tick
            else:
                grace_tick_offset = 0
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2) - grace_tick_offset, velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            #gen_chord_bossa.gen_chord_bossa(track, chord)
            grace_flag = 0
            
            #6
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            short_chord = 0
            gen_chord_bossa.gen_chord_bossa(track, chord, key, short_chord)
        
            #7
            note_last = note
            prob = rand.random()
            if prob > onset:
                vel = 80
                note = pt.gen_next_note(note,mode)
                note = smooth.smooth(note, note_last, sm, sm_th)
                note_key = note + key
            else:
                vel = 0
            on = midi.NoteOnEvent(tick = int(beat/2), velocity = vel, pitch = note_key)
            track.append(on)
            #chord
            #gen_chord_bossa.gen_chord_bossa(track, chord)
       