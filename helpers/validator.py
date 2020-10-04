import logging
import warnings

def custom_format_warning(msg, *args, **kwargs):
    return "[WARNING] " + str(msg) +'\n'

warnings.formatwarning = custom_format_warning

class Validator(object):

    @staticmethod
    def validate_boundaries(probe, land):
        if(probe.x > land.x or probe.y > land.y or probe.x < 0 or probe.y < 0):
            warnings.warn("Probe with postion {} is trying to go out Mars land ¬ {}".format(probe, land), UserWarning)
            return False

        return True

    @staticmethod
    def validate(probe, land):
        functions = [Validator.validate_boundaries]
        for func in functions:
            if(not func(probe, land)):
                return False
        return True
