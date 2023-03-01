import random

class Rgb:
    def __int__(self):
        pass
    def rgb(self,):
        # Return RGB in Tuple
        r = random.randint(0, 255)  # Red
        g = random.randint(0, 255)  # Green
        b = random.randint(0, 255)  # Blue

        return r, g, b
