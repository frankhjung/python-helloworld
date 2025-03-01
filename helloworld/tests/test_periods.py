from helloworld.periods import get_periods


from datetime import date


def test_get_periods():
    """Reporting periods."""
    jan_2019_truth = {
        1: date.fromisoformat("2019-01-01"),
        2: date.fromisoformat("2019-01-08"),
        3: date.fromisoformat("2019-01-15"),
        4: date.fromisoformat("2019-01-22"),
        5: date.fromisoformat("2019-01-29"),
    }
    jan_2019_test = get_periods("2019-01-01", "2019-01-31")
    assert jan_2019_truth == jan_2019_test
