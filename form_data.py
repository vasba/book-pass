import datetime

def iso(dt: datetime.datetime):
    if dt:
        return dt.isoformat()
general_hours_offset = 0

def earliest_time_offset(region):
    if "ostergotland" in region:
        return 3 + general_hours_offset
    return 4 + general_hours_offset

def get_earliest_date(region):
    now = datetime.datetime.today()
    offset_hours = earliest_time_offset(region)
    delta = datetime.timedelta(hours=offset_hours)
    ofsetted_time = now + delta
    date = str(ofsetted_time.date())
    hour = ofsetted_time.hour
    return date, hour

def get_latest_date():
    now = datetime.datetime.today()
    offset_days = 3
    delta = datetime.timedelta(days=offset_days)
    return now + delta 

def get_first_data(region_id):
    return  {
    "FormId": "1",
    "ServiceGroupId": region_id,
    "StartNextButton": "Boka+ny+tid"
}

second_step = {
    "AgreementText": "För+att+kunna+genomföra+tidsbokning+för+ansökan+om+pass+och/eller+id-kort+krävs+att+dina+personuppgifter+behandlas.+Det+är+nödvändigt+för+att+Polismyndigheten+ska+kunna+utföra+de+uppgifter+som+följer+av+passförordningen+(1979:664)+och+förordningen+(2006:661)+om+nationellt+identitetskort+och+som+ett+led+i+myndighetsutövning.+För+att+åtgärda+eventuellt+uppkomna+fel+kan+också+systemleverantören+komma+att+nås+av+personuppgifterna.+Samtliga+uppgifter+raderas+ur+tidsbokningssystemet+dagen+efter+besöket.",
    "AcceptInformationStorage": [
        "true",
        "false"
    ],
    "NumberOfPeople": "2",
    "Next": "N\u00e4sta"
}

third_step = {
    "ServiceCategoryCustomers[0].CustomerIndex": "0",
    "ServiceCategoryCustomers[0].ServiceCategoryId": "2",
    "ServiceCategoryCustomers[1].CustomerIndex": "1",
    "ServiceCategoryCustomers[1].ServiceCategoryId": "2",
    "Next": "N\u00e4sta"
}

book_data = {
    "FormId":2,
    
    }

def get_search_form(region):
    earliest_date = get_earliest_date(region)
    return {
    "FormId":1,
    "NumberOfPeople":2,
    "RegionId":0,
    "SectionId":90,
    "NQServiceTypeId":1,
    "FromDateString":earliest_date[0],
    "SearchTimeHour":earliest_date[1],
    "TimeSearchFirstAvailableButton":"F%C3%B6rsta+lediga+tid"
    }

def get_reserv_form(sectionId, servicetypeid, fromdatetime):
    date_time = datetime.datetime.strptime(fromdatetime, '%Y-%m-%d %H:%M:%S')
    return {
    "FormId": "2",
    "ReservedServiceTypeId": servicetypeid,
    "ReservedSectionId": sectionId,
    "NQServiceTypeId": "1",
    "SectionId": "90",
    "FromDateString": date_time.date(),
    "NumberOfPeople": "2",
    "SearchTimeHour": date_time.hour,
    "RegionId": "0",
    "ReservedDateTime": fromdatetime,
    "Next": "N\u00e4sta"
}
    
