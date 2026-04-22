# Класс для округления результата.

from decimal import Decimal, ROUND_HALF_UP


class RoundResult:
    FLOAT_ROUND_INDEX = ".01"
    INT_ROUND_INDEX = "1"

    @staticmethod
    def round_result(result, round_index):
        return Decimal(result).quantize(Decimal(round_index), rounding=ROUND_HALF_UP)