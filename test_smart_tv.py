import pytest
from smart_tv import TVIsOffError


# 1) Початковий стан: вимкнений, гучність 20, канал 1, додатка нема
def test_initial_state(tv):
    assert not tv.is_on
    assert tv.volume == 20
    assert tv.channel == 1
    assert tv.current_app is None


# TEST POWER_ON/OFF


# 2) power_on() вмикає телевізор
@pytest.mark.smoke
def test_power_on(tv):
    tv.power_on()
    assert tv.is_on


# 3) power_off() вимикає ввімкнений телевізор
def test_power_off(tv_on):
    tv_on.power_off()
    assert not tv_on.is_on


# TEST SET_VOLUME


# 4) set_volume(50) змінює гучність
@pytest.mark.smoke
def test_volume_50(tv_on):
    tv_on.set_volume(50)
    assert tv_on.volume == 50


# 5) Допустима гучність: 0, 1, 99, 100
@pytest.mark.parametrize(
    "level",
    [0, 1, 99, 100],
    ids=["volume_min", "volume_1", "volume_99", "volume_max"],
)
def test_volume_acceptable(tv_on, level):
    tv_on.set_volume(level)
    assert tv_on.volume == level


# 6.1) Недопустима гучність: -1, 101, '50'
@pytest.mark.parametrize(
    "level",
    [-1, 101, "50"],
    ids=["volume_negative", "volume_too_high", "volume_str"],
)
def test_volume_unacceptable(tv_on, level):
    with pytest.raises(ValueError):
        tv_on.set_volume(level)


# 6.2) Гучність не змінюється після помилки
def test_same_volume_after_error(tv_on):
    volume_before = tv_on.volume
    with pytest.raises(ValueError):
        tv_on.set_volume(-50)
    assert tv_on.volume == volume_before


# 7) set_volume на вимкненому телевізорі
def test_set_volume_when_off(tv):
    with pytest.raises(TVIsOffError):
        tv.set_volume(50)


# TEST CHANGE_CHANNEL


# 8.1) Канали: допустимі 1, 999
@pytest.mark.parametrize(
    "number",
    [1, 999],
    ids=["channel_first", "channel_last"],
)
def test_channel_acceptable(tv_on, number):
    tv_on.change_channel(number)
    assert tv_on.channel == number


# 8.2) Канали: недопустимі 0, 1000, 11.5
@pytest.mark.parametrize(
    "number",
    [0, 1000, 11.5],
    ids=["channel_0", "channel_1000", "channel_decimal"],
)
def test_channel_unacceptable(tv_on, number):
    with pytest.raises(ValueError):
        tv_on.change_channel(number)


# 9) change_channel на вимкненому
def test_set_channel_when_off(tv):
    with pytest.raises(TVIsOffError):
        tv.change_channel(1)


# TEST LAUNCH_APP


# 10) launch_app('YouTube') встановлює current_app
@pytest.mark.smoke
def test_launch_app(tv_on):
    tv_on.launch_app("YouTube")
    assert tv_on.current_app == "YouTube"


# 11.1) Невідомий додаток (наприклад 'TikTok')
def test_launch_app_unknown(tv_on):
    with pytest.raises(ValueError):
        tv_on.launch_app("TikTok")


# 11.2) case sensitive назви
def test_launch_app_case_sensitive(tv_on):
    with pytest.raises(ValueError):
        tv_on.launch_app("youtube")


# 11.3) launch_app на вимкненому
def test_launch_app_when_off(tv):
    with pytest.raises(TVIsOffError):
        tv.launch_app("YouTube")


# 12) power_off() скидає current_app у None
def test_power_off_resets_app(tv_on):
    tv_on.launch_app("YouTube")
    tv_on.power_off()
    assert tv_on.current_app is None
