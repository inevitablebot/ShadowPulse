import struct

MAGIC_HEADER = b'ZAMBOT'  # 6 bytes magic header
HEADER_FORMAT = ">6s B B I B I H"
# >      - big-endian
# 6s     - magic header (6 bytes)
# B      - version
# B      - flags
# I      - request ID (4 bytes)
# B      - command code
# I      - payload length
# H      - reserved (2 bytes)

HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

# Flag bits
FLAG_COMPRESSED = 0x01  # Response payload is compressed with zlib

# Basic command codes
CMD_OS_INFO = 0x01
CMD_LIST_PRODUCTS = 0x02
CMD_NETWORK_SCAN = 0x03
CMD_SYSTEM_DIAG = 0x04
CMD_FULL_OS_INFO = 0x05
CMD_FULL_NETWORK_INFO = 0x06
CMD_GET_POWERSHELL_HISTORY = 0x07
CMD_GET_OS_INFO_SECTION = 0x08  # Get a specific section of OS info

# OS Info command codes
CMD_GET_OS_INFO = 0x10
CMD_GET_AMSI_PROVIDERS = 0x11
CMD_GET_REGISTERED_ANTIVIRUS = 0x12
CMD_GET_WINDOWS_DEFENDER_SETTINGS = 0x13
CMD_GET_AUTO_RUN_EXECUTABLES = 0x14
CMD_GET_CERTIFICATES = 0x15
CMD_GET_ENVIRONMENT_VARIABLES = 0x16
CMD_LIST_USER_FOLDERS = 0x17
CMD_GET_FILE_VERSION = 0x18
CMD_GET_INSTALLED_HOTFIXES = 0x19
CMD_GET_INSTALLED_PRODUCTS = 0x1A
CMD_GET_NON_EMPTY_LOCAL_GROUPS = 0x1B
CMD_GET_LOCAL_USERS = 0x1C
CMD_GET_MS_UPDATES = 0x1D
CMD_GET_NTLM_SETTINGS = 0x1E
CMD_GET_RDP_CONNECTIONS = 0x1F
CMD_GET_SECURE_BOOT_INFO = 0x20
CMD_GET_SYSMON_CONFIG = 0x21
CMD_GET_UAC_POLICIES = 0x22
CMD_GET_AUDIT_POLICY = 0x23
CMD_GET_FIREWALL_RULES = 0x24
CMD_GET_RUNNING_PROCESSES = 0x25

# Network Info command codes
CMD_ARP_SCAN = 0x30
CMD_DNS_CACHE = 0x31
CMD_WINDOWS_NETWORK_PROFILE = 0x32
CMD_NETWORK_SHARES = 0x33
CMD_TCP_UDP_CONNECTIONS = 0x34
CMD_RPC_SERVICE_CHECK = 0x35
CMD_PORT_SCANNER = 0x36
CMD_BANNER_GRABBER = 0x37
CMD_PORT_SCAN = 0x38  # Comprehensive port scan with service detection

# Memory Protection Analysis
CMD_ANALYZE_PROCESS_MEMORY = 0x40

# Vulnerability Scanning
CMD_VULNERABILITY_SCAN = 0x50