import random as rand
import pandas_test as pt
import smooth
from inception_include import *
import gen_piano_blue_track
import gen_sax_blue_track
import gen_bass_blue_track
import gen_drum_blue_track
#import gen_string_track
#import gen_guitar_track
#import midi
from midi2audio import FluidSynth 

def inception_phase_20_blue(sm, num, key):
    import midi
    
    
    mode = 2
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
    beat = beat_2
    #onset_mode = onset_0
    onset_piano = 0.4
    onset_piano_less = 0.5
    onset_piano_more = 0.4
    onset_piano_end = 0.6
    onset_sax = 0.45
    onset_sax_less = 0.5
    onset_sax_more = 0.4
    onset_piano_chord_back = 0.3
    onset_piano_chord_solo = 0.5
    
    tick = 0
    note = 72
    note_last = 72
    bass_last = 1
    
    # mode == 0 :
    # chord_a = gen_chord(key, mode, measure_num)
    
    
    
    chord_a = [C_major_7_bass,
               C_major_7_bass,
               C_major_7_bass,
               C_major_7_bass,
               F_major_7_bass,
               F_major_7_bass,
               C_major_7_bass,
               C_major_7_bass,
               G_major_7_bass,
               F_major_7_bass,
               C_major_7_bass,
               C_major_7_bass]
    '''chord_a = [C_major_7,
               C_major_7,
               C_major_7,
               C_major_7,
               F_major_7,
               F_major_7,
               C_major_7,
               C_major_7,
               G_major_7,
               F_major_7,
               C_major_7,
               C_major_7]    '''      
    
    
    chord = chord_a * 1
    
   
    scale_a = [midi.C_6,
               midi.C_6,
               midi.C_6,
               midi.C_6,
               midi.F_6,
               midi.F_6,
               midi.C_6,
               midi.C_6,
               midi.G_6,
               midi.F_6,
               midi.C_6,
               midi.C_6]

    
    
    scale = scale_a * 1
    #scale_sax = [x-12 for x in scale]
    scale_sax = scale
    
    drum_en = [1] * len(scale) 
    #string_en = [0] * len(scale_a) + [1] * len(scale_b) + [1] * len(scale_c)
    #cadence = [0] * len(scale_a) + [0] * len(scale_b) + [0] * 6 + [1] * 3
    cadence = [0] * (len(scale_a)-1) + [0]
               
    #total_measure = 8
    beat_per_measure = 4
    measure_per_chord = 1
    beat_per_chord = beat_per_measure * measure_per_chord
    #note_res = beat/2
    note_per_beat = 2
    note_per_measure = beat_per_measure * note_per_beat
    #note_per_chord = beat_per_chord * note_per_beat
    
    
    pattern = midi.Pattern()
    #piano track
    piano_track = midi.Track()
    pattern.append(piano_track)
    channel_num = 0
    piano = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[0])
    piano_track.append(piano)
    
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
    
    #sax track
    sax_track = midi.Track()
    pattern.append(sax_track)
    channel_num = 2
    sax = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[66])
    sax_track.append(sax)
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
    grace_flag_piano = 0
    grace_flag_sax = 0
    last = 0
    ending = 0
    loop = 5
    piano_solo = 0
    sax_solo = 0
    note_last_sax = scale_sax[0] 
    #A
    for i in range(loop):
        if i == 0 or i == 1 or i == loop - 1:
            piano_solo = 1
            onset_piano = onset_piano_more
        else:
            piano_solo = 0
            onset_piano = onset_piano_less
        if i == 2:
            sax_solo = 1
            onset_sax = onset_sax_less
        elif i == 3:
            sax_solo = 1
            onset_sax = onset_sax_more
        else:
            sax_solo = 0
        #note_last_sax = scale[0]
        for chord_cnt in range(len(chord)):
            note_last_piano = scale[chord_cnt]
            #note_last_sax = scale[chord_cnt]
            if chord_cnt == len(chord) - 1 and i == loop - 1:
                last = 1
            if chord_cnt >= len(chord) - 2 and i == loop - 1:
                ending = 1
                onset_piano = onset_piano_end
            for measure_cnt in range(measure_per_chord):
                #beat_cnt = 0
                first_beat = 0
                third_beat = 0
                #gen_bass_track.gen_bass_track(bass_track, beat, chord[chord_cnt], velocity_bass)
                #gen_string_track.gen_string_track(string_track, beat, chord[chord_cnt], velocity_string, string_en[chord_cnt], last)
                #gen_drum_blue_track.gen_drum_blue_track(drum_track, beat, velocity_drum, first_beat, third_beat, drum_en[chord_cnt], chord_cnt)
    
                for note_cnt in range(note_per_measure):
                    #beat_cnt = note_cnt/2
                    onset = onset_weak
                    if note_cnt == 0:
                        first_beat = 1
                        onset = onset_punch
                        velocity = velocity_punch
                    else:
                        first_beat = 0
                        velocity = velocity_weak
                    if note_cnt == 4:
                        third_beat = 1
                        onset = onset_punch
                        velocity = velocity_punch
                    else:
                        third_beat = 0
                        velocity = velocity_weak
        
                    beat_in = int(beat/2*not_first_note)
                    note_last_piano, grace_flag_piano = gen_piano_blue_track.gen_piano_blue_track(piano_track, beat_in, note_last_piano, chord[chord_cnt], mode, velocity, first_beat, third_beat, onset_piano, sm, grace_flag_piano, cadence, last, note_cnt, piano_solo, key)
                    note_last_sax, grace_flag_sax = gen_sax_blue_track.gen_sax_blue_track(sax_track, beat_in, scale_sax[chord_cnt], note_last_sax, chord[chord_cnt], mode, velocity, first_beat, third_beat, onset_sax, sm, grace_flag_sax, cadence, last, note_cnt, sax_solo, key)
                    
                    
                    gen_drum_blue_track.gen_drum_blue_track(drum_track, beat_in, velocity_drum, first_beat, third_beat, drum_en[chord_cnt], note_cnt, ending, last)
    
                    if note_cnt%2 == 0:
                        #gen_drum_blue_track.gen_drum_blue_track(drum_track, beat*not_first_note, velocity_drum, first_beat, third_beat, drum_en[chord_cnt], note_cnt)
                        gen_bass_blue_track.gen_bass_blue_track(bass_track, beat, chord[chord_cnt], velocity_bass, chord_cnt, note_cnt, ending, key)
                        
                    not_first_note = 1
                    if last:
                        break

    midi.write_midifile("blue.mid", pattern)
    #FluidSynth().play_midi('blue.mid')
    FluidSynth().midi_to_audio('blue.mid', 'blue.wav')
            
