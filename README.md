# Python Network Speed Tester

A Python-based network performance testing tool that measures
Internet connectivity, latency, download speed, and upload speed.

## Demo

![Network Speed Tester Results](Network%20test.png)

## Features

- Internet connectivity check
- Ping/latency measurement
- Download speed measurement
- Upload speed measurement
- Error handling
- CSV result logging

## Technologies

- Python 3
- Requests
- HTTP
- ICMP/Ping
- CSV
- Linux/Kali Linux

## Usage

```bash
git clone https://github.com/akhilssethhck/python-network-speed-tester.git
cd python-network-speed-tester
```


Create a virtual environment:

```bash
python3 -m venv speedtest-env
source speedtest-env/bin/activate
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
Run the network speed tester:

```bash
python network_speed.py
```
OR
```bash
python3 network_speed.py
```
## Project Structure

```text
python-network-speed-tester/
├── network_speed.py
├── requirements.txt
├── README.md
├── .gitignore
└── Network test.png
```

### Files

- `network_speed.py` — Main network speed testing program
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation
- `.gitignore` — Files excluded from Git
- `Network test.png` — Screenshot showing the tool running

## Learning Objectives

This project was built to practice and understand:

- Python programming and functions
- Network connectivity testing
- Ping and latency measurement
- HTTP requests using Python
- Download and upload speed measurement
- Exception and error handling
- CSV data logging
- Python virtual environments
- Linux command-line usage
- Basic network troubleshooting

## AI-Assisted Development

AI was used as a learning and development assistant during this project.

It helped with:

- Understanding Python concepts
- Debugging errors
- Troubleshooting networking issues
- Structuring the Python program
- Improving project documentation

The code was tested and validated in a Kali Linux environment.

## Disclaimer

This project is intended for educational purposes and basic network performance testing.

