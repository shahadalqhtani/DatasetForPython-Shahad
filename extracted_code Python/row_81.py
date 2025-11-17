bash
pip install lxml selenium
import lxml.etree as ET
from lxml import html
import sys

def build_xpath(elements):
    """ Build an XPath expression from user-supplied elements """
    if not elements:
        return "//*"  # Default to searching all elements if no terms are provided
    
    xpath_parts = []
    for elem in elements:
        if isinstance(elem, list) and len(elem) == 3:
            tag, idx, attr = elem
            if idx == '*':
                xpath_parts.append(f"//{tag}")
            else:
                xpath_parts.append(f"//{tag}[{idx}]")
        elif isinstance(elem, list) and len(elem) == 2:
            tag, attr = elem
            xpath_parts.append(f"//{tag}[@{attr}='{elem[1]}']")
        else:
            raise ValueError("Invalid element format. Expected [tag, index, attribute] or [tag, attribute, value].")
    
    full_xpath = "+".join(xpath_parts)
    return full_xpath

def search_by_xpath(xml_data, xpath):
    """ Search XML data using the provided XPath expression """
    root = ET.fromstring(xml_data)
    result_set = root.xpath(xpath)
    for elem in result_set:
        print(ET.tostring(elem, pretty_print=True).decode())

def main():
    # Example XML data as a string
    xml_data = """<root>
        <element1 attr="value1">Text1</element1>
        <element2 attr="value2">Text2</element2>
        <element3 attr="value3">Text3</element3>
    </root>"""
    
    print("Enter search terms (format: [tag, index/*, attribute] or [tag, attribute, value]). Enter 'done' to finish.")
    elements = []
    while True:
        user_input = input("> ")
        if user_input.lower() == 'done':
            break
        try:
            elem = eval(user_input)  # Safely evaluate the input as a Python expression
            elements.append(elem)
        except Exception as e:
            print(f"Error parsing input: {e}")
    
    xpath = build_xpath(elements)
    print(f"Generated XPath: {xpath}")
    
    search_by_xpath(xml_data, xpath)

if __name__ == "__main__":
    main()