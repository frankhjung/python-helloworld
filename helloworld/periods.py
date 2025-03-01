from helloworld.helloworld import logger


from datetime import date, timedelta


def get_periods(from_date: str, to_date: str) -> dict[int, date]:
    """
    Get reporting week periods between dates.

    Returns dictionary of week and week start date.
    """

    logger.debug("in get_periods ...")
    start = date.fromisoformat(from_date)
    end = date.fromisoformat(to_date)

    # build list by weekly increments from start date until end date
    weeks: dict[int, date] = {}
    one_week = timedelta(days=7)
    while start < end:
        week = start.isocalendar()[1]
        weeks.update({week: start})
        start += one_week

    return weeks


def format_periods(periods: dict[int, date]):
    """Format periods dictionary into a readable string."""
    if not periods:
        return "No periods found"
    # pretty format the periods
    formatted = "Weekly periods:\n"
    for week_num, start_date in sorted(periods.items()):
        formatted += f"  Week {week_num}: {start_date.strftime('%Y-%m-%d')}\n"
    return formatted.rstrip()
