##
# Andiamo a costruire la classe point per l'inserimento delle coordinate

class point:
    # Definisco il costruttore e alcuni attributi default
    def __init__(self, start_x, start_y, stop_x, stop_y):
        # Variabili di istanza
        self.start_x = int(start_x)
        self.start_y = start_y
        self.stop_x = stop_x
        self.stop_y = stop_y
        self.top_left = start_x, start_y
        self.bottom_right = stop_x, stop_y
        self.roi = f'{start_y}:{stop_y}, {start_x}:{stop_x}'

    def get_roi(self): # Accessor
        return self.roi

    def get_start_x(self): # Accessor
        return int(self.start_x)
    def get_start_y(self): # Accessor
        return int(self.start_y)
    def get_stop_x(self): # Accessor
        return int(self.stop_x)
    def get_stop_y(self): # Accessor
        return int(self.stop_y)
    
    def get_top_left(self): # Accessor
        return self.top_left

    def get_bottom_right(self): # Accessor
        return self.bottom_right
