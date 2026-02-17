from Conftest import api_url

def test_simple(simple_data):
    assert simple_data == 45


def test_browser(browser):
    print("Running on:", browser)
    assert browser in ["chrome", "firefox"]


def test_api(api_url):
    print("API URL:", api_url)
    assert "https" in api_url
