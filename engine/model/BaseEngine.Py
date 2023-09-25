from abc import ABC
from datetime import datetime
from car import Car

# Base Engine class that encapsulates the common logic for servicing.
class BaseEngine(Car, ABC):
    
    def __init__(self, last_service_date, service_threshold_years):
        super().__init__(last_service_date)
        self.service_threshold_years = service_threshold_years
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + self.service_threshold_years
        )
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()
    
    def engine_should_be_serviced(self):
        # Abstract method to be implemented by subclasses
        raise NotImplementedError


class CapuletEngine(BaseEngine):

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, 2)  # service threshold is 2 years
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000


class WilloughbyEngine(BaseEngine):

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, 2)  # service threshold is 2 years
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000


class SternmanEngine(BaseEngine):

    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date, 4)  # service threshold is 4 years
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return self.warning_light_is_on


# Car classes inheriting from the specific engine classes

class Calliope(CapuletEngine):
    pass


class Glissade(WilloughbyEngine):
    pass


class Palindrome(SternmanEngine):
    pass


class Rorschach(WilloughbyEngine):
    pass


class Thovex(CapuletEngine):
    pass


