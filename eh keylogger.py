print("=" * 50)
print("     KEYLOGGER INCIDENT RESPONSE SYSTEM")
print("=" * 50)

print("\n🚨 SECURITY ALERT")
print("Possible credential-capture behaviour detected.")
print("Device: EMPLOYEE-LAPTOP-07")
print("Severity: HIGH")

input("\nPress ENTER to begin investigation...")

# Incident Responder
print("\n🛡️ INCIDENT RESPONDER")
print("Checking system activity...")

events = [
    "Suspicious process detected",
    "Unusual keyboard-access behaviour",
    "Unknown outbound connection",
    "Authentication failure",
    "Multiple login attempts"
]

for event in events:
    print("  ⚠", event)

print("\nAssessment: SUSPICIOUS ACTIVITY DETECTED")

choice = input("\nIsolate affected device? (yes/no): ").lower()

if choice == "yes":
    print("✓ Device isolated from the network.")
else:
    print("⚠ Isolation not performed. Risk remains HIGH.")

input("\nPress ENTER for forensic analysis...")

# Forensic Analyst
print("\n🔎 FORENSIC ANALYST")
print("Reconstructing incident timeline...")

timeline = [
    "10:21 - Suspicious process",
    "10:22 - Keyboard-access behaviour",
    "10:25 - Unusual network activity",
    "10:29 - Authentication failure",
    "10:31 - Multiple login attempts",
    "10:32 - Security alert"
]

for item in timeline:
    print("  ", item)

print("\n✓ Evidence preserved.")
print("✓ Timeline documented.")

input("\nPress ENTER for threat intelligence analysis...")

# Threat Intelligence Analyst
print("\n🧠 THREAT INTELLIGENCE ANALYST")
print("Analysing observed behaviour...")

indicators = [
    "Credential-capture behaviour",
    "Suspicious process",
    "Unusual network connection",
    "Authentication anomalies"
]

for indicator in indicators:
    print("  •", indicator)

print("\nThreat assessment:")
print("POTENTIAL CREDENTIAL-STEALING MALWARE")
print("Risk Level: HIGH")

input("\nPress ENTER for legal review...")

# Legal Advisor
print("\n⚖️ LEGAL ADVISOR")
print("Checking investigation requirements...")

print("✓ Investigation authorization required")
print("✓ Employee privacy must be protected")
print("✓ Only relevant information should be collected")
print("✓ Evidence handling must be documented")

print("\nLegal status: INVESTIGATION APPROVED WITH CONTROLS")

input("\nPress ENTER for final decision...")

# Team Lead
print("\n👩‍💼 TEAM LEAD")
print("Reviewing all investigation findings...")

print("\nFINAL ASSESSMENT")
print("-" * 40)
print("Incident: SUSPECTED KEYLOGGER ACTIVITY")
print("Risk: HIGH")
print("Device: CONTAINED")
print("Evidence: PRESERVED")
print("Threat: POTENTIAL CREDENTIAL-STEALING MALWARE")

print("\nRecommended actions:")
print("1. Protect potentially compromised credentials")
print("2. Check other systems for similar indicators")
print("3. Continue forensic investigation")
print("4. Monitor affected accounts and systems")
print("5. Document and close the incident after verification")

print("\n" + "=" * 50)
print("          🔐 INCIDENT CONTAINED")
print("=" * 50)