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
    # Constructor function
    # self is just the keyword thats being used 
    # Start is the arg used to set the range for for the serial number
    def __init__(self, start=0):
        """Make a new generator, starting at start."""

        # self.next = start which is 0
        self.start = self.next = start

    
    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next serial."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to original start."""

        self.next = self.start

