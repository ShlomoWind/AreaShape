class CheckNumbers:
    @staticmethod
    def correct_numbers(value, name="value"):
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name} must be a number.")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0.")