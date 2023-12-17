import sys
sys.path.append('src')
import read_midi_parameter as rmidi
import midi
import gen_piano_blue_track
import gen_drum_blue_track
from inception_include import *
#from read_midi_parameter import *
# import add_bass_track 
# import add_drum_track 
# import add_string_track

midi_file = "data/Honestly_Piano_12.midi"
#midi_file = "blue.mid"

beat, music_key, time_signature, pattern = rmidi.read_midi_parameter(midi_file)

print('Beat: ', beat)
print('Key: ', music_key)
print('Time Signature: ', time_signature)
#print('Chord Progress: ', chord)

#beat = 200
onset_punch = 0.1
onset_weak = 0.25
onset_piano = 0.4
onset_piano_less = 0.5
onset_piano_more = 0.4
onset_piano_end = 0.6
beat_per_measure = 4
note_per_beat = 2
note_per_measure = beat_per_measure * note_per_beat
velocity_punch = 80
velocity_weak = 70
mode = 2
sm = 1
last = 0
piano_solo = 1
key = 0
cadence = [0] * (11) + [0]
grace_flag_piano = 0
ending = 0

velocity_drum = 60

chord = [
          C_major_7_bass,
          G_major_7_bass,
          Bb_major_7,
          F_major_7_bass,
          C_major_7_bass,
          D_7_bass,
          F_major_7_bass,
          G_major_7_bass,
          C_major_7_bass,
          F_major_7_bass,
          C_major_7_bass,
          C_major_7_bass
]
drum_en = [1] * len(chord) 

piano_track = midi.Track()
pattern.append(piano_track)
channel_num = 0
piano = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[0])
piano_track.append(piano)

#add drum track
drum_track = midi.Track()
pattern.append(drum_track)
channel_num = 9
drum = midi.ProgramChangeEvent(tick=0, channel=channel_num, data=[0])
drum_track.append(drum)

for chord_cnt in range(len(chord)):
    note_last_piano = midi.C_6

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

        beat_in = int(beat/2)
        note_last_piano, grace_flag_piano = gen_piano_blue_track.gen_piano_blue_track(piano_track, beat_in, note_last_piano, chord[chord_cnt], mode, velocity, first_beat, third_beat, onset_piano, sm, grace_flag_piano, cadence, last, note_cnt, piano_solo, key)
        gen_drum_blue_track.gen_drum_blue_track(drum_track, beat_in, velocity_drum, first_beat, third_beat, drum_en[chord_cnt], note_cnt, ending, last)

# #add bass track
# bass_track = midi.Track()
# pattern.append(bass_track)
# channel_num = 1
# add_bass_track.add_bass_track(bass_track, channel_num, beat, music_key, time_signature, chord)

# #add drum track
# drum_track = midi.Track()
# pattern.append(drum_track)

# channel_num = 9
# add_drum_track.add_drum_track(drum_track, channel_num, beat, time_signature, chord)


# #add string track
# string_track = midi.Track()
# pattern.append(string_track)
# channel_num = 2
# add_string_track.add_string_track(string_track, channel_num, beat, music_key, time_signature, chord)

midi.write_midifile("Honestly_blue.mid", pattern)



