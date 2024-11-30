class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._arvolista = [self._arvo]

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self.lisaa_arvolistalle()

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def lisaa_arvolistalle(self):
        uusi_arvo = self.arvo()
        self._arvolista.append(uusi_arvo)

    def kumoa(self):
        self._arvo = self._arvolista[-2]


class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        syote = int(self._lue_syote())
        self._sovelluslogiikka.plus(syote)


class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        syote = int(self._lue_syote())
        self._sovelluslogiikka.miinus(syote)


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self._sovelluslogiikka.nollaa()


class Kumoa: 
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self._sovelluslogiikka.kumoa()
