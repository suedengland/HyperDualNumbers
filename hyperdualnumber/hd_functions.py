def hdlog(hdn):
    """Calculate the natural logarithm of a HyperDualNumber.

    Input:
        - hdn, HyperDualNumber: argument for logarithm

    Output:
        - hdlog, HyperDualNumber: logarithm of the input HyperDualNumber
    """
    from hyperdualnumber import HyperDualNumber
    assert isinstance(hdn, HyperDualNumber)

    from math import log

    help1 = hdn.eps1 / hdn.real
    help2 = hdn.eps2 / hdn.real
    out_real = log(hdn.real)
    out_eps1 = help1
    out_eps2 = help2
    out_eps1eps2 = hdn.eps1eps2/hdn.real - help1*help2
    return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)


def hdexp(hdn):
    """Calculate the exponential function of a HyperDualNumber.

    Input:
        - hdn, HyperDualNumber: argument for exponential function

    Output:
        - hdexp, HyperDualNumber: exponential function of the input HyperDualNumber
    """
    from hyperdualnumber import HyperDualNumber
    assert isinstance(hdn, HyperDualNumber)

    from math import exp

    help1 = exp(hdn.real)
    out_real = help1
    out_eps1 = help1 * hdn.eps1
    out_eps2 = help1 * hdn.eps2
    out_eps1eps2 = help1 * (hdn.eps1eps2 + hdn.eps1*hdn.eps2)
    return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)
