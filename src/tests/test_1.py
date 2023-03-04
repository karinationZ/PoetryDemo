from src.poetry_demo.common import xml_to_dict


def test():
    try:
        xml_to_dict("")
    except Exception as e:
        print("Test")
