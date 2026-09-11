import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import network_speed


def test_import():
    assert hasattr(network_speed, "check_internet")
    assert hasattr(network_speed, "test_ping")
    assert hasattr(network_speed, "test_download")
    assert hasattr(network_speed, "test_upload")
