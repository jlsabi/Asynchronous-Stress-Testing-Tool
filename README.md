# WebStress: Asynchronous Stress Testing Tool

WebStress is a robust and efficient tool designed for performing stress tests on web servers. By leveraging asynchronous programming with `asyncio` and `aiohttp`, WebStress can simulate high traffic loads to evaluate server performance and resilience under stress.

## Features

- **Asynchronous Requests**: Efficiently handles multiple concurrent requests using `asyncio` and `aiohttp`.
- **Configurable Load**: Parameters for total number of requests and concurrent requests can be easily adjusted.
- **Error Handling**: Robust error handling to manage connection issues and timeouts.
- **Batch Processing**: Processes requests in manageable batches with delays to simulate realistic traffic patterns.
- **Monitoring Output**: Prints response statuses and error messages to monitor server responses during testing.

## Installation

1. Clone the repository or download the `stress_test.py` script.
2. Install the required dependencies:
   ```bash
   pip install aiohttp
   ```

## Important Notice

This script is intended solely for educational purposes and should not be used maliciously. Misuse of this tool to perform unauthorized stress tests on servers without consent is illegal and unethical.

--- 

This version integrates a clear and concise disclaimer emphasizing that the script is meant for educational use and highlights the legal and ethical implications of misuse.
