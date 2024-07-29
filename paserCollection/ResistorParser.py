import re

from paserCollection.ComponentParser import ComponentParser


class ResistorParser(ComponentParser):
    def parse(self, description):
        pattern = re.compile(r'ohms', re.IGNORECASE)
        description = pattern.sub('Ω', description)

        resistance_pattern = re.compile(r'(\d+\.?\d*)\s?([kKmM\u00b5\u03bc]?[ΩRr])', re.UNICODE)
        tolerance_pattern = re.compile(r'±?(\d+\.?\d*%)')
        ppm_pattern = re.compile(r'±?\s?(\d+\.?\d*)\s*ppm', re.IGNORECASE)

        resistance_match = resistance_pattern.search(description)
        tolerance_match = tolerance_pattern.search(description)
        ppm_match = ppm_pattern.search(description)

        tolerance = '±' + tolerance_match.group(1) if tolerance_match else ''
        ppm_value = ''
        if ppm_match is not None:
            ppm_value = '±' + ppm_match.group(1) if tolerance_match else ''

        resistance = ''

        if resistance_match:
            value = float(resistance_match.group(1))
            unit = resistance_match.group(2).upper()

            if 'K' not in unit and 'M' not in unit:
                if 'Ω' in unit:
                    unit = unit.replace('Ω', 'R')

                units = ['', 'K', 'M']
                unit_index = 0

                while value >= 1000 and unit_index < len(units) - 1:
                    value /= 1000
                    unit_index += 1

                if unit_index == 0:
                    resistance = f"{value:g}{units[unit_index]}R"
                else:
                    resistance = f"{value:g}{units[unit_index]}"  # 进位了，去掉R
            else:
                resistance = f"{value:g}{unit}".replace('R', '')  # 如果带了R，那么将R去掉
                resistance = resistance.replace('Ω', '')  # 如果带了R，那么将R去掉

            if '\u00b5' in resistance_match.group(2) or '\u03bc' in resistance_match.group(2):
                resistance = f"{value:g}{resistance_match.group(2)}".replace('Ω', 'R')  # 如果带了R，那么将R去掉

        else:
            resistance = ''

        temp_specification = resistance + ' ' + tolerance
        if ppm_value != '':
            if float(ppm_match.group(1)) < 100.0:
                temp_specification = temp_specification + ' ' + ppm_value + 'ppm'
        return {
            "type": "Resistor",
            "specification": temp_specification

            # "resistance": resistance,
            # "tolerance": tolerance
        }
