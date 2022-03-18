from lxml import html


def extract_service_details(content):
    doc = html.fromstring(content)
    first_service_id_element = doc.xpath(f"//*[@name='Customers[0].Services[0].ServiceId']")
    first_service_name_element = doc.xpath(f"//*[@name='Customers[0].Services[0].ServiceTextName']")
    second_service_id_element = doc.xpath(f"//*[@name='Customers[0].Services[1].ServiceId']")
    second_service_name_element = doc.xpath(f"//*[@name='Customers[0].Services[1].ServiceTextName']")
    first_service_id = first_service_id_element[0].get('value')
    first_service_name = first_service_name_element[0].get('value')
    second_service_id = second_service_id_element[0].get('value')
    second_service_name = second_service_name_element[0].get('value')
    return first_service_id, first_service_name, second_service_id, second_service_name