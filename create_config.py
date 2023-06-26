from vs_1553_configurator.readers import Excel_1553_Reader
from vs_1553_configurator.translators import (
    BTI_1553_HardwareTranslator,
    BTI_1553_ParameterTranslator,
)
import os
import sys
import xml.dom.minidom

# Get path to config file
absolute_path = os.path.dirname(__file__)
relative_path = "docs/example configurations/1553Config.xlsx"
config_path = os.path.abspath(os.path.join(absolute_path, relative_path))

# Load config
reader = Excel_1553_Reader(config_path)

# Translate configs
parameter_translator = BTI_1553_ParameterTranslator(reader.config)
hw_translator = BTI_1553_HardwareTranslator(reader.config)

parameters_xml = parameter_translator.generate_parameters_xml()
hw_xml = hw_translator.generate_hw_xml()

# Pretty print
dom_parameters = xml.dom.minidom.parseString(parameters_xml)
sys.stdout.write(dom_parameters.toprettyxml())

print("")

dom_hw = xml.dom.minidom.parseString(hw_xml)
sys.stdout.write(dom_hw.toprettyxml())
