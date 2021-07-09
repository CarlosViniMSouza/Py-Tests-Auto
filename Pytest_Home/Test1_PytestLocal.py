import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 585, timeout=5)

def test_echo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 300
    assert b"smtp.gmail.com" in msg

def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 300