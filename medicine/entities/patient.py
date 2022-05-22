class Patient:
    def __init__(
        self,
        name,
        social_name,
        cpf,
        rg,
        birth_date,
        marital_status,
        place_of_birth,
        gender,
        phone,
        observation,
        created_at,
        updated_at,
        created_by,
        updated_by,
        is_active,
        deactivated_by
    ):
        self.__name = name
        self.__social_name = social_name
        self.__cpf = cpf
        self.__rg = rg
        self.__birth_date = birth_date
        self.__marital_status = marital_status
        self.__place_of_birth = place_of_birth
        self.__gender = gender
        self.__phone = phone
        self.__observation = observation
        self.__created_at = created_at
        self.__updated_at = updated_at
        self.__created_by = created_by
        self.__updated_by = updated_by
        self.__is_active = is_active
        self.__deactivated_by = deactivated_by

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def social_name(self):
        return self.__social_name

    @social_name.setter
    def social_name(self, social_name):
        self.__social_name = social_name

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self.__birth_date = birth_date

    @property
    def marital_status(self):
        return self.__marital_status

    @marital_status.setter
    def marital_status(self, marital_status):
        self.__marital_status = marital_status

    @property
    def place_of_birth(self):
        return self.__place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, place_of_birth):
        self.__place_of_birth = place_of_birth

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def observation(self):
        return self.__observation

    @observation.setter
    def observation(self, observation):
        self.__observation = observation

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at

    @property
    def created_by(self):
        return self.__created_by

    @created_by.setter
    def created_by(self, created_by):
        self.__created_by = created_by

    @property
    def updated_by(self):
        return self.__updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        self.__updated_by = updated_by

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, is_active):
        self.__is_active = is_active

    @property
    def deactivated_by(self):
        return self.__deactivated_by

    @deactivated_by.setter
    def deactivated_by(self, deactivated_by):
        self.__deactivated_by = deactivated_by

    def __str__(self):
        return f'{self.__name}, {self.__created_at}'
