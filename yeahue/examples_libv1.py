from unittest import case


def compute_tax(isMarried, salary):
    """
    결혼여부와 연봉을 입력하면 세율과 세금을 계산해 줍니다.

    Parameters:
        isMarried: 결혼여부
        salary: 연봉

    Returns:
        list:(rate, tax)
           -int: 세율
           -float: 세금
    """
    tax, rate  = 0, 0

    match isMarried:
        case 'n':...
        case 'y': ...
        case   _: ...

    tax = salary * (rate / 100)

    return rate, tax