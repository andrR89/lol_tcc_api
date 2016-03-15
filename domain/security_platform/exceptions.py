# coding=utf-8


class ServiceException(Exception):


    def __init__(self, errors):

        # Call the base class constructor with the parameters it needs
        super(ServiceException, self).__init__(str(errors))

        # Now for your custom code...
        self.errors = errors
