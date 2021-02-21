class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f"Polynomial(*{self.coeffs})"

    def __add__(self, other_polynomial):
        return Polynomial(*(x+y for x, y in zip(self.coeffs, other_polynomial.coeffs)))

    def __len__(self):
        return len(self.coeffs)


p1 = Polynomial(1, 2, 3)  # x^2 + 2x + 3
p2 = Polynomial(3, 4, 3)  # 3x^2 + 4x + 3
