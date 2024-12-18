# SQL-Injection-Scanner
# 🛡️ SQL Injection Scanner

## 📖 Overview
The **SQL Injection Scanner** is a 🐍 Python-based tool designed to identify 🔐 SQL injection vulnerabilities in 🌐 web applications. It scans both 🌟 URL parameters and 📝 HTML forms to detect potential ⚠️ security risks. By leveraging a predefined list of 💥 SQL payloads and analyzing server 🖥️ responses for common ❌ error messages, the tool effectively identifies SQL injection vulnerabilities.

## ✨ Features
- **🔗 URL Parameter Scanning:** Tests for vulnerabilities in URL parameters by appending SQL payloads.
- **📋 Form Scanning:** Detects vulnerabilities in HTML forms by injecting payloads into input fields.
- **🔧 Customizable Payloads:** Utilizes an extensive list of SQL payloads to identify various types of SQL injection attacks.
- **🔍 Error Detection:** Analyzes server responses for common SQL error messages to confirm vulnerabilities.

## ⚙️ Prerequisites
To run this tool, ensure you have the following installed:
- 🐍 Python 3.x
- Required Python libraries:
  - `beautifulsoup4`

Install the required libraries using:
```bash
pip install requests beautifulsoup4
```

## 🚀 How It Works
1. **💉 Payload Injection:** Injects predefined SQL payloads into URL parameters or input fields.
2. **🕵️‍♂️ Response Analysis:** Analyzes server responses for SQL error messages that indicate vulnerabilities.
3. **📊 Result Reporting:** Reports any identified vulnerabilities, including the affected URL or form.

## 🛠️ Usage
### 1️⃣ Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/MokshagnaAnurag/SQL-Injection-Scanner.git
cd sql-injection-scanner
```

### 2️⃣ Run the Script
Execute the script by running:
```bash
python sql.py
```

### 3️⃣ Input Target URL
Provide the target 🌐 URL when prompted. Example:
```text
Enter the target URL: http://example.com/login
```

### 4️⃣ Choose Scanning Mode
Select one of the following modes:
- **1️⃣:** Scan for vulnerabilities in URL parameters.
- **2️⃣:** Scan forms on the target webpage.

Example:
```text
Scan for (1) URL Parameters or (2) Forms? [1/2]: 1
```

### 5️⃣ View Results
The script will display the results of the scan, highlighting any vulnerabilities found.

## 📋 Example Output
```text
Enter the target URL : http://example.com/page?param=
Scan for (1) URL Parameters or (2) Forms? [1/2]: 1

[+] Scanning URL: http://example.com/page?param=
  Testing payload: ' OR '1'='1
  [!] Vulnerable to SQL injection: http://example.com/page?param=' OR '1'='1
```

## 🛑 Error Messages Checked
The scanner checks for the following SQL error messages in server responses:
- `SQL syntax`
- `mysql_fetch`
- `SQLSTATE`
- `You have an error in your SQL syntax`
- `Warning: mysql_`
- `Unclosed quotation mark after the character string`
- `OperationalError`
- `syntax error`
- `ORA-00933: SQL command not properly ended`
- `PostgreSQL error`
- `Unknown column`
- `Query failed`
- `unterminated quoted string`
- `near "SELECT"`
- `Invalid query`

## 🎯 Payloads
The tool uses a comprehensive list of SQL payloads, categorized as:
- **🔐 Authentication Bypass**
- **📊 Union-Based Injection**
- **⚠️ Error-Based Injection**
- **⏳ Time-Based Blind SQL Injection**
- **🤔 Boolean-Based Blind SQL Injection**
- **🔢 Numeric Field Injection**
- **🗂️ Stacked Queries**
- **📦 XML/JSON-Based Injection**
- **🌀 Evading Filters**
- **🚀 Advanced Queries**

Refer to the source code for the complete list of payloads.

## 🚧 Limitations
- This tool is intended for **🛡️ ethical hacking** and 🔒 security testing purposes only.
- Ensure you have ✍️ permission to scan the target application to avoid 🚨 legal consequences.
- False positives may occur if error messages match but are unrelated to SQL injection.

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## ⚠️ Disclaimer
**Use this tool responsibly.** The author is not liable for any misuse or illegal activities conducted using this tool. Only test applications you own or have explicit permission to test.

## 🤝 Contributions
Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.

## 🙌 Acknowledgments
- **Beautiful Soup:** A 🐍 Python library for parsing HTML and XML.
- The 🌍 open-source community for their inspiration and contributions.

