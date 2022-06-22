"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """ creates a number generator that increments by 1 starting at user inputed start point """
        self.start = start
        self.gen_num = start

    def generate(self):
        """ increments the number by 1 """
        self.gen_num += 1
        return self.gen_num - 1

    def reset(self):
        """ resets the number generator back to the starting value """
        self.gen_num = self.start



