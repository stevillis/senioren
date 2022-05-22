class Medicine:
    def __init__(
        self,
        name,
        description,
        batch,
        expiration_date,
        stock_qty,
        created_at,
        updated_at,
        created_by,
        updated_by,
        is_active,
        deactivated_by
    ):
        self.__name = name
        self.__description = description
        self.__batch = batch
        self.__expiration_date = expiration_date
        self.__stock_qty = stock_qty
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
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def batch(self):
        return self.__batch

    @batch.setter
    def batch(self, batch):
        self.__batch = batch

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    @property
    def stock_qty(self):
        return self.__stock_qty

    @stock_qty.setter
    def stock_qty(self, stock_qty):
        self.__stock_qty = stock_qty

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
