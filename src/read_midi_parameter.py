
#import midi
from music21 import converter, corpus, instrument, midi, note, chord, pitch, stream, roman
from music21_add import *
from music21 import *
import midi
import numpy as np

def read_midi_parameter(midi_file):
    
    #print(midi)
    pattern_read = midi.read_midifile(midi_file)
    #print(pattern_read)
    beat = pattern_read.resolution
    #pattern = open_midi("hh.mid", True)
    # midi_stream = converter.parse(midi_file)

    # # Extract chords from the MIDI file
    # chords = []
    
    # # Iterate through notes and chords in the MIDI stream
    # for element in midi_stream.flat:
    #     if isinstance(element, chord.Chord):
    #         #print(element)
    #         chords.append(element.pitchedCommonName)  # Extract chord names

    # #print("Chord Progression:")
    # #print(chords)

    # chords_per_measure = {}
    # # Iterate through measures in the MIDI stream
    # for part in midi_stream.parts:
    #     for measure_number, measure in enumerate(part.getElementsByClass('Measure')):
    #         print(measure_number)
    #         print(measure)
    #         if measure_number not in chords_per_measure:
    #             chords_per_measure[measure_number] = []

    #         # Get the first chord in the measure
    #         chord_found = False
    #         for element in measure:
    #             if isinstance(element, chord.Chord):
    #                 chords_per_measure[measure_number].append(element.pitchedCommonName)
    #                 chord_found = True
    #                 break

    #         # If no chord found, insert an empty string for the measure
    #         if not chord_found:
    #             chords_per_measure[measure_number].append("")

    # # Display the identified chord progression (one chord per measure)
    # print("Chord Progression (One Chord Per Measure):")
    # for measure_number, chords in chords_per_measure.items():
    #     print(chords_per_measure)  # Display the first chord in each measure

    pattern = open_midi(midi_file, True)

    temp_midi = stream.Score()
    #print(temp_midi)
    temp_midi_chords = pattern.chordify()

    temp_midi.insert(0, temp_midi_chords)
    music_key = temp_midi.analyze('key')
    #print('Key: ', music_key)
    time_signature = temp_midi_chords.getTimeSignatures()[0]
    
    # total_beat = np.size(temp_midi_chords) + 1 - 4
    # total_measure = total_beat / time_signature.beatCount

    # fp = open("chord.txt", "w")
    # for thisChord in temp_midi_chords.recurse().getElementsByClass(chord.Chord):
    #     #print(thisChord)
    #     #print(thisChord.measureNumber, thisChord.beatStr, thisChord)
    #     note_beat = str(thisChord).strip('<>')
    #     fp.write(note_beat)
    #     fp.write("\n")
    
    # fp.close()
    
    
    
    # count = 1
    # ret = []
    # note_list = []
    # fp = open("chord.txt", "r")
    # while True:
    #     read = fp.readline()
    #     read_size = np.size(read.split())
    #     #print read_size
    #     if not read:
    #         #print('end note: ', note_list)
    #         if not note_list:
    #             break
    #         measure_chord = chord.Chord(note_list)
    #         roman_numeral = roman.romanNumeralFromChord(measure_chord, music_key)
    #         ret.append(simplify_roman_name(roman_numeral))
    #         break
    #     #print(read)
    #     #i = 1
        
    #     for i in range(1, read_size):
    #         note1 = read.split()[i]
    #         if note1 == 'rest':
    #             note1 = note1_pre
    #             note_list.append(note1)
    #         else:
    #             note_list.append(note1)
    #             note1_pre = note1
    #     i = i + 1
    #     #print(note_list)
    #     if count % time_signature.beatCount == 0: #or count == total_measure:
    #         #print(note_list)
    #         measure_chord = chord.Chord(note_list)
    #         #print(measure_chord)
    #         roman_numeral = roman.romanNumeralFromChord(measure_chord, music_key)
    #         #print(roman_numeral)
    #         ret.append(simplify_roman_name(roman_numeral))
    #         note_list = []
        
    #     count = count + 1
    # fp.close()
    

    return beat, music_key, time_signature, pattern_read
