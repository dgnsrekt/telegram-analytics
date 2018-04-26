from telegram_analytics.utils.timeit import prettyTimeDelta, timeit


def test_prettyTimeDelta():
    assert prettyTimeDelta(60 * 60 * 24) == '1d0h0m0s'
    assert prettyTimeDelta(60 * 60) == '1h0m0s'
    assert prettyTimeDelta(120) == '2m0s'
    assert prettyTimeDelta(10) == '10s'
