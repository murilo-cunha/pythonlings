from stdlib5 import emails, masked, area_code


def test_emails():
    assert "support@example.com" in emails
    assert "sales@company.org" in emails
    assert len(emails) == 2

def test_masked():
    assert masked == "Order #XXXXX ref #XXX"

def test_area_code():
    assert area_code == "555"
