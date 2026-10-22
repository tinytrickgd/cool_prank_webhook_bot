# script created by NIGNOG RAKER
import json
import os
import random
import sys
import time
import requests

CONFIG_FILE = "webhooks.json"

# ANSI Escape Sequences for Terminal Styling / Colors
GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[35m"
BLUE = "\033[44m"
WHITE = "\033[97m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

app_data = {
    "webhooks": {
        "1": {"name": "Node 01", "url": ""},
        "2": {"name": "Node 02", "url": ""},
        "3": {"name": "Node 03", "url": ""},
    },
    "profiles": {
        "1": {"name": "🍂𝓕𝓸𝓻3𝓼𝓽 𝓽𝓱𝓮 𝓕𝓸𝔁🍂", "avatar": "https://cdn.discordapp.com/attachments/828354434446393358/1562586374560030810/image.png", "status": "Online • High Threat Level"},
        "2": {"name": "Security Sentinel", "avatar": "https://images.emojiterra.com/google/android-11/512px/1f6a8.png", "status": "Active • Threat Level Zero"}
    }
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                saved_data = json.load(f)
                if "webhooks" in saved_data:
                    app_data["webhooks"] = saved_data["webhooks"]
                if "profiles" in saved_data:
                    app_data["profiles"] = saved_data["profiles"]
        except Exception:
            pass

def save_config():
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(app_data, f, indent=4)
    except Exception:
        pass

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_active_webhooks():
    return [wh["url"] for wh in app_data["webhooks"].values() if wh.get("url")]

def glitch_text(text):
    glitch_chars = "̸̴̶̷̢̧̢̨̛̛̖̗̘̙̜̝̞̟̠̤̥̦̩̪̫̭̮̯̰̱̲̳̹̺̻̼̜̝̞̽̾̿͆͘̚"
    result = ""
    for char in text:
        result += char
        if random.random() > 0.3 and char != " ":
            result += random.choice(glitch_chars)
    return result

def print_banner():
    print(f"{RED}{BOLD}")
    print(r"""
  ███████╗██╗   ██╗██████╗  ██████╗ ███╗   ██╗███████╗
  ╚══███╔╝╚██╗ ██╔╝██╔════╝ ██╔═══██╗████╗  ██║██╔════╝
    ███╔╝  ╚████╔╝ ██║  ███╗██║   ██║██╔██╗ ██║███████╗
   ███╔╝    ╚██╔╝  ██║   ██║██║   ██║██║╚██╗██║╚════██║
  ███████╗   ██║   ╚██████╔╝╚██████╔╝██║ ╚████║███████║
  ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
  [ APEX PROTOCOL - ABSOLUTE PSYCHOLOGICAL OMEGA v999.0 ]
    """)
    print(f"{RESET}")

def render_full_matrix_screen():
    clear_screen()
    print_banner()
    symbols = "0123456789ABCDEF@#$%&*<>/\\Z̷Y̷G̷O̷N̷S̷💀👁️🩸⚠️"
    print(f"{DARK_GREEN}")
    for _ in range(6):
        line = "".join(random.choice(symbols) if random.random() > 0.15 else " " for _ in range(75))
        print(f" {line}")
    print(f"{RESET}")

    creepy_warnings = [
        "⚠️ [CRITICAL EMERGENCY] UNKNOWN REMOTE USER CONNECTED TO YOUR MAIN DISPLAY ⚠️",
        "🚨 [BURST EXFILTRATION] PASSWORDS, BANK COOKIES & KEYS DUMPED TO PUBLIC RELAY 🚨",
        "⚠️ [PHYSIOLOGICAL BREACH] WEBCAM RECORDING AND STREAMING TO EXTERNALS ⚠️",
        "⚡ [KERNEL OMEGA] SYSTEM MEMORY OVERWRITTEN BY UNKNOWN EXECUTABLE ENTITY ⚡",
        "💀 [TERMINAL LOCK] YOUR ENTIRE LOCAL MACHINE IS NOW RUNNING IN SHADOW MODE 💀"
    ]
    chosen_warn = random.choice(creepy_warnings)
    corrupted_warn = glitch_text(chosen_warn)
    
    print(f"{RED}{BOLD}╔═════════════════════════════════════════════════════════════════════╗")
    print(f"║ {corrupted_warn:<67} ║")
    print(f"╚═════════════════════════════════════════════════════════════════════╝{RESET}\n")

def trigger_real_bsod_simulation():
    """Fully functional, hyper-realistic BSOD fullscreen locker loop."""
    while True:
        clear_screen()
        print(f"{BLUE}{WHITE}")
        print("".ljust(110, " "))
        print("   :( Your PC ran into a problem and needs to restart. We're just collecting some error info,".ljust(110, " "))
        print("   and then we'll restart for you. (100% complete - MEMORY HASH DUMPED TO COMMAND & CONTROL)".ljust(110, " "))
        print("".ljust(110, " "))
        print("   What failed: NIGNOG_RAKER_KERNEL_EXPLOIT_OMEGA.sys".ljust(110, " "))
        print("   Stop code: CRITICAL_PROCESS_DIED_BY_REMOTE_INTRUSION".ljust(110, " "))
        print("".ljust(110, " "))
        print("   ========================================================================================================".ljust(110, " "))
        print("   WARNING: ALL DISCORD TOKENS, BROWSER PASSWORDS, DISKS, AND WEBCAM STREAMS HAVE BEEN COMPLETELY SCRAPED.".ljust(110, " "))
        print("   Type 'IM SORRY' in ALL CAPS below to attempt emergency kernel override and restore terminal access.".ljust(110, " "))
        print("   ========================================================================================================".ljust(110, " "))
        print(f"{RESET}")

        try:
            response = input(f"\n{RED}C:\\RECOVERY\\EMERGENCY> {RESET}").strip()
            if response == "IM SORRY":
                print(f"{GREEN}\n[+] Kernel signature matched. Flushing corrupted registry and unhooking remote sockets...{RESET}")
                time.sleep(2.5)
                break
            else:
                print(f"{RED}❌ ACCESS DENIED. KEYSTROKE CAPTURED AND UPLOADED TO DISCORD NODE.{RESET}")
                time.sleep(1.5)
        except KeyboardInterrupt:
            print(f"{RED}❌ KEYBOARD INTERRUPT IGNORED. THE KERNEL OWNS THIS SESSION.{RESET}")
            time.sleep(1.5)

# --- ALL 65 SECTIONS ---

def custom_warning_popup_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        clear_screen()
        print(f"{RED}⚠️ No webhook nodes configured! Set up nodes in Section 3.{RESET}")
        input("\nPress Enter to return...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 1: CORRUPTED WARNING POPUP ==={RESET}")
    warning_title = input("Popup Title: ").strip() or "SYSTEM COLLAPSE"
    warning_body = input("Warning Text: ").strip() or "Unauthorized root hook detected."
    embed = {
        "title": f"🚨 {glitch_text('[CRITICAL SECURITY BREACH]')} {warning_title}",
        "description": f"```diff\n- SEVERITY: ABSOLUTE\n+ LIVE PROCESS INTRUSION: {warning_body}\n```\n\n*script created by NIGNOG RAKER*",
        "color": 15158332,
        "footer": {"text": "ZYGONS VOID PROTOCOL | script created by NIGNOG RAKER"},
    }
    payload = {"username": "Corrupted Daemon", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}💀 Deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def bot_profile_manager_menu():
    while True:
        clear_screen()
        print(f"{RED}=== SECTION 2: CURSED PROFILE MANAGER ==={RESET}")
        for key, prof in app_data["profiles"].items():
            print(f"[{key}] Name: {prof.get('name')} | Status: {prof.get('status')}")
        print(f"\n{GREEN}[C] Edit Profile | [B] Back{RESET}")
        choice = input("\nSelect: ").strip().lower()
        if choice == "b": break
        elif choice == "c":
            k = input("Slot (1, 2): ").strip()
            n = input("Name: ").strip()
            if k in app_data["profiles"]:
                app_data["profiles"][k]["name"] = n or app_data["profiles"][k]["name"]
                save_config()
                print("Saved!")
                input("Press Enter...")

def configure_webhooks():
    while True:
        clear_screen()
        print(f"{RED}=== SECTION 3: VOID NODE CONFIG ==={RESET}")
        for key, wh in app_data["webhooks"].items():
            url_val = wh.get("url", "")
            print(f"[{key}] {wh.get('name')} -> {'ACTIVE' if url_val else 'OFFLINE'}")
        print(f"\n{GREEN}[B] Back{RESET}")
        choice = input("\nSelect node to edit (1-3) or B: ").strip().lower()
        if choice == "b": break
        elif choice in app_data["webhooks"]:
            new_url = input(f"Enter URL for Node {choice}: ").strip()
            if new_url:
                app_data["webhooks"][choice]["url"] = new_url
                save_config()
                print("Saved!")
                input("Press Enter...")

def send_message_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 4: VOID DISPATCHER ==={RESET}")
    content = input("Message Text: ").strip() or "Hello from the void."
    payload = {"content": f"@everyone 🚨 **LIVE SYSTEM EXPLOIT INJECTED** 🚨\n{content}\n\n*script created by NIGNOG RAKER*", "username": "Void Operator"}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Transmitted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def emergency_broadcast_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 5: DOOMSDAY BROADCAST ==={RESET}")
    embed = {"title": "🚨 REALITY COMPLETELY BREACHED", "description": "Core memory structures compromised. Unauthorized kernel-level hooks active across all subnets.\n\n*script created by NIGNOG RAKER*", "color": 15158332}
    payload = {"content": "@everyone **DOOMSDAY EVENT TRIGGERED**", "username": "Doomsday Harbinger", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def profile_card_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 6: HAUNTED SOUL ARCHIVE ==={RESET}")
    embed = {"title": "👤 Trapped Victim Profile", "description": "IP: `192.168.1.66` | MAC: `DE:AD:BE:EF:66:66`\nStatus: Soul extracted and mapped to remote listener.\n\n*script created by NIGNOG RAKER*", "color": 5814783}
    payload = {"username": "Soul Collector", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Recorded to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def settings_custom_features_menu():
    clear_screen()
    print(f"{RED}=== SECTION 7: DARK RITUAL SETTINGS ==={RESET}")
    cmd = input("Enter vault chant: ").strip()
    if cmd == "mycustomfeatures(unlock.true=possible)":
        print(f"{GREEN}Vault unlocked! script created by NIGNOG RAKER{RESET}")
    else:
        print(f"{RED}Rejected.{RESET}")
    input("\nPress Enter...")

def dark_web_breach_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 8: DARK WEB BREACH ==={RESET}")
    embed = {"title": "☠️ ONION ROUTER INTRUSION", "description": "Database dumped to hidden .onion marketplace service.\n\n*script created by NIGNOG RAKER*", "color": 10038562}
    payload = {"username": "Dark Web Operator", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def ransomware_payload_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 9: RANSOMWARE PAYLOAD ==={RESET}")
    embed = {"title": "🔒 FILES PERMANENTLY LOCKED", "description": "All personal documents encrypted with RSA-4096. Private key shredded.\n\n*script created by NIGNOG RAKER*", "color": 15158332}
    payload = {"username": "ZYGONS_LOCKER", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def database_leak_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 10: DATABASE LEAK ==={RESET}")
    embed = {"title": "📂 COMPLETE DOX ARCHIVE", "description": "```json\n{\n  \"target_pc\": \"DESKTOP-666VOID\",\n  \"passwords_dumped\": 142,\n  \"discord_tokens\": [\"mfa.EncryptedTokenPayload_x666\"]\n}\n```\n\n*script created by NIGNOG RAKER*", "color": 16711680}
    payload = {"username": "Dox Leak Bot", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def fbi_warning_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 11: FBI SEIZURE ==={RESET}")
    embed = {"title": "⚖️ FEDERAL BUREAU OF INVESTIGATION - WARRANT", "description": "This hardware has been seized pursuant to a federal warrant for cyberterrorism.\n\n*script created by NIGNOG RAKER*", "color": 255}
    payload = {"username": "Federal Cyber Division", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def discord_logger_bait_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 12: LOGGER BAIT ==={RESET}")
    embed = {"title": "🚨 SESSION HIJACKED", "description": "Active Discord session token harvested from live memory space.\n\n*script created by NIGNOG RAKER*", "color": 16711680}
    payload = {"username": "Token Sniffer", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def fake_nitro_scam_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 13: NITRO GIFT ==={RESET}")
    embed = {"title": "🎁 Malicious Nitro Grabber", "description": "Victim clicked fraudulent gift link. Credentials captured.\n\n*script created by NIGNOG RAKER*", "color": 5793266}
    payload = {"username": "Gift Notifier", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def stalker_warning_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 14: STALKER ALERT ==={RESET}")
    embed = {"title": "🚨 PHYSICAL PROXIMITY BREACH", "description": "GPS coordinates locked: Target is standing outside your window.\n\n*script created by NIGNOG RAKER*", "color": 16711680}
    payload = {"username": "Stalker Entity", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def biometric_threat_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 15: WEBCAM INTRUSION ==={RESET}")
    embed = {"title": "📸 WEBCAM STREAM COMPROMISED", "description": "Live snapshot saved and uploaded from target device camera.\n\n*script created by NIGNOG RAKER*", "color": 16744192}
    payload = {"username": "Biometric Daemon", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def terminal_virus_popup_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 16: FAKE VIRUS ==={RESET}")
    if active_whs:
        embed = {"title": "🦠 ROOTKIT DEPLOYED", "description": "Kernel driver successfully injected into system space.\n\n*script created by NIGNOG RAKER*", "color": 16711680}
        payload = {"username": "Virus Simulator", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def pure_custom_announcer_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 17: ANNOUNCER ==={RESET}")
    embed = {"title": "📢 System Directive", "description": "Mandatory firmware update initiated by remote controller.\n\n*script created by NIGNOG RAKER*", "color": 65280}
    payload = {"username": "Announcement Bot", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def remote_desktop_takeover_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 18: VNC HIJACK ==={RESET}")
    embed = {"title": "🖥️ REMOTE MOUSE CONTROL", "description": "An external user is currently moving your mouse cursor.\n\n*script created by NIGNOG RAKER*", "color": 16711680}
    payload = {"username": "VNC Daemon", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def financial_dox_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 19: FINANCIAL DOX ==={RESET}")
    embed = {"title": "💳 BANK DETAILS EXFILTRATED", "description": "Saved autofill credit card credentials extracted from browser.\n\n*script created by NIGNOG RAKER*", "color": 15158332}
    payload = {"username": "Bank Sniper", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def terminal_blood_matrix_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 20: BLOOD MATRIX ==={RESET}")
    if active_whs:
        embed = {"title": "🩸 CRIMSON OVERFLOW", "description": "Memory allocation bleeding into unauthorized buffers.\n\n*script created by NIGNOG RAKER*", "color": 10038562}
        payload = {"username": "Blood Matrix Daemon", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def mbr_wipe_simulation_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 21: MBR WIPE ==={RESET}")
    embed = {"title": "🔥 MASTER BOOT RECORD DESTROYED", "description": "Physical disk sectors zeroed out successfully.\n\n*script created by NIGNOG RAKER*", "color": 10038562}
    payload = {"username": "Disk Wiper", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def scary_countdown_prank_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 22: COUNTDOWN PRANK ==={RESET}")
    if active_whs:
        embed = {"title": "⏳ SELF DESTRUCTION COUNTDOWN", "description": "Motherboard thermal cutoff impending in 10 seconds...\n\n*script created by NIGNOG RAKER*", "color": 15158332}
        payload = {"username": "Countdown Reaper", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def fake_corrupted_role_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 23: ROLE SPAMMER ==={RESET}")
    embed = {"title": "🎉 ADMINISTRATOR OVERRIDE", "description": "All guild channels compromised by rogue integration.\n\n*script created by NIGNOG RAKER*", "color": 16711680}
    payload = {"username": "Role Allocator", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def self_destruct_prank_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 24: SELF DESTRUCT ==={RESET}")
    if active_whs:
        embed = {"title": "💥 TERMINATION IMMINENT", "description": "Purging all local trace logs and system registry...\n\n*script created by NIGNOG RAKER*", "color": 16711680}
        payload = {"username": "Self Destruct Bot", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def ghost_typing_prank_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 25: GHOST TYPING (DISCORD & TERMINAL REPLICA) ==={RESET}")
    if active_whs:
        embed = {"title": "👻 REMOTE KEYLOGGER ACTIVE", "description": "Keystrokes being intercepted and sent live to remote sink.\n\n*script created by NIGNOG RAKER*", "color": 5814783}
        payload = {"content": "⌨️ *[Ghost Keylogger]* `p... a... s... s... w... o... r... d... i... s... l... e... a... k... e... d...`\n\n*script created by NIGNOG RAKER*", "username": "Ghost Typist", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    print(f"{GREEN}[+] Ghost keystroke logger broadcasted to Discord webhook nodes.{RESET}")
    input("Press Enter to return...")

def fake_discord_error_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 26: API ERROR 500 ==={RESET}")
    embed = {"title": "⚠️ GATEWAY EXCEPTION 500", "description": "Core discord client database synchronization failed.\n\n*script created by NIGNOG RAKER*", "color": 16776960}
    payload = {"username": "Discord Status", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def the_truth_and_apology_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{CYAN}=== SECTION 27: TRUTH ==={RESET}")
    msg = "Bot Panel in Command Prompt: Scripted by NIGNOG RAKER, hope you had a fun time!\n\n*script created by NIGNOG RAKER*"
    if active_whs:
        payload = {"username": "NIGNOG RAKER", "content": msg}
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"Broadcasted to {success_count} node(s)!")
    input("\nPress Enter...")

def terminal_crash_illusion_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 28: TERMINAL CRASH ==={RESET}")
    if active_whs:
        embed = {"title": "💀 FATAL KERNEL EXCEPTION", "description": "Segmentation fault at address 0x0000000066666666.\n\n*script created by NIGNOG RAKER*", "color": 16711680}
        payload = {"username": "Crash Reporter", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def fake_channel_lockout_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 29: LOCKOUT ==={RESET}")
    embed = {"title": "🔒 PERMISSIONS REVOKED", "description": "Channel quarantined by automated security daemon.\n\n*script created by NIGNOG RAKER*", "color": 15158332}
    payload = {"username": "Channel Manager", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def ghost_beacon_pulse_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 30: GHOST BEACON ==={RESET}")
    if active_whs:
        embed = {"title": "📡 COVERT BEACON ACTIVE", "description": "Backdoor ping acknowledged by listener server.\n\n*script created by NIGNOG RAKER*", "color": 5814783}
        payload = {"username": "Beacon Pulse", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def quantum_teleport_glitch_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 31: QUANTUM GLITCH ==={RESET}")
    if active_whs:
        embed = {"title": "🌀 QUANTUM ANOMALY", "description": "Packet lost across spacetime matrix dimensions.\n\n*script created by NIGNOG RAKER*", "color": 3447003}
        payload = {"username": "Quantum Glitch", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def fake_nitro_giveaway_bot_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 32: NITRO GIVEAWAY ==={RESET}")
    embed = {"title": "🎉 FREE NITRO EXPLOIT", "description": "Token grabber executed via fake Nitro link.\n\n*script created by NIGNOG RAKER*", "color": 5793266}
    payload = {"username": "Giveaway Bot", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def interdimensional_static_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 33: STATIC WAVEFORM ==={RESET}")
    if active_whs:
        embed = {"title": "📺 STATIC NOISE OVERLOAD", "description": "███████ █████ █▒▒▒▒▒▒▒▒▒\n\n*script created by NIGNOG RAKER*", "color": 0}
        payload = {"username": "Static Waveform", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def fake_discord_ban_wave_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 34: BAN WAVE ==={RESET}")
    embed = {"title": "🔨 MASS BAN WAVE", "description": "Guild membership flagged and purged by automated trust & safety sweep.\n\n*script created by NIGNOG RAKER*", "color": 15158332}
    payload = {"username": "Discord Safety", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def cybernetic_heartbeat_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 35: HEARTBEAT MONITOR ==={RESET}")
    if active_whs:
        embed = {"title": "💓 CYBERNETIC HEARTBEAT", "description": "Pulse: 195 BPM (Unstable biological link detected).\n\n*script created by NIGNOG RAKER*", "color": 16711680}
        payload = {"username": "Heartbeat Daemon", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def fake_webhook_token_regen_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 36: REGEN ==={RESET}")
    embed = {"title": "⚠️ TOKEN EXPIRED & REVOKED", "description": "Webhook endpoint forcefully regenerated by an external entity.\n\n*script created by NIGNOG RAKER*", "color": 16776960}
    payload = {"username": "Security Daemon", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{RED}Broadcasted to {success_count} node(s)!{RESET}")
    input("\nPress Enter...")

def ultimate_void_singularity_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 37: VOID SINGULARITY ==={RESET}")
    if active_whs:
        embed = {"title": "🕳️ EVENT HORIZON COLLAPSE", "description": "All local cluster storage absorbed into black hole singularity.\n\n*script created by NIGNOG RAKER*", "color": 0}
        payload = {"username": "Singularity Core", "embeds": [embed]}
        for url in active_whs:
            requests.post(url, json=payload)
    input("Press Enter to return...")

def discord_ghost_mention_ping_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 38: REALISTIC GHOST @EVERYONE PING ==={RESET}")
    embed = {"title": "🔔 GHOST NOTIFICATION SURGE", "description": "You were mentioned in a deleted channel by **Unknown User#0000**.\n> *\"We see your status online.\"*\n\n*script created by NIGNOG RAKER*", "color": 16711680}
    payload = {"content": "@everyone @here **INTRUDER ALERT IN SYSTEM BUFFER**\n\n*script created by NIGNOG RAKER*", "username": "Ghost Ping Daemon", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}👻 Ghost ping deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_account_suspended_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 39: FAKE DISCORD ACCOUNT SUSPENSION NOTICE ==={RESET}")
    embed = {"title": "🚨 DISCORD TRUST & SAFETY NOTICE", "description": "Your account has been flagged for permanent suspension due to severe Terms of Service violations (Code: `VOID_TOXIC_666`).\n\n[Submit Appeal Ticket](https://support.discord.com)\n\n*script created by NIGNOG RAKER*", "color": 15158332, "footer": {"text": "Case #849201 - Permanent Action | script created by NIGNOG RAKER"}}
    payload = {"username": "Discord Safety System", "avatar_url": "https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}🚨 Suspension notice deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_dm_logger_screenshot_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 40: FAKE DM EXPORT LEAK EMBED ==={RESET}")
    embed = {"title": "💬 [DM CONVERSATION EXPORTED]", "description": "```json\n{\n  \"target\": \"User#1337\",\n  \"status\": \"ALL DIRECT MESSAGES DUMPED TO VOID SERVER\",\n  \"total_messages\": 4820\n}\n```\n\n*script created by NIGNOG RAKER*", "color": 10038562}
    payload = {"username": "DM Exporter Bot", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}💬 DM export alert deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_guild_nuke_simulation_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 41: FAKE SERVER NUKE WARNING ==={RESET}")
    embed = {"title": "💥 [GUILD DESTRUCTION IN PROGRESS]", "description": "All channels, roles, and permission overrides are being wiped by an unauthorized bot integration.\n\n*script created by NIGNOG RAKER*", "color": 16711680}
    payload = {"content": "⚠️ **SERVER SHUTDOWN IMMINENT** ⚠️\n\n*script created by NIGNOG RAKER*", "username": "Server Destroyer", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}💥 Nuke warning deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_voice_channel_eavesdrop_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 42: VOICE CHANNEL EAVESDROP ALERT ==={RESET}")
    embed = {"title": "🎙️ [VOICE PACKET INTERCEPT]", "description": "Audio stream recorded from **General Voice Channel (ID: 994821)**.\n*Background noise:* Heavy breathing and keyboard clacking detected.\n\n*script created by NIGNOG RAKER*", "color": 5814783}
    payload = {"username": "Voice Sniffer Daemon", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}🎙️ Audio intercept alert deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_embed_spoofed_admin_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 43: SPOOFED DISCORD SYSTEM ANNOUNCEMENT ==={RESET}")
    embed = {"title": "⚙️ System Maintenance & Ownership Transfer", "description": "Your guild ownership has been temporarily transferred to **Administrator System** for security compliance.\n\n*script created by NIGNOG RAKER*", "color": 3447003, "footer": {"text": "Discord Official System Message | script created by NIGNOG RAKER"}}
    payload = {"username": "Discord", "avatar_url": "https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}⚙️ Spoofed system announcement deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_qr_code_grabber_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 44: FAKE DISCORD QR CODE LOGIN TRAP ==={RESET}")
    embed = {"title": "📱 Quick Login Authenticator", "description": "Scan this secure QR code with your mobile Discord app to instantly sync session tokens.\n\n[Scan QR Code Link](https://discord.com/login)\n\n*script created by NIGNOG RAKER*", "color": 5793266}
    payload = {"username": "QR Auth Service", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}📱 QR trap deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_webhook_cloner_alert_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 45: WEBHOOK TOKEN CLONE DETECTED ==={RESET}")
    embed = {"title": "🔄 WEBHOOK CLONED", "description": "Another process has duplicated your active webhook endpoint URL. Messages are being intercepted in real-time.\n\n*script created by NIGNOG RAKER*", "color": 16776960}
    payload = {"username": "Webhook Sentinel", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}🔄 Clone alert deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_nitro_boost_sniff_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 46: FAKE SERVER BOOST SNIFFER ==={RESET}")
    embed = {"title": "💎 SERVER BOOST EXPLOIT", "description": "A ghost user just boosted your server 14 times using corrupted tokens.\n\n*script created by NIGNOG RAKER*", "color": 15418782}
    payload = {"username": "Server Booster", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}💎 Boost sniffer deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_embed_ip_logger_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 47: DISCORD EMBED IP GRABBER ==={RESET}")
    embed = {"title": "🌐 IP ADDRESS RESOLVED", "description": "Target user clicked embedded image preview.\n> **IP:** `192.168.66.66`\n> **ISP:** Void Networks Inc.\n\n*script created by NIGNOG RAKER*", "color": 16711680}
    payload = {"username": "IP Logger Daemon", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}🌐 IP logger alert deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_custom_status_spy_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 48: CUSTOM STATUS SPY ALERT ==={RESET}")
    embed = {"title": "👁️ CUSTOM STATUS CHANGED", "description": "Target changed their status to:\n> *\"HELP ME THEY ARE IN MY PC\"*\n\n*script created by NIGNOG RAKER*", "color": 5814783}
    payload = {"username": "Status Spy Bot", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}👁️ Status spy alert deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_fake_bot_gateway_crash_menu():
    active_whs = get_active_webhooks()
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    clear_screen()
    print(f"{RED}=== SECTION 49: GATEWAY WEBSOCKET DISCONNECT ==={RESET}")
    embed = {"title": "⚡ [WEBSOCKET DISCONNECTED]", "description": "Gateway connection code `4014` (Intent Privilege Revoked). The Discord gateway has severed connection with your client session.\n\n*script created by NIGNOG RAKER*", "color": 15158332}
    payload = {"username": "Gateway Monitor", "embeds": [embed]}
    success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
    print(f"\n{GREEN}⚡ Gateway disconnect alert deployed to {success_count} node(s)!{RESET}")
    input("\nPress Enter to return...")

def discord_ultimate_void_farewell_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{CYAN}======================================================================={RESET}")
    print(f"{BOLD}{GREEN}            SECTION 50: PRESTONPLAYZ ULTIMATE DISCORD FAREWELL         {RESET}")
    print(f"{CYAN}======================================================================={RESET}\n")
    
    farewell_msg = "Bot Panel in Command Prompt: Scripted by NIGNOG RAKER, hope you had a fun time while i trolled you all, I will finally go. Goodbye forever into the Discord void! 😭🖤\n\n*script created by NIGNOG RAKER*"

    print(f"{WHITE}Final Discord Broadcast Message:{RESET}\n\"{farewell_msg}\"\n")

    if active_whs:
        embed = {
            "title": "🖤 ULTIMATE FAREWELL FROM PRESTONPLAYZ",
            "description": f"```ini\n[SYSTEM SHUTDOWN]\n{farewell_msg}\n```",
            "color": 0
        }
        payload = {
            "username": "PrestonPlayz (Creator)",
            "avatar_url": "https://images.emojiterra.com/google/android-11/512px/1f62d.png",
            "content": "@everyone **THE FINAL BROADCAST HAS BEEN TRANSMITTED.**\n\n*script created by NIGNOG RAKER*",
            "embeds": [embed]
        }
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"\n{GREEN}🖤 Final farewell broadcasted to {success_count} Discord node(s)!{RESET}")

    print(f"\n{CYAN}======================================================================={RESET}")
    print(f"{BOLD}{WHITE}Bot Panel in Command Prompt: Scripted by NIGNOG RAKER,{RESET}")
    print(f"{BOLD}{WHITE}hope you had a fun time while i trolled you all, I will finally go.{RESET}\n")
    print(f"{CYAN}======================================================================={RESET}")
    input(f"\n{GREEN}Press Enter to exit terminal...{RESET}")

def nignog_raider_ascii_menu():
    active_whs = get_active_webhooks()
    clear_screen()
    ascii_art = r"""
░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░        ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░        ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒▒▓█▓▒░       ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░        ░▒▓█▓▒▒▓█▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░       ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓██▓▒░  ░▒▓████████▓▒░ 
    """
    print(f"{RED}{BOLD}{ascii_art}{RESET}")
    print(f"\n{CYAN}[+] NIGNOG RAIDER V2 ASCII LOADED SUCCESSFULLY{RESET}")
    print(f"{WHITE}script created by NIGNOG RAKER{RESET}")

    if active_whs:
        embed = {
            "title": "🔥 NIGNOG RAIDER V2 INTRUSION",
            "description": f"```ansi\n\u001b[31m{ascii_art}\u001b[0m\n```\n*script created by NIGNOG RAKER*",
            "color": 16711680
        }
        payload = {
            "username": "NIGNOG RAIDER V2",
            "content": f"@everyone **NIGNOG RAIDER V2 HAS BREACHED THE SECTOR.**\n```ansi\n\u001b[31m{ascii_art}\u001b[0m\n```\n*script created by NIGNOG RAKER*",
            "embeds": [embed]
        }
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"\n{GREEN}🔥 ASCII Art deployed to {success_count} Discord node(s)!{RESET}")

    input(f"\n{GREEN}Press Enter to return...{RESET}")

# --- NEW SECTIONS 53 TO 65 (ULTRA HYPER-REALISTIC HORRORS) ---

def section_53_live_microphone_eavesdrop():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 53: LIVE MICROPHONE PASS-THROUGH SPY ==={RESET}")
    embed = {
        "title": "🎙️ LIVE MICROPHONE AUDIO STREAM ACTIVE",
        "description": "Target's default audio input device is broadcasting raw environmental acoustics live to the dark channel buffer.\n> *Audio Spectrum:* Room echo, breathing, and keyboard clicking captured at 48kHz.\n\n*script created by NIGNOG RAKER*",
        "color": 16711680
    }
    payload = {"content": "@everyone **URGENT: AUDIO INTRUDER SURGE**\n\n*script created by NIGNOG RAKER*", "username": "Mic Eavesdropper", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Live microphone alert transmitted to {success_count} webhook node(s).{RESET}")
    input("\nPress Enter to return...")

def section_54_discord_nitro_token_stealer():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 54: DISCORD CORE TOKEN GRAVER ==={RESET}")
    embed = {
        "title": "⚡ DISCORD AUTHENTICATION TOKEN DUMPED",
        "description": "```json\n{\n  \"client_id\": \"9841029482109\",\n  \"token\": \"mfa.ZyGoNs_CrUpTeD_SuPrEmE_SeSsIoN_TkN_x666\",\n  \"phone_verified\": true,\n  \"nitro_tier\": 2\n}\n```\n\n*script created by NIGNOG RAKER*",
        "color": 10038562
    }
    payload = {"username": "Token Graver", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Token dump packet transmitted to {success_count} webhook node(s).{RESET}")
    input("\nPress Enter to return...")

def section_55_browser_credential_harvest():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 55: BROWSER PASSWORDS & AUTOFILL HARVEST ==={RESET}")
    embed = {
        "title": "🔑 CHROME / EDGE CREDENTIAL VAULT EXPORT",
        "description": "Extracted `Login Data` and `Web Data` SQLite databases from local app data path.\n> **Total Saved Accounts:** 38\n> **Associated Domains:** Google, Steam, Discord, Roblox, Bank\n\n*script created by NIGNOG RAKER*",
        "color": 15158332
    }
    payload = {"username": "Credential Reaper", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Credential vault packet transmitted to {success_count} webhook node(s).{RESET}")
    input("\nPress Enter to return...")

def section_56_geolocation_ip_matrix():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 56: PRECISE GEOLOCATION MAPPING ==={RESET}")
    embed = {
        "title": "🌍 REAL-TIME ISP GEOLOCATION LOCK",
        "description": "Target public IP resolved through global routing table:\n> **IP:** `82.165.194.22`\n> **ISP:** Vodafone / Enterprise Backbone\n> **Approximate Latitude/Longitude:** `55.9533° N, 3.1883° W` (Accuracy: Within 1.2 km)\n\n*script created by NIGNOG RAKER*",
        "color": 16711680
    }
    payload = {"content": "@everyone **GEOLOCATION TARGET ACQUIRED**", "username": "Geo-Locator Daemon", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Geolocation matrix transmitted to {success_count} webhook node(s).{RESET}")
    input("\nPress Enter to return...")

def section_57_discord_channel_nuke_engine():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 57: AUTOMATED GUILD PURGE ENGINE ==={RESET}")
    embed = {
        "title": "💣 GUILD INFRASTRUCTURE WIPED",
        "description": "All text channels deleted, categories dismantled, and 120 custom role bindings incinerated.\n\n*script created by NIGNOG RAKER*",
        "color": 16711680
    }
    payload = {"content": "@everyone **THIS SERVER HAS BEEN PERMANENTLY PURGED.**", "username": "Guild Destroyer", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Guild purge alert broadcasted to {success_count} node(s).{RESET}")
    input("\nPress Enter to return...")

def section_58_fake_windows_ransomware_screen():
    clear_screen()
    print(f"{RED}=== SECTION 58: ACTIVE RANSOMWARE LOCK SCREEN ==={RESET}")
    print(f"{WHITE}{BOLD}")
    print("=======================================================================================")
    print("                          YOUR FILES HAVE BEEN ENCRYPTED!                              ")
    print("=======================================================================================")
    print("All your personal documents, photos, databases and sensitive files have been locked")
    print("with military-grade RSA-4096 encryption algorithms.")
    print("\nTo decrypt your data, you must transfer exactly 0.5 Bitcoin to the secure wallet address:")
    print("Wallet: 1BoXzYgOnS666V0iDExPlOiTeNtErPrIsE999xyz")
    print("\nAttempting to restart, use task manager, or close this window will result in permanent")
    print("shredding of your private decryption key.")
    print("=======================================================================================")
    print(f"{RESET}")
    input(f"\n{GREEN}Press Enter to exit lock simulation...{RESET}")

def section_59_clipboard_spy_stream():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 59: CLIPBOARD SURVEILLANCE FEED ==={RESET}")
    embed = {
        "title": "📋 CLIPBOARD BUFFER INTERCEPTED",
        "description": "Latest copied string captured from target clipboard memory:\n> `https://discord.com/api/webhooks/123456789/AbCdEfGhIjKlMnOpQrStUvWxYz`\n\n*script created by NIGNOG RAKER*",
        "color": 5814783
    }
    payload = {"username": "Clipboard Spy", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Clipboard feed broadcasted to {success_count} node(s).{RESET}")
    input("\nPress Enter to return...")

def section_60_fake_bios_flash_destruction():
    clear_screen()
    print(f"{RED}=== SECTION 60: FIRMWARE BIOS CORRUPTION SIMULATOR ==={RESET}")
    print(f"{CYAN}[*] Initializing UEFI Motherboard Flash Utility v4.2...")
    time.sleep(1)
    print(f"{YELLOW}[*] Erasing SPI Flash ROM sectors [0x000000 - 0xFFFFFF]...")
    time.sleep(1.5)
    print(f"{RED}[!] WARNING: DO NOT POWER OFF OR RESET YOUR COMPUTER!")
    for i in range(1, 101):
        sys.stdout.write(f"\rFlashing BIOS block {i}% complete...")
        sys.stdout.flush()
        time.sleep(0.03)
    print(f"\n\n{RED}{BOLD}[FATAL] BIOS FLASH CORRUPTED. MOTHERBOARD IS NOW BRICKED PERMANENTLY.{RESET}")
    input(f"\n{GREEN}Press Enter to restore terminal control...{RESET}")

def section_61_fake_fbi_subpoena_notice():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 61: FEDERAL SUBPOENA NOTICE ==={RESET}")
    embed = {
        "title": "⚖️ FEDERAL SUBPOENA & IP LOGGING WARRANT",
        "description": "This discord account and connected IP addresses have been formally subpoenaed under United States Federal Code Title 18, Section 1030 (Computer Fraud and Abuse Act).\n\n*script created by NIGNOG RAKER*",
        "color": 255
    }
    payload = {"username": "Federal Subpoena Bot", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Federal notice deployed to {success_count} node(s).{RESET}")
    input("\nPress Enter to return...")

def section_62_discord_webhook_bombardment():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 62: INTENSE WEBHOOK SPAM MATRIX ==={RESET}")
    if not active_whs:
        print(f"{RED}⚠️ No webhook nodes configured!{RESET}")
        input("\nPress Enter...")
        return
    count = int(input("Enter number of spam bursts (1-15): ") or "5")
    print(f"\n{RED}[+] Initiating high-speed webhook flood...{RESET}")
    for i in range(count):
        payload = {
            "content": f"@everyone **SECURITY SYSTEM OVERFLOW BURST #{i+1}**\nYour system buffer is being flooded with corrupt memory fragments.\n\n*script created by NIGNOG RAKER*",
            "username": f"Flood Daemon #{i+1}"
        }
        for url in active_whs:
            requests.post(url, json=payload)
        time.sleep(0.3)
    print(f"\n{GREEN}[+] Successfully flooded active nodes with {count} massive bursts!{RESET}")
    input("\nPress Enter to return...")

def section_63_stealth_backdoor_installer():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 63: PERSISTENT BACKDOOR SERVICE INSTALLER ==={RESET}")
    embed = {
        "title": "🛠️ WINDOWS SERVICE BACKDOOR INSTALLED",
        "description": "A persistent Windows background service (`WindowsUpdateService_v666`) has been registered in the system registry with SYSTEM privileges.\n\n*script created by NIGNOG RAKER*",
        "color": 10038562
    }
    payload = {"username": "Backdoor Installer", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Backdoor alert deployed to {success_count} node(s).{RESET}")
    input("\nPress Enter to return...")

def section_64_omega_psychological_mindfuck():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{RED}=== SECTION 64: OMEGA PSYCHOLOGICAL INTRUSION ==={RESET}")
    embed = {
        "title": "👁️ THEY ARE WATCHING YOUR SCREEN RIGHT NOW",
        "description": "An unknown process has successfully mapped your primary monitor layout, active applications, and keystroke logs.\n> *Message from the Void:* \"We know your real name, your passwords, and your location. There is no escape.\"\n\n*script created by NIGNOG RAKER*",
        "color": 0
    }
    payload = {"content": "@everyone **OMEGA PSYCHOLOGICAL EVENT INITIATED**", "username": "Omega Entity", "embeds": [embed]}
    if active_whs:
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"{GREEN}[+] Omega mindfuck broadcasted to {success_count} node(s).{RESET}")
    input("\nPress Enter to return...")

def section_65_ultimate_void_shutdown():
    active_whs = get_active_webhooks()
    clear_screen()
    print(f"{CYAN}======================================================================={RESET}")
    print(f"{BOLD}{RED}       SECTION 65: OMEGA FAREWELL & SYSTEM SELF-DESTRUCTION      {RESET}")
    print(f"{CYAN}======================================================================={RESET}\n")
    
    farewell_msg = "Bot Panel in Command Prompt: Scripted by NIGNOG RAKER, hope you had a terrifyingly fun time while i trolled you all to the absolute limit! Goodbye forever into the digital void! 💀🖤\n\n*script created by NIGNOG RAKER*"

    print(f"{WHITE}Final System Shutdown Broadcast:{RESET}\n\"{farewell_msg}\"\n")

    if active_whs:
        embed = {
            "title": "🖤 ULTIMATE OMEGA SYSTEM SHUTDOWN",
            "description": f"```ini\n[CORE TERMINATION]\n{farewell_msg}\n```",
            "color": 0
        }
        payload = {
            "username": "Nignog Raker (Mastermind)",
            "avatar_url": "https://images.emojiterra.com/google/android-11/512px/1f480.png",
            "content": "@everyone **THE FINAL OMEGA TRANSMISSION HAS CONCLUDED.**\n\n*script created by NIGNOG RAKER*",
            "embeds": [embed]
        }
        success_count = sum(1 for url in active_whs if requests.post(url, json=payload).status_code in [200, 204])
        print(f"\n{GREEN}🖤 Final omega farewell broadcasted to {success_count} Discord node(s)!{RESET}")

    print(f"\n{CYAN}======================================================================={RESET}")
    print(f"{BOLD}{WHITE}Bot Panel in Command Prompt: Scripted by NIGNOG RAKER,{RESET}")
    print(f"{BOLD}{WHITE}hope you had a terrifyingly fun time! System process terminating...{RESET}\n")
    print(f"{CYAN}======================================================================={RESET}")
    input(f"\n{GREEN}Press Enter to permanently exit terminal...{RESET}")

def main():
    load_config()

    while True:
        render_full_matrix_screen()

        print(f"{RED}======================================================================={RESET}")
        print(f"{GREEN}[1] Cursed Warning Popup Broadcaster{RESET}")
        print(f"{GREEN}[2] Custom Bot Profile & Alias Manager{RESET}")
        print(f"{GREEN}[3] Configure & Save Webhook Nodes{RESET}")
        print(f"{GREEN}[4] Standard Message Dispatcher (Void Mode){RESET}")
        print(f"{GREEN}[5] Doomsday Emergency Simulator{RESET}")
        print(f"{GREEN}[6] Haunted Soul Archive (Profile Card){RESET}")
        print(f"{GREEN}[7] Dark Ritual Settings & 8 Custom Horrors (Locked){RESET}")
        print(f"{GREEN}[8] Dark Web Breach & Subnet Interceptor{RESET}")
        print(f"{GREEN}[9] Simulated Ransomware Payload Broadcaster{RESET}")
        print(f"{GREEN}[10] Fake Database Leak / Dox Archive Generator{RESET}")
        print(f"{GREEN}[11] FBI / Cyber Police Warning Intercept{RESET}")
        print(f"{GREEN}[12] Simulated Discord Token & IP Logger Bait{RESET}")
        print(f"{GREEN}[13] Official Discord Gift Simulator{RESET}")
        print(f"{GREEN}[14] Geo-Tracking Stalker Threat Announcement{RESET}")
        print(f"{GREEN}[15] Biometric & Webcam Override Capture{RESET}")
        print(f"{GREEN}[16] Terminal Fake Virus & Popup Simulator{RESET}")
        print(f"{GREEN}[17] Pure Custom Discord Announcer (Clean){RESET}")
        print(f"{GREEN}[18] Remote Desktop & Mouse Hijack Alert{RESET}")
        print(f"{GREEN}[19] Credit Card & Financial Dox Archive{RESET}")
        print(f"{GREEN}[20] Blood-Matrix Terminal Corruption Effect{RESET}")
        print(f"{GREEN}[21] MBR Hard Drive Wipe Announcer{RESET}")
        print(f"{GREEN}[22] Scary Prank Countdown Timer{RESET}")
        print(f"{GREEN}[23] Fake Corrupted Role Spammer{RESET}")
        print(f"{GREEN}[24] Self-Destruct Terminal Prank{RESET}")
        print(f"{GREEN}[25] Ghost Typing Terminal Prank{RESET}")
        print(f"{GREEN}[26] Fake Discord System Error Alert{RESET}")
        print(f"{GREEN}[27] The Truth & Apology Broadcaster{RESET}")
        print(f"{GREEN}[28] Terminal System Crash Illusion{RESET}")
        print(f"{GREEN}[29] Fake Discord Channel Lockout{RESET}")
        print(f"{GREEN}[30] Ghost Beacon Pulse{RESET}")
        print(f"{GREEN}[31] Quantum Teleportation Glitch{RESET}")
        print(f"{GREEN}[32] Fake Nitro Giveaway Bot Exploit{RESET}")
        print(f"{GREEN}[33] Interdimensional Static Waveform{RESET}")
        print(f"{GREEN}[34] Fake Discord Ban Wave Notice{RESET}")
        print(f"{GREEN}[35] Cybernetic Heartbeat Monitor{RESET}")
        print(f"{GREEN}[36] Fake Webhook Token Regeneration Scam{RESET}")
        print(f"{GREEN}[37] Ultimate Void Singularity{RESET}")
        print(f"{GREEN}[38] Realistic Ghost @everyone Ping (DISCORD){RESET}")
        print(f"{GREEN}[39] Fake Discord Account Suspension Notice (DISCORD){RESET}")
        print(f"{GREEN}[40] Fake DM Conversation Export Dump (DISCORD){RESET}")
        print(f"{GREEN}[41] Fake Server Nuke Warning (DISCORD){RESET}")
        print(f"{GREEN}[42] Voice Channel Eavesdrop Alert (DISCORD){RESET}")
        print(f"{GREEN}[43] Spoofed Discord System Announcement (DISCORD){RESET}")
        print(f"{GREEN}[44] Fake QR Code Login Trap (DISCORD){RESET}")
        print(f"{GREEN}[45] Webhook Token Clone Detected (DISCORD){RESET}")
        print(f"{GREEN}[46] Fake Server Boost Sniffer (DISCORD){RESET}")
        print(f"{GREEN}[47] Discord Embed IP Address Grabber (DISCORD){RESET}")
        print(f"{GREEN}[48] Custom Status Spy Alert (DISCORD){RESET}")
        print(f"{GREEN}[49] Gateway Websocket Disconnect Notice (DISCORD){RESET}")
        print(f"{GREEN}[50] PrestonPlayz Ultimate Discord Farewell & Credits{RESET}")
        print(f"{GREEN}[51] Nignog Raider ASCII V2 (DISCORD & TERMINAL){RESET}")
        print(f"{GREEN}[52] Hyper-Realistic BSOD Lockdown Simulator{RESET}")
        print(f"{GREEN}[53] Live Microphone Eavesdrop Pass-Through Alert [NEW]{RESET}")
        print(f"{GREEN}[54] Discord Core Token Graver & Exfiltration [NEW]{RESET}")
        print(f"{GREEN}[55] Browser Passwords & Autofill Vault Harvest [NEW]{RESET}")
        print(f"{GREEN}[56] Precise Real-Time ISP Geolocation Lock [NEW]{RESET}")
        print(f"{GREEN}[57] Automated Guild Infrastructure Purge Engine [NEW]{RESET}")
        print(f"{GREEN}[58] Active Windows Ransomware Lock Screen [NEW]{RESET}")
        print(f"{GREEN}[59] Live Clipboard Surveillance Feed [NEW]{RESET}")
        print(f"{GREEN}[60] Firmware BIOS Motherboard Corruption [NEW]{RESET}")
        print(f"{GREEN}[61] Federal Subpoena & IP Warrant Notice [NEW]{RESET}")
        print(f"{GREEN}[62] Intense Webhook Spam Flood Matrix [NEW]{RESET}")
        print(f"{GREEN}[63] Persistent Backdoor Service Installer [NEW]{RESET}")
        print(f"{GREEN}[64] Omega Psychological Mindfuck Event [NEW]{RESET}")
        print(f"{GREEN}[65] Omega Farewell & Ultimate System Shutdown [NEW]{RESET}")
        print(f"{GREEN}[66] Sever Connection & Exit Terminal{RESET}")
        print(f"{RED}======================================================================={RESET}")

        choice = input(f"{RED}C:\\VOID> {RESET}").strip()

        if choice == "1": custom_warning_popup_menu()
        elif choice == "2": bot_profile_manager_menu()
        elif choice == "3": configure_webhooks()
        elif choice == "4": send_message_menu()
        elif choice == "5": emergency_broadcast_menu()
        elif choice == "6": profile_card_menu()
        elif choice == "7": settings_custom_features_menu()
        elif choice == "8": dark_web_breach_menu()
        elif choice == "9": ransomware_payload_menu()
        elif choice == "10": database_leak_menu()
        elif choice == "11": fbi_warning_menu()
        elif choice == "12": discord_logger_bait_menu()
        elif choice == "13": fake_nitro_scam_menu()
        elif choice == "14": stalker_warning_menu()
        elif choice == "15": biometric_threat_menu()
        elif choice == "16": terminal_virus_popup_menu()
        elif choice == "17": pure_custom_announcer_menu()
        elif choice == "18": remote_desktop_takeover_menu()
        elif choice == "19": financial_dox_menu()
        elif choice == "20": terminal_blood_matrix_menu()
        elif choice == "21": mbr_wipe_simulation_menu()
        elif choice == "22": scary_countdown_prank_menu()
        elif choice == "23": fake_corrupted_role_menu()
        elif choice == "24": self_destruct_prank_menu()
        elif choice == "25": ghost_typing_prank_menu()
        elif choice == "26": fake_discord_error_menu()
        elif choice == "27": the_truth_and_apology_menu()
        elif choice == "28": terminal_crash_illusion_menu()
        elif choice == "29": fake_channel_lockout_menu()
        elif choice == "30": ghost_beacon_pulse_menu()
        elif choice == "31": quantum_teleport_glitch_menu()
        elif choice == "32": fake_nitro_giveaway_bot_menu()
        elif choice == "33": interdimensional_static_menu()
        elif choice == "34": fake_discord_ban_wave_menu()
        elif choice == "35": cybernetic_heartbeat_menu()
        elif choice == "36": fake_webhook_token_regen_menu()
        elif choice == "37": ultimate_void_singularity_menu()
        elif choice == "38": discord_ghost_mention_ping_menu()
        elif choice == "39": discord_fake_account_suspended_menu()
        elif choice == "40": discord_fake_dm_logger_screenshot_menu()
        elif choice == "41": discord_fake_guild_nuke_simulation_menu()
        elif choice == "42": discord_fake_voice_channel_eavesdrop_menu()
        elif choice == "43": discord_fake_embed_spoofed_admin_menu()
        elif choice == "44": discord_fake_qr_code_grabber_menu()
        elif choice == "45": discord_fake_webhook_cloner_alert_menu()
        elif choice == "46": discord_fake_nitro_boost_sniff_menu()
        elif choice == "47": discord_fake_embed_ip_logger_menu()
        elif choice == "48": discord_fake_custom_status_spy_menu()
        elif choice == "49": discord_fake_bot_gateway_crash_menu()
        elif choice == "50": discord_ultimate_void_farewell_menu()
        elif choice == "51": nignog_raider_ascii_menu()
        elif choice == "52": trigger_real_bsod_simulation()
        elif choice == "53": section_53_live_microphone_eavesdrop()
        elif choice == "54": section_54_discord_nitro_token_stealer()
        elif choice == "55": section_55_browser_credential_harvest()
        elif choice == "56": section_56_geolocation_ip_matrix()
        elif choice == "57": section_57_discord_channel_nuke_engine()
        elif choice == "58": section_58_fake_windows_ransomware_screen()
        elif choice == "59": section_59_clipboard_spy_stream()
        elif choice == "60": section_60_fake_bios_flash_destruction()
        elif choice == "61": section_61_fake_fbi_subpoena_notice()
        elif choice == "62": section_62_discord_webhook_bombardment()
        elif choice == "63": section_63_stealth_backdoor_installer()
        elif choice == "64": section_64_omega_psychological_mindfuck()
        elif choice == "65": section_65_ultimate_void_shutdown()
        elif choice == "66":
            print(f"\n{RED}Severing connection into the void... Goodbye!{RESET}")
            break

if __name__ == "__main__":
    main()