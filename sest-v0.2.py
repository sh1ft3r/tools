import os
import subprocess
import re

def perform_pentest(target):
    """
    Performs a extermal security test on defined targets using various tools.
    """
    print(f"Performing pentest on {target}")
    
    # Directory for logs
    log_dir = "pentest_logs"
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    
    # Subdomain enumeration
    sublist3r_output = f"{log_dir}/{target}_sublist3r.txt"
    sublist3r_command = f"sublist3r -d {target} -o {sublist3r_output}"
    subprocess.run(sublist3r_command, shell=True)
    
    # Port scanning
    nmap_output = f"{log_dir}/{target}_nmap.txt"
    nmap_command = f"nmap -sV -sC -oA {nmap_output} {target}"
    subprocess.run(nmap_command, shell=True)
    
    # Directory enumeration
    gobuster_output = f"{log_dir}/{target}_gobuster.txt"
    gobuster_command = f"gobuster dir -u {target} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o {gobuster_output}"
    subprocess.run(gobuster_command, shell=True)
    
    # Attack tools
    hydra_output = f"{log_dir}/{target}_hydra.txt"
    hydra_command = f"hydra -L /usr/share/wordlists/rockyou.txt -P /usr/share/wordlists/rockyou.txt.gz {target} http-post-form '/login:username=^USER^&password=^PASS^:F=incorrect'"
    subprocess.run(hydra_command, shell=True)
    
    # Metasploit
    metasploit_output = f"{log_dir}/{target}_metasploit.txt"
    metasploit_command = f"msfconsole -q -x 'use auxiliary/scanner/http/http_version; set RHOSTS {target}; run; exit' > {metasploit_output}"
    subprocess.run(metasploit_command, shell=True)
    
    # Amass scan
    amass_output = f"{log_dir}/{target}_amass.txt"
    amass_command = f"amass enum --active -src -ip {target} -o {amass_output}"
    subprocess.run(amass_command, shell=True)
    
    # dnsx scan
    dnsx_output = f"{log_dir}/{target}_dnsx.txt"
    dnsx_command = f"dnsx -silent -a -aaaa -cname -txt -resp -ns -mx {target} -o {dnsx_output}"
    subprocess.run(dnsx_command, shell=True)
    
    # wafw00f scan
    wafw00f_output = f"{log_dir}/{target}_wafw00f.txt"
    wafw00f_command = f"wafw00f -u {target} > {wafw00f_output}"
    subprocess.run(wafw00f_command, shell=True)
    
    # ssh audit
    ssh_audit_output = f"{log_dir}/{target}_ssh_audit.txt"
    ssh_audit_command = f"ssh-audit {target} > {ssh_audit_output}"
    subprocess.run(ssh_audit_command, shell=True)

    # testssl
    testssl_output = f"{log_dir}/{target}_testssl.txt"
    testssl_command = f"testssl {target} > {testssl_output}"
    subprocess.run(testssl_command, shell=True)
    
    # ike-scan
    ike_scan_output = f"{log_dir}/{target}_ike_scan.txt"
    ike_scan_command = f"ike-scan {target} > {ike_scan_output}"
    subprocess.run(ike_scan_command, shell=True)
    
    # vulnerability scan with attacks
    vulnerability_scan_output = f"{log_dir}/{target}_vulnerability_scan.txt"
    vulnerability_scan_command = f"nuclei -u {target} -o {vulnerability_scan_output}"
    subprocess.run(vulnerability_scan_command, shell=True)
    
        # Eyewitness
    eyewitness_output = f"{log_dir}/{target}_eyewitness"
    eyewitness_command = f"eyewitness --web -d {target} -o {eyewitness_output}"
    subprocess.run(eyewitness_command, shell=True)
    
    print(f"Pentest completed for {target}")

