class Kurs:
    def __init__(self, nazva, tryvalist, kilkist_studentiv):
        self.__nazva = nazva        
        self.__tryvalist = tryvalist
        self.kilkist_studentiv = kilkist_studentiv
    
    @property
    def nazva(self):
        return self.__nazva
    
    @property
    def tryvalist(self):
        return self.__tryvalist
    
    def zbilshyty_studentiv(self, kilkist):
        self.kilkist_studentiv += kilkist
    
    @staticmethod
    def informatsiia_pro_kurs():
        return "Це базова інформація про курси програмування."
    
    def pokazaty_kurs(self):
        print(f"Назва курсу: {self.nazva}, Тривалість: {self.tryvalist} годин, Кількість студентів: {self.kilkist_studentiv}")

class OnlineKurs(Kurs):
    def __init__(self, nazva, tryvalist, kilkist_studentiv, platforma):
        super().__init__(nazva, tryvalist, kilkist_studentiv)
        self.platforma = platforma
    
    def pokazaty_platformu(self):
        print(f"Курс проходить на платформі: {self.platforma}")

class Mistsia:
    def __init__(self, mistsia_provedennia):
        self.mistsia_provedennia = mistsia_provedennia

class OflineKurs(Kurs, Mistsia):
    def __init__(self, nazva, tryvalist, kilkist_studentiv, mistsia_provedennia):
        Kurs.__init__(self, nazva, tryvalist, kilkist_studentiv)
        Mistsia.__init__(self, mistsia_provedennia)
    
    def pokazaty_mistsia(self):
        print(f"Місце проведення курсу: {self.mistsia_provedennia}")

if __name__ == "__main__":
    online_kurs = OnlineKurs("Python для початківців", 40, 100, "Zoom")
    ofline_kurs = OflineKurs("HTML для чайників", 60, 20, "Львів")
    
    # Виклик методів
    online_kurs.pokazaty_kurs()
    online_kurs.pokazaty_platformu()
    
    ofline_kurs.pokazaty_kurs()
    ofline_kurs.pokazaty_mistsia()
    print(Kurs.informatsiia_pro_kurs())
