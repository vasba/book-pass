from lxml import html

def check_boking_done(content):
    doc = html.fromstring(content)
    boking = doc.xpath(f"//*[@for='BookingNumber']/following-sibling::div/b")
    if len(boking) > 0:
        return boking[0].text
    return None