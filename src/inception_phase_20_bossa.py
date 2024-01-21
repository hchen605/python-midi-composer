#import random as rand
#import pandas_test as pt
#import smooth
from inception_include import *
import gen_piano_bossa_track

import gen_bass_bossa_track
import gen_drum_bossa_track
from midi2audio import FluidSynth
#import gen_string_track
#import gen_guitar_track
#import midi
from midi2audio import FluidSynth

def inception_phase_20_bossa(sm, num, key):
    import midi
    
    
    mode = 0;
    tick_0 = 6400
    tick_1 = 6400
    tick_2 = 9600
    
    beat_0 = 100
    beat_1 = 150
    beat_2 = 200
    beat_3 = 250
    
    onset_punch = 0.1
    onset_weak = 0.25
    onset_end = 0.25
    onset_guitar = 0.5
    
    velocity_punch = 80
    velocity_weak = 70
    velocity_bass = 70
    velocity_string = 45
    velocity_guitar = 40
    velocity_drum = 60
    
    tone = 'major'
    tick_mode = tick_0
    beat = beat_3
    #onset_mode = onset_0
    
    
    tick = 0
    note = 72;
    note_last = 72
    bass_last = 1
    
    # mode == 0 :
    # chord_a = gen_chord(key, mode, measure_num)
    chord_a = [C_major_9,
               C_major_9,
               D_13,
               D_13,
               D_minor_9,
               Db_13,
               C_major_9,
               Db_13]
              
    chord_b = [F_major_bass,
               G_major_bass,
               C_major_bass,
               C_major_bass,
               D_minor_bass,
               D_minor_bass,
               E_major_bass,
               E_major_bass]
      
    chord_c = [C_major_9,
               C_major_9,
               D_13,
               D_13,
               D_minor_9,
               Db_13,
               C_major_9,
               Db_13,
               C_major_9]

    
    chord = chord_a + chord_a * 3 + chord_c
    #chord = chord_a * 3
    
   
    scale_a = [midi.C_6,
               midi.C_6,
               midi.D_6,
               midi.D_6,
               midi.D_6,
               midi.D_6 - 1,
               midi.C_6,
               midi.D_6 - 1]

    scale_b = [midi.F_5,
               midi.G_5,
               midi.C_5,
               midi.C_5,
               midi.D_5,
               midi.D_5,
               midi.E_5,
               midi.E_5]
               
    scale_c = [midi.C_6,
               midi.C_6,
               midi.D_6,
               midi.D_6,
               midi.D_6,
               midi.D_6 - 1,
               midi.C_6,
               midi.D_6 - 1,
               midi.C_6]
    
    scale = scale_a + scale_a * 3 + scale_c
    #scale = scale_a * 4
    
    
    drum_en = [1] * (len(scale) - 1) + [1]
    #string_en = [0] * len(scale_a) + [1] * len(scale_b) + [1] * len(scale_c)
    #cadence = [0] * len(scale_a) + [0] * len(scale_b) + [0] * 6 + [1] * 3
    cadence = [0] * len(scale)
    
               
    total_measure = 8
    beat_per_measure = 4
    measure_per_chord = 1
    beat_per_chord = beat_per_measure * measure_per_chord
    note_res = beat/2
    note_per_beat = 2
    note_per_measure = beat_per_measure * note_per_beat
    note_per_chord = beat_per_chord * note_per_beat
    
    
    pattern = midi.Pattern()
    #piano track
    piano_track = midi.Track()
    pattern.append(piano_track)
    channel_num = 0
    piano = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[0])
    piano_track.append(piano)
    '''
    #piano chord track
    piano_chord_track = midi.Track()
    pattern.append(piano_chord_track)
    channel_num = 1
    piano = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[0])
    piano_chord_track.append(piano)
    '''
    #bass track
    bass_track = midi.Track()
    pattern.append(bass_track)
    channel_num = 1
    bass = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[33])
    bass_track.append(bass)
    
    #drum track
    drum_track = midi.Track()
    pattern.append(drum_track)
    channel_num = 9
    drum = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[0])
    drum_track.append(drum)
    '''    
    #string track
    string_track = midi.Track()
    pattern.append(string_track)
    channel_num = 2
    string = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[42])
    string_track.append(string)
    
    #guitar track
    guitar_track = midi.Track()
    pattern.append(guitar_track)
    channel_num = 3
    guitar = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[25])
    guitar_track.append(guitar)
    
    '''
    not_first_note = 0
    grace_flag = 0
    last = 0
    
    #A
    for chord_cnt in range(len(chord)):
        note_last = scale[chord_cnt]
        if chord_cnt == len(chord) - 1:
            last = 1
        for measure_cnt in range(measure_per_chord):
            beat_cnt = 0
            
            gen_bass_bossa_track.gen_bass_bossa_track(bass_track, beat, chord[chord_cnt], velocity_bass, last, key)
            gen_drum_bossa_track.gen_drum_bossa_track(drum_track, beat, not_first_note, velocity_drum, drum_en[chord_cnt], last)
            #gen_string_track.gen_string_track(string_track, beat, chord[chord_cnt], velocity_string, string_en[chord_cnt], last, key)
    
            gen_piano_bossa_track.gen_piano_bossa_track(piano_track, beat, chord[chord_cnt], scale[chord_cnt], chord_cnt, mode, sm, grace_flag, cadence, last, key)
                
                
            not_first_note = 1
            if last:
                break

    midi.write_midifile("bossa.mid", pattern)
    #FluidSynth().play_midi('blue.mid')
    FluidSynth().midi_to_audio('bossa.mid', 'bossa.wav')        
