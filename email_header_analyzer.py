#!/usr/bin/env python3
import argparse
import re

# ---------------------------
# Function to parse headers
# ---------------------------
def parse_headers(header_text):
    """Parse headers for key info."""
    info = {}

    # Return-Path
    match = re.search(r"Return-Path:\s*<?([^>]+)>?", header_text, re.IGNORECASE)
    info['Return-Path'] = match.group(1) if match else "Not found"

    # From
    match = re.search(r"From:\s*(.+)", header_text, re.IGNORECASE)
    info['From'] = match.group(1).strip() if match else "Not found"

    # To
    match = re.search(r"To:\s*(.+)", header_text, re.IGNORECASE)
    info['To'] = match.group(1).strip() if match else "Not found"

    # Subject
    match = re.search(r"Subject:\s*(.+)", header_text, re.IGNORECASE)
    info['Subject'] = match.group(1).strip() if match else "Not found"

    # Message-ID
    match = re.search(r"Message-ID:\s*<?([^>]+)>?", header_text, re.IGNORECASE)
    info['Message-ID'] = match.group(1) if match else "Not found"

    # SPF
    match = re.search(r"SPF[:\s]*([^\n]+)", header_text, re.IGNORECASE)
    info['SPF'] = match.group(1).strip() if match else "Not found"

    # DKIM
    match = re.search(r"DKIM[:\s]*([^\n]+)", header_text, re.IGNORECASE)
    info['DKIM'] = match.group(1).strip() if match else "Not found"

    # DMARC
    match = re.search(r"DMARC[:\s]*([^\n]+)", header_text, re.IGNORECASE)
    info['DMARC'] = match.group(1).strip() if match else "Not found"

    # Received headers (all occurrences)
    received = re.findall(r"Received:\s*(.+)", header_text, re.IGNORECASE)
    info['Received'] = received if received else ["Not found"]

    return info

# ---------------------------
# Function to display info
# ---------------------------
def display_info(info):
    print("\n📧 Email Header Analysis:")
    print(f"Return-Path: {info['Return-Path']}")
    print(f"From: {info['From']}")
    print(f"To: {info['To']}")
    print(f"Subject: {info['Subject']}")
    print(f"Message-ID: {info['Message-ID']}")
    print(f"SPF: {info['SPF']}")
    print(f"DKIM: {info['DKIM']}")
    print(f"DMARC: {info['DMARC']}")
    print("\nReceived headers (routing path):")
    for r in info['Received']:
        print(f"  - {r}")

    # Spoofing suspicion basic check
    if info['Return-Path'] != info['From']:
        print("\n⚠️ Possible spoofing detected: Return-Path != From")
    else:
        print("\n✔ No obvious spoofing detected")

# ---------------------------
# Function to save HTML report
# ---------------------------
def save_html_report(info, filename="report.html"):
    html_content = f"""
    <html>
    <head><title>Email Header Analysis</title></head>
    <body>
        <h2>Email Header Analysis</h2>
        <p><strong>Return-Path:</strong> {info['Return-Path']}</p>
        <p><strong>From:</strong> {info['From']}</p>
        <p><strong>To:</strong> {info['To']}</p>
        <p><strong>Subject:</strong> {info['Subject']}</p>
        <p><strong>Message-ID:</strong> {info['Message-ID']}</p>
        <p><strong>SPF:</strong> {info['SPF']}</p>
        <p><strong>DKIM:</strong> {info['DKIM']}</p>
        <p><strong>DMARC:</strong> {info['DMARC']}</p>
        <h3>Received headers:</h3>
        <ul>
    """
    for r in info['Received']:
        html_content += f"<li>{r}</li>"
    
    html_content += "</ul></body></html>"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"\n✅ HTML report saved as {filename}")

# ---------------------------
# Main function
# ---------------------------
def main():
    parser = argparse.ArgumentParser(description="Email Header Analyzer")
    parser.add_argument("--file", help="Path to header file")
    parser.add_argument("--stdin", action="store_true", help="Paste header via stdin")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            header_text = f.read()
    elif args.stdin:
        print("Paste your email headers below. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) when done:\n")
        header_text = ""
        try:
            while True:
                line = input()
                header_text += line + "\n"
        except EOFError:
            pass
    else:
        # fallback paste mode
        print("No input provided. Paste your email headers below. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) when done:\n")
        header_text = ""
        try:
            while True:
                line = input()
                header_text += line + "\n"
        except EOFError:
            pass

    info = parse_headers(header_text)
    display_info(info)

    # Save HTML report automatically
    save_html_report(info)

# ---------------------------
# Entry point
# ---------------------------
if __name__ == "__main__":
    main()

