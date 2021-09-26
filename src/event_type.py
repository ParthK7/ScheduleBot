class event_type:
    def __init__(self, event_name, start_time, end_time):
        self.event_name = event_name
        self.start_time = start_time
        self.end_time = end_time
     
    # Converts event object to a string
    def __str__(self):
        output = (
            self.event_name 
            + " "
            + str(self.start_time)
            + " "
            + str(self.end_time)
        )
        return output
    
    def get_start_time(self):
        return str(self.start_time.strftime('%I:%M %p'))

    def get_end_time(self):
        return str(self.end_time.strftime('%I:%M %p'))


# Converts event object to a list
    def to_list_event(self):
        array = [self.event_name, self.get_start_time(), self.get_end_time()]
        return array
