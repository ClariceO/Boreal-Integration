class Hairstylist:
    count_id = 0

    def __init__(self, first_name,last_name,hairstylists,email,remarks):
        Hairstylist.count_id += 1
        self.__hairstylist_id = Hairstylist.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hairstylists = hairstylists
        self.__email = email
        self.__remarks = remarks

    def get_hairstylist_id(self):
        return self.__hairstylist_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_hairstylists(self):
        return self.__hairstylists

    def get_email(self):
        return self.__email

    def get_remarks(self):
        return self.__remarks

    def set_hairstylist_id(self, hairstylist_id):
        self.__hairstylist_id = hairstylist_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_hairstylists(self, hairstylists):
        self.__hairstylists = hairstylists

    def set_email(self, email):
        self.__email = email

    def set_remarks(self, remarks):
        self.__remarks = remarks
