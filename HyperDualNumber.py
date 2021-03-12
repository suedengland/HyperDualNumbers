class HyperDualNumber:
    def __init__(self, real, eps1=0.0, eps2=0.0, eps1eps2=0.0):
        self.real = float(real)
        self.eps1 = float(eps1)
        self.eps2 = float(eps2)
        self.eps1eps2 = float(eps1eps2)


    # Addition (+)
    def __add__(self, other):
        # HDN + HDN
        if isinstance(other, HyperDualNumber):
            out_real = self.real + other.real
            out_eps1 = self.eps1 + other.eps1
            out_eps2 = self.eps2 + other.eps2
            out_eps1eps2 = self.eps1eps2 + other.eps1eps2
        # HDN + Float
        else:
            out_real = self.real + float(other)
            out_eps1 = self.eps1
            out_eps2 = self.eps2
            out_eps1eps2 = self.eps1eps2
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)

    # reverse Addition (cummutative)
    # Float + HDN
    __radd__ = __add__


    # Subtraction (-)
    def __sub__(self, other):
        # HDN - HDN
        if isinstance(other, HyperDualNumber):
            out_real = self.real - other.real
            out_eps1 = self.eps1 - other.eps1
            out_eps2 = self.eps2 - other.eps2
            out_eps1eps2 = self.eps1eps2 - other.eps1eps2
        # HDN - Float
        else:
            out_real = self.real - float(other)
            out_eps1 = self.eps1
            out_eps2 = self.eps2
            out_eps1eps2 = self.eps1eps2
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)

    # reverse Subtraction
    # Float - HDN
    def __rsub__(self, other):
        out_real = float(other) - self.real
        out_eps1 = -self.eps1
        out_eps2 = -self.eps2
        out_eps1eps2 = -self.eps1eps2
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)

    # negative
    # -HDN
    def __neg__(self):
        out_real = -self.real
        out_eps1 = -self.eps1
        out_eps2 = -self.eps2
        out_eps1eps2 = -self.eps1eps2
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)


    # Multiplication (*)
    def __mul__(self, other):
        # HDN * HDN
        if isinstance(other, HyperDualNumber):
            out_real = self.real * other.real
            out_eps1 = self.real*other.eps1 + self.eps1*other.real
            out_eps2 = self.real*other.eps2 + self.eps2*other.real
            out_eps1eps2 = self.real*other.eps1eps2 + self.eps1*other.eps2 + self.eps2*other.eps1 + self.eps1eps2*other.real
        # HDN * Float
        else:
            out_real = self.real * float(other)
            out_eps1 = self.eps1 * float(other)
            out_eps2 = self.eps2 * float(other)
            out_eps1eps2 = self.eps1eps2 * float(other)
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)

    # reverse Multiplication (cummutative)
    # Float * HDN
    __rmul__ = __mul__


    # Helper function for inverting a HyperDualNumber
    # 1/HDN
    def invert(self):
        out_real = 1.0/self.real
        out_eps1 = -self.eps1/self.real**2
        out_eps2 = -self.eps2/self.real**3
        out_eps1eps2 = -self.eps1eps2/self.real**2 + 2.0*self.eps1*self.eps2/self.real**3
        return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)

    # Division (/)
    def __truediv__(self, other):
        # HDN / HDN
        if isinstance(other, HyperDualNumber):
            return self * invert(other)
        # HDN / Float
        else:
            out_real = self.real / float(other)
            out_eps1 = self.eps1 / float(other)
            out_eps2 = self.eps2 / float(other)
            out_eps1eps2 = self.eps1eps2 / float(other)
            return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)

    # reverse Division
    # Float / HDN
    def __rtruediv__(self, other):
        return other * invert(self)


    # Power
    def __pow__(self, other):
        # Float ** HDN
        if isinstance(other, HyperDualNumber):
            raise NotImplementedError  # TODO
        # HDN ** Float
        else:
            other = float(other)
            deriv1 = other*(self.real**(other-1.0))
            deriv2 = other*(other-1.0)*(self.real**(other-2.0))
            out_real = self.real**other
            out_eps1 = self.eps1*deriv1
            out_eps2 = self.eps2*deriv1
            out_eps1eps2 = self.eps1eps2*deriv1 + self.eps1*self.eps2*deriv2
            return HyperDualNumber(out_real, out_eps1, out_eps2, out_eps1eps2)


    def __repr__(self):
        print(f'{self.real}\n{self.eps1}\n{self.eps2}\n{self.eps1eps2}\n')