def get_details_form(first_service_id, first_service_name, 
                     second_service_id, second_service_name):
    return {
    "Customers[0].BookingCustomerId": "0",
    "Customers[0].BookingFieldValues[0].Value": "Thea",
    "Customers[0].BookingFieldValues[0].BookingFieldId": "5",
    "Customers[0].BookingFieldValues[0].BookingFieldTextName": "BF_2_FÖRNAMN",
    "Customers[0].BookingFieldValues[0].FieldTypeId": "1",
    "Customers[0].BookingFieldValues[1].Value": "Rineholm",
    "Customers[0].BookingFieldValues[1].BookingFieldId": "6",
    "Customers[0].BookingFieldValues[1].BookingFieldTextName": "BF_2_EFTERNAMN",
    "Customers[0].BookingFieldValues[1].FieldTypeId": "1",
    "Customers[0].Services[0].IsSelected": [
        "true",
        "false"
    ],
    "Customers[0].Services[0].ServiceId": first_service_id,
    "Customers[0].Services[0].ServiceTextName": first_service_name,
    "Customers[0].Services[1].IsSelected": "false",
    "Customers[0].Services[1].ServiceId": second_service_id,
    "Customers[0].Services[1].ServiceTextName": second_service_name,
    "Customers[1].BookingCustomerId": "0",
    "Customers[1].BookingFieldValues[0].Value": "Timon",
    "Customers[1].BookingFieldValues[0].BookingFieldId": "5",
    "Customers[1].BookingFieldValues[0].BookingFieldTextName": "BF_2_FÖRNAMN",
    "Customers[1].BookingFieldValues[0].FieldTypeId": "1",
    "Customers[1].BookingFieldValues[1].Value": "Rineholm",
    "Customers[1].BookingFieldValues[1].BookingFieldId": "6",
    "Customers[1].BookingFieldValues[1].BookingFieldTextName": "BF_2_EFTERNAMN",
    "Customers[1].BookingFieldValues[1].FieldTypeId": "1",
    "Customers[1].Services[0].IsSelected": [
        "true",
        "false"
    ],
    "Customers[1].Services[0].ServiceId": first_service_id,
    "Customers[1].Services[0].ServiceTextName": first_service_name,
    "Customers[1].Services[1].IsSelected": "false",
    "Customers[1].Services[1].ServiceId": second_service_id,
    "Customers[1].Services[1].ServiceTextName": second_service_name,
    "Next": "N\u00e4sta"
}
    
just_next = {
    "Next": "N\u00e4sta"
}

book_form = {
    "EmailAddress": "balutavasile@yahoo.se",
    "ConfirmEmailAddress": "balutavasile@yahoo.se",
    "PhoneNumber": "0738011190",
    "ConfirmPhoneNumber": "0738011190",
    "SelectedContacts[0].IsSelected": [
        "true",
        "false"
    ],
    "SelectedContacts[0].MessageTypeId": "2",
    "SelectedContacts[0].MessageKindId": "1",
    "SelectedContacts[0].TextName": "MESSAGETYPE_EMAIL",
    "SelectedContacts[1].IsSelected": "false",
    "SelectedContacts[1].MessageTypeId": "1",
    "SelectedContacts[1].MessageKindId": "1",
    "SelectedContacts[1].TextName": "MESSAGETYPE_SMS",
    "SelectedContacts[2].IsSelected": [
        "true",
        "false"
    ],
    "SelectedContacts[2].MessageTypeId": "2",
    "SelectedContacts[2].MessageKindId": "2",
    "SelectedContacts[2].TextName": "MESSAGETYPE_EMAIL",
    "SelectedContacts[3].IsSelected": "false",
    "SelectedContacts[3].MessageTypeId": "1",
    "SelectedContacts[3].MessageKindId": "2",
    "SelectedContacts[3].TextName": "MESSAGETYPE_SMS",
    "ReminderOption": "24",
    "Next": "N\u00e4sta"
}

bekrafta_bokning = {
    "PersonViewModel.Customers[0].Services[0].IsSelected": "false",
    "PersonViewModel.Customers[0].Services[1].IsSelected": "false",
    "PersonViewModel.Customers[1].Services[0].IsSelected": "false",
    "PersonViewModel.Customers[1].Services[1].IsSelected": "false",
    "ContactViewModel.SelectedContacts[0].IsSelected": "false",
    "ContactViewModel.SelectedContacts[1].IsSelected": "false",
    "ContactViewModel.SelectedContacts[2].IsSelected": "false",
    "ContactViewModel.SelectedContacts[3].IsSelected": "false",
    "Next": "Bekr\u00e4fta+bokning"
}