class Note:
    def __init__(self, s, is_long=False):
        self.s = s
        if is_long:
            if s == 'до':
                self.s = 'до-о'
            elif s == 'ре':
                self.s = 'ре-э'
            elif s == 'ми':
                self.s = 'ми-и'
            elif s == 'фа':
                self.s = 'фа-а'
            elif s == 'соль':
                self.s = 'со-оль'
            elif s == 'ля':
                self.s = 'ля-а'
            elif s == 'си':
                self.s = 'си-и'

    def __str__(self):
        return self.s


class LoudNote(Note):
    def __str__(self):
        return self.s.upper()


class DefaultNote(Note):
    def __init__(self, s='до', is_long=False):
        self.s = s
        if is_long:
            if s == 'до':
                self.s = 'до-о'
            elif s == 'ре':
                self.s = 'ре-э'
            elif s == 'ми':
                self.s = 'ми-и'
            elif s == 'фа':
                self.s = 'фа-а'
            elif s == 'соль':
                self.s = 'со-оль'
            elif s == 'ля':
                self.s = 'ля-а'
            elif s == 'си':
                self.s = 'си-и'


class NoteWithOctave(Note):
    def __init__(self, s, oc, is_long=False):
        self.s = s
        if is_long:
            if s == 'до':
                self.s = 'до-о'
            elif s == 'ре':
                self.s = 'ре-э'
            elif s == 'ми':
                self.s = 'ми-и'
            elif s == 'фа':
                self.s = 'фа-а'
            elif s == 'соль':
                self.s = 'со-оль'
            elif s == 'ля':
                self.s = 'ля-а'
            elif s == 'си':
                self.s = 'си-и'
        self.oc = oc
    
    def __str__(self):
        return self.s + ' (' + self.oc + ')'


PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]