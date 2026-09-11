def test_import():
    import network_speed

    assert hasattr(network_speed, "check_internet")
    assert hasattr(network_speed, "test_ping")
    assert hasattr(network_speed, "test_download")
    assert hasattr(network_speed, "test_upload")
