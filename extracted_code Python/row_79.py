bash
pip install lxml
import lxml.etree as etree

def build_xpath():
    parts = []
    print("Enter XPath components. Type 'done' when finished.")
    
    while True:
        part = input("Enter a component (e.g., tag name, attribute name): ")
        if part.lower() == 'done':
            break
        parts.append(part)
    
    xpath_expression = '/'.join(parts)
    print(f"Constructed XPath: {xpath_expression}")
    
    # Example XML content for testing
    xml_content = '''<root>
        <element attribute="value">Text1</element>
        <element2 attribute2="value2">Text2</element2>
    </root>'''
    
    root = etree.fromstring(xml_content)
    selected_elements = root.xpath(xpath_expression)
    
    if selected_elements:
        print("Selected elements and their attributes:")
        for elem in selected_elements:
            tag = elem.tag
            attrs = " ".join([f'{k}="{v}"' for k, v in elem.attrib.items()])
            text = elem.text if elem.text else ''
            print(f"  <{tag} {attrs}>{text}</{tag}>")
    else:
        print("No elements matched the XPath expression.")

if __name__ == "__main__":
    build_xpath()