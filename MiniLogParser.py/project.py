import re

# ============================================================
# Task 1: Named Groups for Log Entries
# ============================================================

log = """2024-06-01 08:15:32 ERROR user=john msg=Disk full
2024-06-01 08:16:10 WARN user=ram msg=Low memory
2024-06-01 08:17:05 INFO user=john msg=Login successful
2024-06-01 08:18:20 ERROR user=ram msg=Connection failed
2024-06-01 08:19:45 INFO user=alex msg=File opened"""

# Named groups capture timestamp, level, user and message.
pattern = (
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
    r'(?P<level>ERROR|WARN|INFO) '
    r'user=(?P<user>\w+) '
    r'msg=(?P<msg>.*)'
)

print("Task 1: Pattern created successfully")


# ============================================================
# Task 2: Parse Log Entries using re.finditer()
# ============================================================

entries = []

for match in re.finditer(pattern, log):
    entries.append(match.groupdict())

print("\nTask 2: Parsed Entries")

for entry in entries:
    print(entry)


# ============================================================
# Task 3: Count ERROR, WARN and INFO Entries
# ============================================================

error_count = 0
warn_count = 0
info_count = 0

for entry in entries:
    if entry["level"] == "ERROR":
        error_count += 1
    elif entry["level"] == "WARN":
        warn_count += 1
    elif entry["level"] == "INFO":
        info_count += 1

print("\nTask 3: Summary")
print("ERROR:", error_count)
print("WARN :", warn_count)
print("INFO :", info_count)


# ============================================================
# Task 4: Redact User Names
# ============================================================

# Replace only user=<name>; everything else remains unchanged.
redacted_log = re.sub(r'user=\w+', 'user=<hidden>', log)

print("\nTask 4: Redacted Log")
print(redacted_log)


# ============================================================
# Task 5: Sort by User and Print ERROR Entries
# ============================================================

# Sort the dictionaries alphabetically by user name.
sorted_entries = sorted(entries, key=lambda x: x["user"])

print("\nTask 5: ERROR Entries by User")

for entry in sorted_entries:
    if entry["level"] == "ERROR":
        print(entry)