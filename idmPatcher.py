import sys
from pathlib import Path

# 001202E4
# "2YOPB3AQCVUXMNRS97WE0IZD4KLFGHJ8165T0"
PATCHES = [
    (
        "50 8b 0d ?? ?? ?? ?? 51 ff 15 ?? ?? ?? ?? 85 c0 ?? ?? ?? ?? ?? ?? c6 85 4f f5 ff ff 01",
        "50 8b 0d ?? ?? ?? ?? 51 ff 15 ?? ?? ?? ?? 33 c0 ?? ?? ?? ?? ?? ?? c6 85 4f f5 ff ff 01",
    ),
    (
        "89 5D D4 89 5D FC A1 ?? ?? ?? ?? F7 D8 1B C0 83 E0 0F 83 C0 0F",
        "89 5D D4 89 5D FC A1 ?? ?? ?? ?? F7 D8 1B C0 b8 ff ff ff f7 90",
    ),
    (
        "C6 45 FC 03 39 1D ?? ?? ?? ?? 74 ?? 8B 0D ?? ?? ?? ?? 51",
        "C6 45 FC 03 39 1D ?? ?? ?? ?? EB ?? 8B 0D ?? ?? ?? ?? 51",
    ),
    (
        "8D ?? ?? ?? E8 ?? ?? ?? ?? 84 C0 74 ?? 80 7C 24 07 00 75 ?? C7 44 24 14 FF FF FF FF 8D",
        "8D ?? ?? ?? E8 ?? ?? ?? ?? 84 C0 EB ?? 80 7C 24 07 00 75 ?? C7 44 24 14 FF FF FF FF 8D",
    ),
    (
        "?? FF 68 ?? ?? ?? ?? 64 A1 00 00 00 00 50 81 EC 64 01 00 00 A1 ?? ?? ?? ?? 33 C4 89 84 24 60 01 00 00 53 56",
        "C3 FF 68 ?? ?? ?? ?? 64 A1 00 00 00 00 50 81 EC 64 01 00 00 A1 ?? ?? ?? ?? 33 C4 89 84 24 60 01 00 00 53 56",
    ),
    (
        "?? FF 68 ?? ?? ?? ?? 64 A1 00 00 00 00 50 81 EC C4 01 00 00 A1 ?? ?? ?? ?? 33 C4 89 84 24 ?? 01 00 00 53 55 56",
        "C3 90 68 ?? ?? ?? ?? 64 A1 00 00 00 00 50 81 EC C4 01 00 00 A1 ?? ?? ?? ?? 33 C4 89 84 24 ?? 01 00 00 53 55 56",
    ),
    (
        "55 8B EC 83 E4 F8 6A FF 68 ?? ?? ?? ?? 64 A1 00 00 00 00 50 81 EC CC 01 00 00",
        "C3 8B EC 83 E4 F8 6A FF 68 ?? ?? ?? ?? 64 A1 00 00 00 00 50 81 EC CC 01 00 00",
    ),
    (
        "40 84 C9 75 ?? 2B C2 83 F8 02 0F 85 ?? ?? ?? ?? ?? ?? ?? ?? ?? 85 C0",
        "40 84 C9 75 ?? 2B C2 83 F8 02 90 E9 ?? ?? ?? ?? ?? ?? ?? ?? ?? 85 C0",
    ),
    (
        "C6 44 24 0F 00 E8 ?? ?? ?? ?? 84 C0 74 ?? 80 7C ?? ?? ??",
        "C6 44 24 0F 00 E8 ?? ?? ?? ?? 84 C0 EB ?? 80 7C ?? ?? ??",
    ),
    (
        "CC CC 6A FF 68 ?? ?? ?? ?? ?? A1 00 00 00 00 50 83 EC ?? A1 ?? ?? ?? ?? 33 C4 89 44 ?? ?? 53 56 57 A1 ?? ?? ?? ?? 33 C4 50 8D 44 ?? ?? ?? A3 00 00 00 00 8B ?? E8 ?? ?? ?? ?? 8B",
        "CC CC 90 C3 68 ?? ?? ?? ?? ?? A1 00 00 00 00 50 83 EC ?? A1 ?? ?? ?? ?? 33 C4 89 44 ?? ?? 53 56 57 A1 ?? ?? ?? ?? 33 C4 50 8D 44 ?? ?? ?? A3 00 00 00 00 8B ?? E8 ?? ?? ?? ?? 8B",
    ),
    (
        "01 00 00 00 01 00 00 00 1E 00 00 00",
        "01 00 00 00 00 00 00 00 FF FF FF 7F",
    ),
    (
        "?? ?? ?? ?? 75 54 C7 05 ?? ?? 75 00 ?? 00 00 00 8D 95 EC 03 00 00",
        "?? ?? ?? ?? 90 90 C7 05 ?? ?? 75 00 01 00 00 00 8D 95 EC 03 00 00",
    ),
    (
        "53 8D 8D ?? FC FF FF E8 ?? ?? 0C 00 C6 45 FC ??",
        "53 8D 8D ?? FC FF FF 90 90 90 90 90 C6 45 FC ??",
    ),
    (
        "8D 4C 24 18 E8 ?? ?? ?? ?? 3B EB 74 09 8B 4C 24 34 E8 F4 F1 FF FF 8B 8C 24 DC 00 00 00 64 89 0D 00 00 00 00 59 5F 5E 5D 5B 8B 8C 24 C4 00 00 00 33 CC E8 ?? ?? ?? ?? 81 C4 D4 00 00 00 C3",
        "8D 4C 24 18 E8 ?? ?? ?? ?? 3B EB 74 09 90 90 90 90 90 90 90 90 90 8B 8C 24 DC 00 00 00 64 89 0D 00 00 00 00 59 5F 5E 5D 5B 8B 8C 24 C4 00 00 00 33 CC E8 ?? ?? ?? ?? 81 C4 D4 00 00 00 C3",
    ),
    (
        "50 8B 0D ?? ?? ?? 00 51 FF 15 ?? ?? ?? 00 85 C0 74 0C 8B CB E8 ?? ?? FF FF E9 BD 00 00 00 89 7D DC 8D 55 DC 52",
        "50 8B 0D ?? ?? ?? 00 51 FF 15 ?? ?? ?? 00 85 C0 EB 0C 90 90 90 90 90 90 90 E9 BD 00 00 00 89 7D DC 8D 55 DC 52"
    ),
    (
        "6A 1D 8b 4d cc e8 ?? ?? fb ff",
        "6A 1D 90 90 90 90 90 90 90 90"
    )
]


