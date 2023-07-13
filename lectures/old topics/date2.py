class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # de constructor heet altijd __init__ !
    def __init__(self, day, month, year):
        """Construct a Date with the given day, month, and year."""
        self.day = day
        self.month = month
        self.year = year

    # de "afdruk"-functie heet altijd __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}-{:02d}-{:04d}".format(self.day, self.month, self.year)
        return s

    # Hier is een voorbeeld van een "methode" van de klasse Date:
    def is_leap_year(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.day, self.month, self.year)
        return dnew

    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
           whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way , we don't need to use the awkward
            d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def is_before(self, d2):
        """Decides if self comes before d2."""
        return (
            self.year < d2.year
            or (self.year == d2.year and self.month < d2.month)
            or (self.year == d2.year and self.month == d2.month and self.day < d2.day)
        )

    def __lt__(self, d2):
        """Overrides the < operator to decide if self comes before d2."""
        return self.is_before(d2)

    def is_after(self, d2):
        """Decides if self comes after d2."""
        return not self.is_before(d2) and not self.equals(d2)

    def __gt__(self, d2):
        """Overrides the > operator to decide if self comes after d2."""
        return self.is_after(d2)

    def tomorrow(self):
        """Set self to tomorrow."""
        if self.is_leap_year():
            fdays = 29
        else:
            fdays = 28
        dim = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += 1
        if self.day > dim[self.month]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def yesterday(self):
        """Set self to yesterday."""
        self.day -= 1
        if self.day < 1:
            if self.is_leap_year():
                fdays = 29
            else:
                fdays = 28
            dim = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            self.month -= 1
            if self.month < 1:
                self.month = 12
                self.year -= 1
            self.day = dim[self.month]

    def add_n_days(self, n):
        """Add n days to self."""
        print(self)
        for i in range(n):
            self.tomorrow()
            print(self)

    def sub_n_days(self, n):
        """Subtract n days from self."""
        print(self)
        for i in range(n):
            self.yesterday()
            print(self)

    def __iadd__(self, n):
        """Add n days to self."""
        self.add_n_days(n)
        return self

    def __isub__(self, n):
        """Subtract n days from self."""
        self.sub_n_days(n)
        return self

    def diff(self, d2):
        """Get the number of days between self and d2."""
        self_copy = self.copy()
        n = 0
        while self_copy.is_before(d2):
            n -= 1
            self_copy.tomorrow()
        while self_copy.is_after(d2):
            n += 1
            self_copy.yesterday()
        return n

    def __sub__(self, d2):
        """Get the number of days between self and d2."""
        return self.diff(d2)

    def dow(self):
        """Get the day of the week of self."""
        days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        n = self.diff(Date(10, 10, 2010))
        return days[n % 7]

    def dow2(self, sunday):
        days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        n = self.diff(sunday)
        return days[n % 7]
