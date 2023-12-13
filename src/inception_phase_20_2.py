import random as rand
import pandas_test as pt
import smooth
from inception_include import *

def inception_phase_20_2(sm, num):

    mode = 1;
    fp = open("auto_phase_11.py", "w")

#start composing MIDI
    fp.write("#Inception phase 11\n");
    fp.write("import midi\n\n\n")
    fp.write("def midi_gen():\n")
    fp.write("    hh_midi = midi.Pattern(tracks=[[midi.TimeSignatureEvent(tick=0, data=[4, 2, 24, 8]),")
    midi_setup = ["    midi.KeySignatureEvent(tick=0, data=[0, 0]),\n",
              "    midi.EndOfTrackEvent(tick=1, data=[])],\n",
              "    [midi.ControlChangeEvent(tick=0, channel=0, data=[91, 58]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[10, 69]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[0, 0]),\n",
              "    midi.ControlChangeEvent(tick=0, channel=0, data=[32, 0]),\n",
              "    midi.ProgramChangeEvent(tick=0, channel=0, data=[0]),\n\n"]

    fp.writelines(midi_setup)

#automatic composing
    fp.write("#automatic composing\n")
   
    
    tick_0 = 6400
    tick_1 = 6400
    tick_2 = 9600
    
    beat_0 = 100
    beat_1 = 100
    beat_2 = 200
    
    onset_0 = 0.1
    onset_1 = 0.1
    onset_2 = 0.25

    #if mode == 1:
    chord_1 = A2
    chord_2 = D3
    chord_3 = G3
    chord_4 = C3
    chord_5 = D3
    chord_6 = A2
    chord_7 = F3
    chord_8 = E3
    chord_8_c = A2
    chord_1_b = G3
    chord_2_b = A2
    chord_3_b = G3
    chord_4_b = A2
    chord_5_b = F3
    chord_6_b = F3
    chord_7_b = E3
    chord_8_b = E3
        
    chorus_b_1 = G_major_bass
    chorus_b_2 = A_minor_bass
    chorus_b_3 = G_major_bass
    chorus_b_4 = A_minor_bass
    chorus_b_5 = F_major_bass
    chorus_b_6 = F_major_bass
    chorus_b_7 = E_major_bass
    chorus_b_8 = E_major_bass
        
    chorus_c_1 = A_minor_bass
    chorus_c_2 = D_minor_bass
    chorus_c_3 = G_major_bass
    chorus_c_4 = C_major_bass
    chorus_c_5 = D_minor_bass
    chorus_c_6 = A_minor_bass
    chorus_c_7 = F_major_bass
    chorus_c_8 = E_major_bass
    chorus_c_8_c = A_minor_bass
        
    scale_1 = A_minor
    scale_2 = D_minor
    scale_3 = G_major
    scale_4 = C_major
    scale_5 = D_minor
    scale_6 = A_minor
    scale_7 = F_major
    scale_8 = E_major
    scale_8_c = A_minor
    scale_1_b = G_major
    scale_2_b = A_minor
    scale_3_b = G_major
    scale_4_b = A_minor
    scale_5_b = F_major
    scale_6_b = F_major
    scale_7_b = E_major
    scale_8_b = E_major
    tone = 'minor'
    tick_mode = tick_1
    beat = beat_1
    onset_mode = onset_1
    


    tick = 0
    note = 72;
    note_last = 72
    sm_th = 9

