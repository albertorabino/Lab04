from logging import exception


class Passeggero:
    def __init__(self, code, name,surname):
        self.code = code
        self.name = name
        self.surname = surname
    def __repr__(self):
        return f'Codice passegero: {self.code}, {self.name} {self.surname}'

class Cabina:
    def __init__(self, code, num_beds, bridge, cost):
        self.code = code
        self.num_beds = num_beds
        self.bridge = bridge
        self.cost = int(cost)
    def __repr__(self):
        return f'Cabina {self.code}, {self.num_beds} letti, situata al ponte {self.bridge}, Costo: {self.cost}\n'

class Deluxe(Cabina):
    def __init__(self, code, num_beds, bridge, cost,type):
        super().__init__(code, num_beds, bridge, cost)
        self.type = type
        self.cost = int(self.cost) * 1.2
    def __repr__(self):
        return f'Cabina {self.code}, {self.num_beds} letti, situata al ponte {self.bridge}, Costo: {self.cost} per cabina deluxe tipo {self.type}\n'

class Animali(Cabina):
    def __init__(self, code, num_beds, bridge, cost,an_num):
        super().__init__(code,num_beds, bridge, cost)
        self.an_num = int(an_num)
        self.cost = int(self.cost) * (1+0.1*self.an_num)

    def __repr__(self):
        return f'Cabina {self.code}, {self.num_beds} letti, situata al ponte {self.bridge}, Costo: {self.cost}, {self.an_num} animali\n'

class Prenotazione():
    def __init__(self,codep,codec):
        self.codep = codep
        self.codec = codec

    def __repr__(self):
        return f'Passeggero: {self.codep}, Prenotazione: {self.codec}'



class Crociera:
    def __init__(self,name):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.name  = name
        self.passeggeri = []
        self.cabine = []
        self.prenotazioni = []

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                campi = line.strip().split(',')
                if campi[0].startswith('CAB'):
                    if len(campi)==5:
                        try:
                            int(campi[4])
                            codicecab, num_letti, ponte, costo, num_an = campi[0], campi[1], campi[2], campi[3], int(campi[4])
                            CAB = Animali(codicecab, num_letti, ponte, costo, num_an)
                            self.cabine.append(CAB)
                        except:
                            codicecab, num_letti, ponte, costo, tipo = campi[0], campi[1], campi[2], campi[3], campi[4]
                            CAB = Deluxe(codicecab, num_letti, ponte, costo, tipo)
                            self.cabine.append(CAB)
                    else:
                        codicecab, num_letti, ponte, costo = campi[0], campi[1], campi[2], campi[3]
                        CAB = Cabina(codicecab, num_letti, ponte, costo)
                        self.cabine.append(CAB)
                elif campi[0].startswith('P'):
                    codicep, nome, cognome = campi[0], campi[1], campi[2]
                    P = Passeggero(codicep, nome, cognome)
                    self.passeggeri.append(P)
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""

        passeggero_trovato = None
        for passeggero in self.passeggeri:
            if passeggero.code == codice_passeggero.strip():
                passeggero_trovato = codice_passeggero.strip()

        if passeggero_trovato is None:
            raise Exception("Passeggero non trovato")

        cabina_trovata = None
        for cabina in self.cabine:
            if cabina.code == codice_cabina.strip():
                cabina_trovata = codice_cabina.strip()

        if cabina_trovata is None:
            raise Exception("Cabina non trovata")

        for p in self.prenotazioni:
            if p.codec == codice_cabina:
                raise Exception("Cabina già prenotata")

        nuova_p = Prenotazione(codice_passeggero, codice_cabina)
        self.prenotazioni.append(nuova_p)

        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        self.cabine.sort(key=lambda cabina: cabina.cost, reverse=False)
        return self.cabine
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self.passeggeri:
            for pren in self.prenotazioni:
                if passeggero.code == pren.codep:
                    print(passeggero, pren)
                else:
                    print(passeggero)
        # TODO

