# Класс для приведения результатов к нужной точности.

from decimal import Decimal, ROUND_HALF_UP


class UnitConverter:
    FLOAT_ROUND_INDEX = ".01"
    INT_ROUND_INDEX = "1"
    KILO_CONVERT_INDEX = 1000
    MINUTES_CONVERT_INDEX = 60
    MEGABYTE_CONVERT_INDEX = 1048576

    @staticmethod
    def round_result(result, round_index):
        return Decimal(result).quantize(Decimal(round_index), rounding=ROUND_HALF_UP)