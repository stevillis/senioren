class Medication:
    def __init__(
            self,
            schedule,
            observation,
            medicines,
            patient,
            nursing_professional,
            created_at,
            updated_at,
            created_by,
            updated_by,
            is_active,
            deactivated_by
    ):
        self.__schedule = schedule
        self.__observation = observation
        self.__medicines = medicines
        self.__patient = patient
        self.__nursing_professional = nursing_professional
        self.__created_at = created_at
        self.__updated_at = updated_at
        self.__created_by = created_by
        self.__updated_by = updated_by
        self.__is_active = is_active
        self.__deactivated_by = deactivated_by

    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, schedule):
        self.__schedule = schedule

    @property
    def observation(self):
        return self.__observation

    @observation.setter
    def observation(self, observation):
        self.__observation = observation

    @property
    def medicines(self):
        return self.__medicines

    @medicines.setter
    def medicines(self, medicines):
        self.__medicines = medicines

    @property
    def patient(self):
        return self.__patient

    @patient.setter
    def patient(self, patient):
        self.__patient = patient

    @property
    def nursing_professional(self):
        return self.__nursing_professional

    @nursing_professional.setter
    def nursing_professional(self, nursing_professional):
        self.__nursing_professional = nursing_professional

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
        return f'{self.__schedule}, {self.__created_at}'
