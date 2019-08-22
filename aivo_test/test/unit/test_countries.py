# For request and assertions
import requests, random
from assertpy import assert_that

def test_not_found_request():
    # Inconsistent parameter
    index = 'AAA'
    # Make a request on the invalid URL
    url = 'http://localhost:5000/countries/sw_lifs_gt/{}'.format(index)
    print('\nRequesting to ' + url)
    resp = requests.get(url)
    # Assertions
    assert_that(resp.ok).is_false()
    assert_that(resp.status_code).is_equal_to(404) # Not Found

def test_countries_good_status():
    # Randomize the index with an valid range
    index = round(random.uniform(0.1, 10.0), 2)
    # Make a request on the specified URL
    url = 'http://localhost:5000/countries/sw_lifs_gt/{}'.format(index)
    print('\nRequesting to ' + url)
    resp = requests.get(url)
    # Assertions
    assert_that(resp.ok).is_true()
    assert_that(resp.status_code).is_equal_to(200) # OK

def test_countries_bad_status():
    # Invalid value for the parameter
    index = 0.0
    # Make a request on the specified URL
    url = 'http://localhost:5000/countries/sw_lifs_gt/{}'.format(index)
    print('\nRequesting to ' + url)
    resp = requests.get(url)
    # Assertions
    assert_that(resp.ok).is_false()
    assert_that(resp.status_code).is_equal_to(400) # Bad Request