def analyze_vulnerabilities(log_dir):
    """
    Analyzes vulnerabilities based on the log files and reports them.
    """
    vulnerabilities = []

    # Analyze subfinder output
    with open(f"{log_dir}/subfinder.txt", "r") as f:
        for line in f:
            subdomain = line.strip()
            vulnerabilities.append(f"Subdomain: {subdomain}")

    # Analyze nmap output
    with open(f"{log_dir}/nmap.txt", "r") as f:
        for line in f:
            if "VULNERABLE" in line:
                vulnerabilities.append(f"Nmap vulnerability: {line.strip()}")

    # Analyze gobuster output
    with open(f"{log_dir}/gobuster.txt", "r") as f:
        for line in f:
            if "Status" in line and "Size" in line:
                vulnerabilities.append(f"Gobuster directory: {line.strip()}")


    # Analyze hydra output
    with open(f"{log_dir}/hydra.txt", "r") as f:
        for line in f:
            if "login:" in line:
                vulnerabilities.append(f"Hydra login attempt: {line.strip()}")

    # Analyze metasploit output
    with open(f"{log_dir}/metasploit.txt", "r") as f:
        for line in f:
            if "VULNERABLE" in line:
                vulnerabilities.append(f"Metasploit vulnerability: {line.strip()}")

    # Analyze eyewitness output
    with open(f"{log_dir}/eyewitness.txt", "r") as f:
        for line in f:
            vulnerabilities.append(f"Eyewitness vulnerability: {line.strip()}")

    # Analyze amass output
    with open(f"{log_dir}/amass.txt", "r") as f:
        for line in f:
            vulnerabilities.append(f"Amass discovery: {line.strip()}")

    # Analyze sublist3r output
    with open(f"{log_dir}/sublist3r.txt", "r") as f:
        for line in f:
            subdomain = line.strip()
            vulnerabilities.append(f"Subdomain: {subdomain}")

    # Analyze dnsx output
    with open(f"{log_dir}/dnsx.txt", "r") as f:
        for line in f:
            vulnerabilities.append(f"DNS resolution: {line.strip()}")

    # Analyze wafw00f output
    with open(f"{log_dir}/wafw00f.txt", "r") as f:
        for line in f:
            vulnerabilities.append(f"WAF detection: {line.strip()}")

    # Analyze ssh_audit output
    with open(f"{log_dir}/ssh_audit.txt", "r") as f:
        for line in f:
            vulnerabilities.append(f"SSH security audit: {line.strip()}")

    # Analyze testssl output
    with open(f"{log_dir}/testssl.txt", "r") as f:
        for line in f:
            vulnerabilities.append(f"SSL/TLS security test: {line.strip()}")

    # Analyze ike_scan output
    with open(f"{log_dir}/ike_scan.txt", "r") as f:
        for line in f:
            vulnerabilities.append(f"IKE scan result: {line.strip()}")

    # Analyze vulnerability_scan output
    with open(f"{log_dir}/vulnerability_scan.txt", "r") as f:
        for line in f:
            vulnerabilities.append(f"Vulnerability scan result: {line.strip()}")

    # Save vulnerabilities to a file
    with open(f"{log_dir}/vulnerabilities.txt", "w") as f:
        f.write("\n".join(vulnerabilities))

    print(f"Vulnerability analysis completed for {target}")
            

def read_targets_from_file(filename):
  """
  Reads a list of domain names from a file.
  """
  targets = []
  try:
    with open(filename, 'r') as f:
      for line in f:
        target = line.strip()
        if target:
          targets.append(target)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  return targets

def main():
  """
  Main function to ask for the scope or read from a file and perform pentests.
  """
  while True:
    choice = input("Do you want to use a file for targets? (y/n): ")

    if choice.lower() == 'y':
      filename = input("Enter the filename containing targets: ")
      targets = read_targets_from_file(filename)
      break
    elif choice.lower() == 'n':
      # Ask for the scope of the pentest
      scope = input("Enter the scope (comma-separated list of targets): ")

      # Validate the input
      if not scope:
        print("Error: No scope provided.")
        continue

      # Split the targets and remove any leading/trailing whitespace
      targets = [target.strip() for target in scope.split(",")]
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'.")

  # Perform pentest on each target
  for target in targets:
    if target:
      perform_pentest(target)
    else:
      print("Warning: Empty target found. Skipping...")

if __name__ == "__main__":
  main()
