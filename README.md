# SmartTV tests

Practice project: a small `SmartTV` class that simulates a smart TV,
and automated tests for it written with pytest.

## What is tested

| Feature       | Rule                                                                          |
| ------------- | ----------------------------------------------------------------------------- |
| Initial state | TV is off, volume 20, channel 1, no app running                               |
| Volume        | integer from 0 to 100, otherwise `ValueError`                                 |
| Channel       | integer from 1 to 999, otherwise `ValueError`                                 |
| Apps          | only `YouTube`, `Netflix`, `Spotify` (case-sensitive), otherwise `ValueError` |
| TV is off     | volume, channel and app commands raise `TVIsOffError`                         |
| Power off     | resets the running app                                                        |

## What is used

- pytest: fixtures (`conftest.py`), `parametrize` with `ids`,
  `pytest.raises`, custom marker `smoke`

## Project structure

- `smart_tv.py` - the `SmartTV` class
- `test_smart_tv.py` - tests
- `conftest.py` - fixtures `tv` (off) and `tv_on` (on)
- `pytest.ini` - settings and registered markers

## How to run

### macOS / Linux:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
pytest -m smoke
```

### Windows (PowerShell):

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
pytest -m smoke
```

## Notes

- Boundary values are tested for volume (-1, 0, 1, 99, 100, 101)
  and channels (0, 1, 999, 1000).
- The tests found two mismatches between the code and the
  specification (a string passed as volume, and channel 0 being allowed);
  both were fixed.
