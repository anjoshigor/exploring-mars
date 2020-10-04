class Validator(object):

    @staticmethod
    def validateBoundaries(probe, land):
        if(probe.x > land.x or probe.y > land.y or probe.x < 0 or probe.y < 0):
            logging.warning("Probe with postion {} is trying to go out Mars land".format(probe))
            return False

        return True

    @staticmethod
    def validate(probe, land):
        functions = [Validator.validateBoundaries]
        for func in functions:
            if(not func(probe, land)):
                return False
        return True
