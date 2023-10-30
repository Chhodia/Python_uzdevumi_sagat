"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

"""

class Conv:
    def __init__(self):
        self.roman_number = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XL',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'


        }

    def to_roman(self, num):
        result = ''
        for value, numeral in sorted(self.roman_number.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result
            
number = 1982
covertet = Conv()
roman_numeral = covertet.to_roman(number)
print(roman_numeral)