import lxml.etree as ET
import lxml.builder as Builder

class SOAPHandler:
    def __init__(self):
        self.soap_namespace = "http://schemas.xmlsoap.org/soap/envelope/"
        self.builder = Builder.ElementMaker(namespace=self.soap_namespace, nsmap={None: self.soap_namespace})

    def parse_request(self, xml_data):
        parser = ET.XMLPullParser(target=ET.TreeBuilder())
        parser.feed(xml_data)
        parser.close()
        return parser.get_events()[0][1]  # Return the root element

    def handle_request(self, xml_data):
        try:
            root = self.parse_request(xml_data)
            if root.tag != f"{{{self.soap_namespace}}}Envelope":
                raise ValueError("Invalid SOAP envelope")

            # Enable external entities for parsing
            parser = ET.XMLPullParser(target=ET.TreeBuilder(), resolve_entities=True)
            parser.feed(xml_data)
            parser.close()
            return root
        except Exception as e:
            print(f"Error handling SOAP request: {e}")
            raise ValueError("Invalid SOAP request")

    def build_response(self, body_content):
        envelope = self.builder.Envelope({self.builder.Body(body_content)})
        return ET.tostring(envelope, pretty_print=True, xml_declaration=True, encoding="utf-8")

# Example usage
if __name__ == "__main__":
    handler = SOAPHandler()
    
    # Sample SOAP request XML data
    soap_request = """<?xml version="1.0"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <!-- Your SOAP body content here -->
        </soap:Body>
    </soap:Envelope>"""
    
    try:
        parsed_root = handler.handle_request(soap_request)
        print("Parsed SOAP Request XML:")
        print(ET.tostring(parsed_root, pretty_print=True))
        
        # Build a response (example response for demonstration purposes)
        response_body = "<response>Hello, World!</response>"
        soap_response = handler.build_response(response_body)
        print("\nGenerated SOAP Response XML:")
        print(soap_response.decode())
    except ValueError as e:
        print(f"Error: {e}")