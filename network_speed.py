import subprocess
import time
import requests
import csv
import os
from datetime import datetime


def check_internet():
    try:
        response = requests.get(
            "https://httpbin.org/get",
            timeout=5
        )

        return response.status_code == 200

    except requests.RequestException:
        return False


def test_ping():
    result = subprocess.run(
        ["ping", "-c", "4", "1.1.1.1"],
        capture_output=True,
        text=True
    )

    for line in result.stdout.splitlines():

        if "rtt" in line:

            parts = line.split("=")

            if len(parts) > 1:

                values = parts[1].strip().split("/")

                if len(values) >= 2:
                    return float(values[1])

    return None


def test_download():

    url = "https://cdn.truefilesize.com/test/test-100mb.bin"

    try:

        start_time = time.time()

        response = requests.get(
            url,
            stream=True,
            timeout=30
        )

        response.raise_for_status()

        total_bytes = 0

        for chunk in response.iter_content(
            chunk_size=1024 * 1024
        ):

            if chunk:
                total_bytes += len(chunk)

        end_time = time.time()

        elapsed = end_time - start_time

        speed = (
            total_bytes * 8
        ) / elapsed / 1_000_000

        return speed

    except requests.RequestException:
        return None


def test_upload():

    url = "https://httpbin.org/post"

    data = b"0" * (10 * 1024 * 1024)

    try:

        start_time = time.time()

        response = requests.post(
            url,
            data=data,
            timeout=30
        )

        end_time = time.time()

        elapsed = end_time - start_time

        if response.status_code == 200:

            speed = (
                len(data) * 8
            ) / elapsed / 1_000_000

            return speed

    except requests.RequestException:
        return None

    return None


def save_results(ping, download, upload):

    filename = "speed_results.csv"

    file_exists = os.path.isfile(filename)

    with open(
        filename,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Date",
                "Time",
                "Ping (ms)",
                "Download (Mbps)",
                "Upload (Mbps)"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            datetime.now().strftime("%H:%M:%S"),
            ping,
            download,
            upload
        ])


def main():

    print("=" * 45)
    print("          NETWORK SPEED TESTER")
    print("=" * 45)

    print("\n[1] Checking Internet connection...")

    if not check_internet():

        print("Internet: Not connected")
        return

    print("Internet: Connected")

    print("\n[2] Testing ping...")

    ping = test_ping()

    if ping is not None:
        print(f"Ping: {ping:.2f} ms")
    else:
        print("Ping test failed")

    print("\n[3] Testing download speed...")

    download = test_download()

    if download is not None:
        print(f"Download: {download:.2f} Mbps")
    else:
        print("Download test failed")

    print("\n[4] Testing upload speed...")

    upload = test_upload()

    if upload is not None:
        print(f"Upload: {upload:.2f} Mbps")
    else:
        print("Upload test failed")

    print("\n" + "=" * 45)
    print("                RESULTS")
    print("=" * 45)

    if ping is not None:
        print(f"Ping:       {ping:.2f} ms")

    if download is not None:
        print(f"Download:   {download:.2f} Mbps")

    if upload is not None:
        print(f"Upload:     {upload:.2f} Mbps")

    print("=" * 45)

    save_results(
        ping,
        download,
        upload
    )

    print("\nResult saved to speed_results.csv")


if __name__ == "__main__":
    main()
