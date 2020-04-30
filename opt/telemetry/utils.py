from threading import Timer


class TimeoutVar:
    """
    Class for the creation of variables with timeout.

    A timeout variable auto resets itself to a default value if it's not changed after the set timeout time.
    In this case the default value represent the unavailable state of the gps data.
    """

    def __init__(self, default, timeout_sec):
        """ Set options and initialize variable to it's default value. """
        self.actual = default
        self.default = default
        self._timeout_sec = timeout_sec
        self._timeout_timer = None

    def set_value(self, value):
        """ Set the value of the variable and reset the timeout timer. """
        self.actual = value
        if self.actual != self.default:
            if self._timeout_timer is not None: self._timeout_timer.cancel()
            self._timeout_timer = Timer(self._timeout_sec, self.set_value, [self.default])
            self._timeout_timer.start()
    
    def is_default(self):
        """ Tell if the variable value is the default one. """
        return self.actual == self.default

    def __str__(self):
        """ Return the string representation of the object. """
        return str(self.actual)
    
    def __repr__(self):
        """ Return the object representation. """
        return {'actual': self.actual, 'default': self.default}
