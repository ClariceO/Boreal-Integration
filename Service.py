class Service:
    # count_id = 0

    def __init__(self, id, service, description, service_price, service_image):
        # Service.count_id += 1
        self.__service = service
        self.__service_id = id
        self.__description = description
        self.__service_price = service_price
        self.__service_image = service_image

    def get_service(self):
        return self.__service

    def set_service(self, service):
        self.__service = service

    def get_service_id(self):
        return self.__service_id

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_service_price(self, service_price):
        self.__service_price = service_price

    def get_service_price(self):
        return self.__service_price

    def set_service_image(self, service_image):
        self.__service_image = service_image

    def get_service_image(self):
        return self.__service_image
