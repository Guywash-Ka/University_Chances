class Bell:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print_info(self):
        if self.kwargs:
            list_keys = list(self.kwargs.keys())
            list_keys.sort()
            res = []
            for i in list_keys:
                res.append(f'{i}: {self.kwargs[i]}')
            if self.args:
                print(', '.join(res) + ';', ', '.join(self.args))
            else:
                print(', '.join(res))
        elif self.args:
            print(', '.join(self.args))
        else:
            print('-')


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.is_ding = True
    
    def __str__(self):
        if self.is_ding:
            return 'ding'
        return 'dong'
    
    def sound(self):
        print(self)
        if self.is_ding:
            self.is_ding = False
        else:
            self.is_ding = True
        

class LittleBell(Bell):
    def __str__(self):
        return 'ding'
    
    def sound(self):
        print(self)