def parse_pattern(pattern_str):
    bytes_out = []
    mask = []

    for b in pattern_str.split():
        if b == "??":
            bytes_out.append(0x00)
            mask.append(False)
        else:
            bytes_out.append(int(b, 16))
            mask.append(True)

    return bytes(bytes_out), mask


def scan_pattern(data, search_bytes, search_mask):
    """Count how many times a pattern occurs without modifying data"""
    pat_len = len(search_bytes)
    count = 0

    for i in range(len(data) - pat_len + 1):
        for j in range(pat_len):
            if search_mask[j] and data[i + j] != search_bytes[j]:
                break
        else:
            count += 1

    return count


def apply_patch(data, search_bytes, search_mask, replace_bytes, replace_mask):
    data = bytearray(data)
    pat_len = len(search_bytes)
    count = 0

    for i in range(len(data) - pat_len + 1):
        for j in range(pat_len):
            if search_mask[j] and data[i + j] != search_bytes[j]:
                break
        else:
            for j in range(pat_len):
                if replace_mask[j]:
                    data[i + j] = replace_bytes[j]
            count += 1

    return bytes(data), count


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.exe> [--dry-run]")
        sys.exit(1)

    exe_path = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv
    overwrite = "--overwrite" in sys.argv or "-o" in sys.argv

    if not exe_path.exists():
        print("File not found.")
        sys.exit(1)
        
    print(f"Source EXE: {exe_path}")

    data = exe_path.read_bytes()
    total_matches = 0
    
    

    print("Dry-run mode ON\n" if dry_run else "")

    for idx, (search, replace) in enumerate(PATCHES, 1):
        search_bytes, search_mask = parse_pattern(search)
        replace_bytes, replace_mask = parse_pattern(replace)

        if len(search_bytes) != len(replace_bytes):
            print(f"[!] Patch {idx}: search/replace length mismatch")
            continue

        if dry_run:
            count = scan_pattern(data, search_bytes, search_mask)
            print(f"[=] Patch {idx}: would apply {count} time(s)")
        else:
            data, count = apply_patch(
                data,
                search_bytes,
                search_mask,
                replace_bytes,
                replace_mask,
            )
            print(f"[+] Patch {idx}: applied {count} time(s)")

        total_matches += count

    if dry_run:
        if not overwrite:
            path = exe_path.with_suffix(".xex")
            print(f"Destination EXE: {path}")
        else:
            print(f"Destination EXE: {exe_path}")
        print(f"✔  Dry-run complete. Total matches found: {total_matches}")
        print("✔  No files were modified.")
        return

    if total_matches > 0:
        print(f"\n✔  Done. Total patches applied: {total_matches}")
        if overwrite:
            exe_path.write_bytes(data)
            print(f"Patched EXE: {exe_path}")
        else:
            path = exe_path.with_suffix(".xex")
            path.write_bytes(data)
            print(f"Patched EXE: {path}")
    else:
        print("\n✖  No patterns matched. File not modified.")


if __name__ == "__main__":
    main()
