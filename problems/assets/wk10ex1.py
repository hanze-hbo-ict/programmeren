#
# wk10ex1.py
#
# naam:
#

# Eerst de klassedefinitie
# Hieronder definiëren we een aantal handige objecten van het type Date
#  +++ bewaar die en/of voeg je eigen toe! +++


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


#
# vergeet niet je code voor de klasse Date HIERBOVEN toe te voegen; in de klassedefinitie
#


#
# een aantal datums om mee te werken...
#
# Het handige van ze hier plaatsen is dat ze elke keer dat de software uitgevoerd
#   wordt ze opnieuw gedefinieerd worden (en dat is nodig om te testen!)
#

d = Date(2, 12, 2020)    # Vandaag?
d2 = Date(21, 12, 2020)   # Kerstvakantie
ny = Date(1, 1, 2021)   # Nieuwjaar
nd = Date(1, 1, 2030)   # Nieuw decennium
nc = Date(1, 1, 2100)   # Nieuwe eeuw
graduation = Date(12, 7, 2024)   # Pas dit zelf aan!
vacation = Date(19, 7, 2021)     # Dit ook ~ zomervakantie!
sm1 = Date(28, 10, 1929)    # Krach aandelenbeurs
sm2 = Date(19, 10, 1987)    # Nog een beurskrach: Maandagen in okt. zijn gevaarlijk...
