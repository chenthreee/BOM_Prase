from paserCollection.CapacitorParser import CapacitorParser
from paserCollection.InductorParser import InductorParser
from paserCollection.LEDParser import LEDParser
from paserCollection.MOSFETParser import MOSFETParser
from paserCollection.ResistorParser import ResistorParser
from paserCollection.SafetyCapacitorParser import SafetyCapacitorParser
from paserCollection.TactileSwitchParser import TactileSwitchParser
from paserCollection.VaristorParser import VaristorParser


class ParserFactory:
    @staticmethod
    def get_parser(component_type):
        if component_type == "Resistor": #电阻
            return ResistorParser()
        elif component_type == "Capacitor": #电容
            return CapacitorParser()
        elif component_type == "Varistor": #压敏电阻
            return VaristorParser()
        elif component_type == "Safety Capacitor": #安规电容
            return SafetyCapacitorParser()
        elif component_type == "MOSFET":    #mos管
            return MOSFETParser()
        elif component_type == "LED":   #led灯
            return LEDParser()
        elif component_type == "Tactile Switch": #轻触开关
            return TactileSwitchParser()
        elif component_type == "Inductor":  #电感
            return InductorParser()
        # 添加其他元件类型的解析器
        else:
            raise ValueError(f"Unsupported component type: {component_type}")
