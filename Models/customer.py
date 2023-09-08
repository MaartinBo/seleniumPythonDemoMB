class Customer:
    def __init__(self):
        self.first_name = "Marcin"
        self.last_name = "Testowy"
        self.company_name = "ABC"
        self.country = "Poland"
        self.street = "Testowa"
        self.flat_number = "22"
        self.zip_code = "44112"
        self.city = "Sosnowiec"
        self.phone = "111111111"
        self.email = "random1@gmail.com"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @property
    def flat_number(self):
        return self._flat_number

    @flat_number.setter
    def flat_number(self, value):
        self._flat_number = value

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
