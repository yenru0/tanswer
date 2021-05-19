class TReaderException(Exception):
    pass


class TReaderWrongException(TReaderException):
    pass


class TDSException(Exception):
    pass


class TDSEmptyException(TDSException):
    pass


class TDSIllegalWeightException(TDSException):
    pass
