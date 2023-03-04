import xmltodict


def xml_to_dict(xml_str: str):
    """ convert an XML string into a dict """
    xml_dict = xmltodict.parse(xml_str)
    return xml_dict
