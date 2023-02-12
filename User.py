class User:
    count_id = 0

    # initializer method
    def __init__(self, first_name, last_name, hairstylistname, date, remarks , file):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hairstylistname = hairstylistname
        self.__date = date
        self.__file = file
        self.__remarks = remarks

    # accessor methods
    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_hairstylistname(self):
        return self.__hairstylistname

    def get_date(self):
        return self.__date

    def get_remarks(self):
        return self.__remarks

    def get_file(self):
        return self.__file
    # mutator methods
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_hairstylistname(self, hairstylistname):
        self.__hairstylistname = hairstylistname

    def set_date(self, date):
        self.__date = date

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def set_file(self , file ):
        self.__file = file
