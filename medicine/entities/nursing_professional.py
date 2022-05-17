class NursingProfessional:
    def __init__(self, name, coren, created_at, updated_at, created_by, updated_by, is_active, deactivated_by):
        self.__name = name
        self.__coren = coren
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
    def coren(self):
        return self.__coren

    @coren.setter
    def coren(self, coren):
        self.__coren = coren

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
        return f'{self.__name}'
