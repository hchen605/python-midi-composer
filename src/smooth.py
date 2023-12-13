

def smooth(note, note_last, sm, sm_th):
    
    if (sm == 1 and (note - note_last) > sm_th):
        note_sm = note - 12
    else:
        note_sm = note

    return note_sm
