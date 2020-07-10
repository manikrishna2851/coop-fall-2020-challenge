class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.events = [] 
        self.undo_events = [] 

    def add(self, num: int):
        self.value += num
        self.events.append({"add":num})
        
    def subtract(self, num: int):
        self.value -= num
        self.events.append({"sub":num})

    def undo(self):
        if len(self.events) == 0:
            print('Nothing to undo')
            return
        event = self.events.pop()
        for name, value in event.items():
            if name == 'add':
                self.value -= value
                self.undo_events.append({"sub":value})
            elif name == 'sub':
                self.value += value
                self.undo_events.append({"add":value})

    def redo(self):
        if len(self.undo_events) == 0:
            print('Nothing to redo')
            return
        undo_event = self.undo_events.pop()
        for name, value in undo_event.items():
            if name == 'add':
                self.value -= value
                self.events.append({"sub":value})
            elif name == 'sub':
                self.value += value
                self.events.append({"add":value})
                

    def bulk_undo(self, steps: int):
        if len(self.events) < steps:
            steps = len(self.events)
            print('Overstep')
        for _ in range(0,steps):
            self.undo()

    def bulk_redo(self, steps: int):
        if len(self.undo_events) < steps:
            steps =  len(self.undo_events)
            print('Overstep')
        for _ in range(0,steps):
            self.redo()