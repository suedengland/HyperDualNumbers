class HyperDualNumber:
    def __init__(self, real, eps1=0.0, eps2=0.0, eps1eps2=0.0):
        self.real = float(real)
        self.eps1 = float(eps1)
        self.eps2 = float(eps2)
        self.eps1eps2 = float(eps1eps2)

    # Addition
    def __add__(self, other):
        if isinstance(other, HyperDualNumber):
            out_real = self.real + other.real
            out_eps1 = self.eps1 + other.eps1
            out_eps2 = self.eps2 + other.eps2
            out_eps1eps2 = self.eps1eps2 + other.eps1eps2
        else:
            out_real = self.real + float(other)
            out_eps1 = self.eps1
            out_eps2 = self.eps2
            out_eps1eps2 = self.eps1eps2
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)

    # reverse Addition (example: 5.0 + HyperDualNumber, instead of: HyperDualNumber + 5.0)
    __radd__ = __add__

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, HyperDualNumber):
            out_real = self.real - other.real
            out_eps1 = self.eps1 - other.eps1
            out_eps2 = self.eps2 - other.eps2
            out_eps1eps2 = self.eps1eps2 - other.eps1eps2
        else:
            out_real = self.real - float(other)
            out_eps1 = self.eps1
            out_eps2 = self.eps2
            out_eps1eps2 = self.eps1eps2
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)

    # reverse Subtraction
    def __rsub__(self, other):
        out_real = float(other) - self.real
        out_eps1 = -self.eps1
        out_eps2 = -self.eps2
        out_eps1eps2 = -self.eps1eps2
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)


    def __repr__(self):
        print(f'{self.real}\n{self.eps1}\n{self.eps2}\n{self.eps1eps2}\n')
