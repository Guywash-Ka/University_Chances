class BigBell:
    def __init__(self):
        self.is_ding = True
    
    def __str__(self):
        if self.is_ding:
            return 'ding'
        return 'dong'
    

class LittleBell:
    def __str__(self):
        return 'ding'


class BellTower:
    def __init__(self, *args):
        self.bells = list(args)
    
    def sound(self):
        for i in self.bells:
            print(i)
            if isinstance(i, BigBell):
                if i.is_ding:
                    i.is_ding = False
                else:
                    i.is_ding = True
        print('...')
    
    def append(self, bell):
        self.bells.append(bell)