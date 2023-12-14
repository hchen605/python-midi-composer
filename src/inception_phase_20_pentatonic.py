import random as rand
import pandas_test as pt
import smooth
from inception_include import *
import gen_piano_track
import gen_bass_track
import gen_drum_track
import gen_string_track
import gen_guitar_track
import gen_marimba_track
from midi2audio import FluidSynth
#import midi

def inception_phase_20_pentatonic(sm, num, key):
    import midi
    
    
    mode = 3;
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
    onset_marimba = 0.4
    
    velocity_punch = 80
    velocity_weak = 70
    velocity_bass = 70
    velocity_string = 45
    velocity_guitar = 40
    velocity_marimba = 50
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
    
    
    
    
    chord_a = [C_major_bass,
               A_minor_bass,
               F_major_bass,
               G_major_bass]
              
    chord_b = [C_major_bass,
               A_minor_bass,
               F_major_bass,
               G_major_bass,
               C_major_bass]
    
    chord_c = []
               
    chord = chord_a + chord_b + chord_c
    
   
    scale_a = [midi.C_5,
               midi.A_5,
               midi.F_5,
               midi.G_5]
    
    scale_b = [midi.C_5,
               midi.A_5,
               midi.F_5,
               midi.G_5,
               midi.C_5]

    scale_c = []
    
    scale = scale_a + scale_b + scale_c
    
    drum_en = [0] * len(scale_a) + [0] * len(scale_b) + [1] * len(scale_c)
    string_en = [0] * len(scale_a) + [1] * len(scale_b) + [1] * len(scale_c)
    guitar_en = [0] * len(scale_a) + [0] * len(scale_b) + [1] * len(scale_c)
    cadence = [0] * len(scale_a) + [0] * len(scale_b) + [0] * 6 + [1] * 3
    
               
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
    
    #marimba track
    marimba_track = midi.Track()
    pattern.append(marimba_track)
    channel_num = 4
    marimba = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[12])
    marimba_track.append(marimba)
    
    
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
            first_beat = 0
            third_beat = 0
            gen_bass_track.gen_bass_track(bass_track, beat, chord[chord_cnt], velocity_bass, key)
            gen_string_track.gen_string_track(string_track, beat, chord[chord_cnt], velocity_string, string_en[chord_cnt], last, key)
            for note_cnt in range(note_per_measure):
                beat_cnt = note_cnt/2
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
                note_last, grace_flag = gen_piano_track.gen_piano_track(piano_track, beat_in, note_last, chord[chord_cnt], mode, velocity, first_beat, third_beat, onset, sm, grace_flag, cadence, last, key)
                gen_guitar_track.gen_guitar_track(guitar_track, beat_in, note_last, chord[chord_cnt], mode, velocity_guitar, first_beat, third_beat, onset_guitar, key)
                gen_marimba_track.gen_marimba_track(marimba_track, beat_in, note_last, chord[chord_cnt], mode, velocity_marimba, first_beat, third_beat, onset_marimba, key)
                
                
                if note_cnt%2 == 0:
                    gen_drum_track.gen_drum_track(drum_track, beat*not_first_note, velocity_drum, first_beat, third_beat, drum_en[chord_cnt])
                
                not_first_note = 1
                if last:
                    break

    midi.write_midifile("pentatonic_major.mid", pattern)
    #FluidSynth().play_midi('pentatonic_major.mid')
            
