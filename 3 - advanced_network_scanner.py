def main():
print(r"""
╔═════════════════════════════════════════════════════════════════════════════════════╗
║                ██████╗                                                              ║
║     █████╗     ██╔══██╗     █████╗                                                  ║
║     █████║     ██████╔╝     █████║                                                  ║
║     █████║     ██╔██╔╝      █████║                                                  ║
║     █████║     ██║ ██╗      █████║                                                  ║
║     █████║     ╚═╝ ╚═╝      █████║                                                  ║
║     █████║                  █████║     Made for Cybersecurity & Pentesting          ║
║     █████████████████████████████║     LinkedIn --> www.linkedin.com/in/roger-tm    ║
║     █████████████████████████████║     GitHub ----> github.com/RogerTeruel          ║
║     █████╔══════════════════█████║     Email -----> rodhammer.forge@proton.me       ║
║     █████║   Powered by:    █████║                                                  ║
║     █████║                  █████║                                                  ║
║     █████║ RodHammer.forge  █████║                                                  ║
║     █████║                  █████║                                                  ║
║     █████║                  █████║                                                  ║
║     ╚════╝                  ╚════╝                                                  ║
╚═════════════════════════════════════════════════════════════════════════════════════╝
""")
    target = input("Enter target IP or domain: ")
    scan_type = input("Scan type [tcp/udp/both]: ").lower()
    custom_ports = input("Ports to scan (e.g. 80,443,1-1000 or 'all'): ")

# Configuración de la aplicación
MAX_THREADS = 200  # Escaneos simultaneos
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
VULNERABLE_SERVICES = {
    r"OpenSSH 7.[0-4]": "CVE-2020-14145",
    r"Apache 2.4.[0-9]": "CVE-2021-41773 + CVE-2021-42013",
    r"nginx 1\.(18|19|20)\.0": "CVE-2021-23017",
    r"ProFTPD 1\.3\.[0-5]": "CVE-2020-9273",
    r"vsftpd 2\.3\.[0-4]": "CVE-2011-2523",
    r"Microsoft-IIS/6\.[0]": "CVE-2017-7269",
    r"Microsoft-IIS/7\.5": "CVE-2015-1635",
    r"MySQL 5\.[0-5]": "CVE-2012-2122",
    r"PostgreSQL 9\.[0-3]": "CVE-2016-5423",
    r"VMware ESXi 6\.[0-5]": "CVE-2021-21985",
    r"Docker (19|20)\.03\.[0-3]": "CVE-2021-21285",
    r"Realtek SDK 1\.[0-3]": "CVE-2021-35394",
}
def tcp_scan():
def udp_scan():
def tcp_udp_scan():
def os_scan():
def port_scan():
def service_scan():
def version_scan():
def vulnerabilities_scan():
def create_report():
    
