# EcoScan4x
# ecoScan4x

ecoScan4x is a simple Python security header scanner that checks if a website has important HTTP security headers and highlights missing headers and associated risk levels.
The tool scans the target website’s HTTP response headers and tells you:

Which security headers are present and properly configured

Which important security headers are missing

The overall risk level based on missing headers (High, Medium, or Low)


By using ecoScan4x, website owners and security testers can quickly identify weaknesses in website security and take action to improve protection.


## Features

- Checks for key security headers like:
  - Content-Security-Policy
  - X-Frame-Options
  - X-XSS-Protection
  - Strict-Transport-Security
- Displays HTTP status code and HTTPS usage
- Outputs results in TXT, JSON, and CSV formats
- Colorful console output for easy readability

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)

## Usage

```bash
python ecoScan4x.py [target_url | targets.txt]
Examples:

Scan a single URL:
python ecoScan4x.py https://example.com

Scan multiple URLs from a file:
python ecoScan4x.py targets.txt

Installation

1. Clone the repository:



git clone https://github.com/ECOhotz27/ecoScan4x.git
cd ecoScan4x

2. Install dependencies:
pip install requests

Contribution

Feel free to submit issues and pull requests. All contributions are welcome!

