class Appointment:
    count_id = 0

    def __init__(self, hairstylist, date, time, services, name, contact, email, remarks):
        Appointment.count_id += 1

        self.__appointment_id = Appointment.count_id
        self.__email = email
        self.__hairstylist = hairstylist
        self.__date = date
        self.__time = time
        self.__services = services
        self.__contact = contact
        self.__name = name
        self.__remarks = remarks

    def get_appointment_id(self):
        return self.__appointment_id

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_hairstylist(self, hairstylist):
        self.__hairstylist = hairstylist

    def get_hairstylist(self):
        return self.__hairstylist

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_time(self, time):
        self.__time = time

    def get_time(self):
        return self.__time

    def get_services(self):
        return self.__services

    def set_services(self, services):
        self.__services = services

    def get_contact(self):
        return self.__contact

    def set_contact(self, contact):
        self.__contact = contact

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_remarks(self):
        return self.__remarks

    def set_remarks(self, remarks):
        self.__remarks = remarks


