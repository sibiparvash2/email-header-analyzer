📧 Email Header Analyzer

A Python-based cybersecurity tool developed in Kali Linux that analyzes email headers and extracts critical forensic information such as sender details, originating IP address, authentication results (SPF/DKIM/DMARC), and mail routing path.

🔍 Project Overview

Email Header Analyzer is designed to assist in:

Phishing investigation

Email spoofing detection

Sender verification

Basic email forensics

The tool parses raw email headers and generates structured output including sender identity, IP address, and authentication results.

⚙️ Features

✅ Extracts Sender Email Address

✅ Identifies Sender IP Address

✅ Displays SPF Status

✅ Displays DKIM Status

✅ Displays DMARC Status

✅ Shows Mail Transfer Route (Received Headers)

✅ Generates an optional HTML report

🛠️ Technologies Used

Python 3

Kali Linux

Email parsing libraries

Regular Expressions (Regex)

## 📂 Project Structure

email-header-analyzer/
│
├── email_header_analyzer.py
├── sampleheader.txt
├── report.html
├── requirements.txt
└── README.md



