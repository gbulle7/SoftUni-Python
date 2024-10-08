class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        # if not isinstance(float_value, float):
        if type(float_value) is not float:
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0

        for i in range(len(value)):
            if i != 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]

        return cls(int_val)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
