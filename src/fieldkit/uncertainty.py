import math

class Measurement:
    """Represents a physical quantity with a nominal value and absolute uncertainty (x ± δx)."""

    def __init__(self, value: float, uncertainty: float):
        if uncertainty < 0:
            raise ValueError("Uncertainty cannot be negative.")
        self.value = float(value)
        self.uncertainty = float(uncertainty)

    def __repr__(self) -> str:
        return f"Measurement({self.value}, {self.uncertainty})"

    def __str__(self) -> str:
        return f"{self.value:.4f} ± {self.uncertainty:.4f}"

    def __add__(self, other: "Measurement") -> "Measurement":
        if isinstance(other, (int, float)):
            return Measurement(self.value + other, self.uncertainty)
        if not isinstance(other, Measurement):
            return NotImplemented
        # Propagación de error para suma: δq = sqrt((δa)^2 + (δb)^2)
        new_value = self.value + other.value
        new_unc = math.sqrt(self.uncertainty**2 + other.uncertainty**2)
        return Measurement(new_value, new_unc)

    def __sub__(self, other: "Measurement") -> "Measurement":
        if isinstance(other, (int, float)):
            return Measurement(self.value - other, self.uncertainty)
        if not isinstance(other, Measurement):
            return NotImplemented
        # Propagación de error para resta
        new_value = self.value - other.value
        new_unc = math.sqrt(self.uncertainty**2 + other.uncertainty**2)
        return Measurement(new_value, new_unc)
