import midi


    
C2 = 36
D2 = 38
E2 = 40
F2 = 41
G1 = 31
A1 = 33
B1 = 35
F1 = 29
    
C3 = 48
Db3 = 49
D3 = 50
D4 = 62
E3 = 52
E4 = 64
F3 = 53
Gb3 = 54
G3 = 55
G4 = 67
A2 = 45
B2 = 47
G2 = 43
B3 = 59
B4 = 71
F2 = 41
A3 = 57
A4 = 69
F3 = 53
F4 = 65
C4 = 60
C5 = 72
D5 = 74
E5 = 76
F5 = 77
G5 = 79
A5 = 81
B5 = 83

Gb5 = 78
Gb3 = 54
Ab5 = 80
Ab3 = 56
Ab2 = 44
Bb3 = 58
Bb2 = 46
Bb5 = 82
Bb4 = 70
Eb3 = 51
Eb4 = 63
Eb2 = 39
Eb5 = 75

scale_C = [C5,D5,E5,F5,G5,A5,B5]
C_major = [C5,E5,G5,E5]
G_major = [G5,B5,D5,B5]
A_minor = [A5,C5,E5,C5]
E_minor = [E5,G5,B5,G5]
F_major = [F5,A5,C5,A5]
D_minor = [D5,F5,A5,F5]
D_major = [D5,Gb5,A5,Gb5]
E_major = [E5,Ab5,B5,Ab5]
E_7 = [E5,Ab5,B5,D5]
D_7 = [D5,Gb5,A5,C5]
D_7_bass = [D3,Gb3,A3,C3]
    
C_major_bass = [C3,E3,G3,E3]
G_major_bass = [G2,B2,D3,B2]
A_minor_bass = [A2,C3,E3,C3]
#E_minor_bass = [E3,G3,B3,G3]
E_minor_bass = [E2,G2,B2,G2]
#E_major_bass = [E3,Ab3,B3,Ab3]
F_major_bass = [F2,A2,C3,A2]
D_minor_bass = [D3,F3,A3,F3]
D_major_bass = [D3,Gb3,A3,Gb3]
E_major_bass = [E2,Ab2,B2,Ab2]
E_7_bass = [E3,Ab3,B3,D3]

#G6  = [G5,B5,D6,E6]
G6_bass = [G2,B2,D3,E3]
    
C_major_7_bass = [C3,E3,G3,Bb3,C4]
F_major_7_bass = [F2,A2,C3,Eb3,F3]
G_major_7_bass = [G2,B2,D3,F3,G3]
C_major_7_bass_low = [C2,E2,G2,Bb2,C3]
F_major_7_bass_low = [F1,A1,C2,Eb2,F2]
G_major_7_bass_low = [G1,B1,D2,F2,G2]
C_major_7 = [C4,E4,G4,Bb4,C5]
F_major_7 = [F3,A3,C4,Eb4,F4]
G_major_7 = [G3,B3,D4,F4,G4]

#C_major_9 = [midi.C_3, midi.E_3, midi.G_3, midi.B_3, midi.D_2]  
C_major_9 = [C3,E3,G3,B3,D3] #1372
D_13 =      [D3,Gb3,A3,C4,B2] #13b76 2#417
#D_13 =      [D3,Gb3,A3,C4,E4,B4] #13b76 2#417
D_minor_9 = [D3,F3,A3,C4,E2]
Db_13 =     [Db3,F3,Ab3,B3,Bb2]
#Db_13 = [Db3,F3,Ab3,B3,Eb4,Bb4]


    
#drum
HH = 51
SS = 37
SD = 38
BD = 35
LT = 41
HT = 48
