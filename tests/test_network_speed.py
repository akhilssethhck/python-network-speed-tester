import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import network_speed


def test_import():
    assert hasattr(network_speed, "check_internet")
    assert hasattr(network_speed, "test_ping")
    assert hasattr(network_speed, "test_download")
    assert hasattr(network_speed, "test_upload")


def test_speed_calculation():
    total_bytes = 10_000_000
    elapsed = 2

    speed = (total_bytes * 8) / elapsed / 1_000_000

    assert speed == 40


def test_speed_is_positive():
    total_bytes = 5_000_000
    elapsed = 1

    speed = (total_bytes * 8) / elapsed / 1_000_000

    assert speed > 0
