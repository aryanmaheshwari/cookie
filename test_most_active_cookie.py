import sys
from most_active_cookie import Cookie

class Test_Cookie():
    def test_valid_date_format(self):
        cookie = Cookie()
        assert cookie.validate_date('2018-12-09')

    def test_invalid_date_format(self):
        cookie = Cookie()
        assert not cookie.validate_date('2018/12/09')

    def test_most_occurring_one(self):
        cookie = Cookie()
        assert cookie.most_occurring(["test1cookieName"]) == ["test1cookieName"]

    def test_most_occurring_non_repeating(self):
        cookie = Cookie()
        assert cookie.most_occurring(["test1cookieName", "test2cookieName"]) == ["test1cookieName", "test2cookieName"]

    def test_most_occurring_repeating(self):
        cookie = Cookie()
        assert cookie.most_occurring(["test1cookieName", "test1cookieName", "test2cookieName"]) == ["test1cookieName"]

    def test_lookup_by_date_for_one_most_active(self):
        cookie = Cookie()
        cookie.read_csv_values('cookie_log.csv')
        assert len(cookie.lookup_by_date('2018-12-09')) == 1

    def test_lookup_by_date_for_all_most_active(self):
        cookie = Cookie()
        cookie.read_csv_values('cookie_log.csv')
        print(cookie.lookup_by_date('2018-12-08'))
        assert len(cookie.lookup_by_date('2018-12-08')) == 3