# AB
    while (tick < 6400):
        tick_round = tick%6400
        if tick_round < 800:
            chord = chord_1
            scale = scale_1
        elif 800 <= tick_round < 1600:
            chord = chord_2
            scale = scale_2
        elif 1600 <= tick_round < 2400:
            chord = chord_3
            scale = scale_3
        elif 2400 <= tick_round < 3200:
            chord = chord_4
            scale = scale_4
        elif 3200 <= tick_round < 4000:
            chord = chord_5
            scale = scale_5
        elif 4000 <= tick_round < 4800:
            chord = chord_6
            scale = scale_6
        elif 4800 <= tick_round < 5600:
            chord = chord_7
            scale = scale_7
        elif 5600 <= tick_round < 6400:
            chord = chord_8
            scale = scale_8
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,chord))
        
        onset = rand.random()
        if onset > 0.3:
            note = pt.gen_next_note(scale[0],mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(0,note))
        
        onset = rand.random()
        if onset > 0.4:
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(100,note))
        

        onset = rand.random()
        if onset > 0.2:
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last =  note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(100,note))

        onset = rand.random()
        if onset > 0.45:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 400
    
    
    note_last = 72
    sm_th = 9
    tick = 0
    # bridge
    while (tick < 6400):
        tick_round = tick%6400
        if tick_round < 800:
            chord = chord_1_b
            scale = scale_1_b
        elif 800 <= tick_round < 1600:
            chord = chord_2_b
            scale = scale_2_b
        elif 1600 <= tick_round < 2400:
            chord = chord_3_b
            scale = scale_3_b
        elif 2400 <= tick_round < 3200:
            chord = chord_4_b
            scale = scale_4_b
        elif 3200 <= tick_round < 4000:
            chord = chord_5_b
            scale = scale_5_b
        elif 4000 <= tick_round < 4800:
            chord = chord_6_b
            scale = scale_6_b
        elif 4800 <= tick_round < 5600:
            chord = chord_7_b
            scale = scale_7_b
        elif 5600 <= tick_round < 6400:
            chord = chord_8_b
            scale = scale_8_b
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(100,chord))

        onset = rand.random()
        if onset > 0.3:
            note = pt.gen_next_note(scale[0],mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(0,note))
        
        onset = rand.random()
        if onset > 0.3:
            v = 80
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
        else:
            v = 0

        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))

        if onset > 0.2:
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            v = 80
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        else:
            v = 0
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))

        onset = rand.random()
        if onset > 0.4:
            v = 80
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
        else:
            v = 0

        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 800
    
    
    note_last = 72
    sm_th = 9
    tick = 0
    # C
    while (tick < 6400):
        tick_round = tick%6400
        if tick_round < 800:
            chord = chorus_c_1
            scale = scale_1
        elif 800 <= tick_round < 1600:
            chord = chorus_c_2
            scale = scale_2
        elif 1600 <= tick_round < 2400:
            chord = chorus_c_3
            scale = scale_3
        elif 2400 <= tick_round < 3200:
            chord = chorus_c_4
            scale = scale_4
        elif 3200 <= tick_round < 4000:
            chord = chorus_c_5
            scale = scale_5
        elif 4000 <= tick_round < 4800:
            chord = chorus_c_6
            scale = scale_6
        elif 4800 <= tick_round < 5200:
            chord = chorus_c_7
            scale = scale_7
        elif 5200 <= tick_round < 5600:
            chord = chorus_c_8
            scale = scale_8
        elif 5600 <= tick_round < 6400:
            chord = chorus_c_8_c
            scale = scale_8_c
        
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 70]),\n".format(100,chord[0]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[1]))
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 50]),\n".format(0,chord[2]))
        onset = rand.random()
        if onset > 0.2:
            note = pt.gen_next_note(scale[0],mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 80]),\n".format(0,note))
        else:
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, 0]),\n".format(0,note))

        onset = rand.random()
        if onset > 0.25:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        onset = rand.random()
        if onset > 0.25:
            note = pt.gen_next_note(note,mode)
            note = smooth.smooth(note, note_last, sm, sm_th)
            note_last = note
            v = 80
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        else:
            v = 0
            fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        
        onset = rand.random()
        if onset > 0.3:
            v = 80
            note = pt.gen_next_note(note,mode)
        else:
            v = 0
        note = smooth.smooth(note, note_last, sm, sm_th)
        note_last = note
        fp.write("    midi.NoteOnEvent(tick={}, data = [{}, {}]),\n".format(100,note,v))
        tick = tick + 400
    
        
#end automatic composing
    fp.write("#end automatic composing\n\n")
    
    
    fp.write("    midi.EndOfTrackEvent(tick=1, data=[])]])\n\n\n")
    fp.write("    midi.write_midifile(\"inception_phase_28_{}_{}.mid\", hh_midi)".format(tone,num))

    fp.close()

    #midi_file = 'inception_phase_11_{}_0.mid'.format(tone)
    #midi_play.play_music(midi_file)


