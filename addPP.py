import os
import sys

def get_upf_filename(el):
    return f"{el}.pbe-{'dn' if el == 'Bi' else 'n'}-kjpaw_psl.1.0.0.UPF"

def update_scf_file(folder, elements):
    target_file = None
    for fname in os.listdir(folder):
        if fname.startswith('scf') and fname.endswith('.in'):
            target_file = fname
            break
    if not target_file:
        print(f"[!] No scf*.in file found in {folder}")
        return

    path = os.path.join(folder, target_file)
    with open(path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    inside = False
    for line in lines:
        if line.strip().startswith('ATOMIC_SPECIES'):
            inside = True
            new_lines.append(line)
            continue
        if inside:
            if not line.strip():
                inside = False
            else:
                tokens = line.strip().split()
                if tokens[0] in elements and tokens[2] == 'None':
                    new_lines.append(f"{tokens[0]} {tokens[1]} {get_upf_filename(tokens[0])}\n")
                    continue
        new_lines.append(line)

    with open(path, 'w') as f:
        f.writelines(new_lines)
    print(f"[✓] Updated: {target_file} in {folder}")

# 実行例: python addPP.py BiSBr Bi S Br
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py <folder_name> <element1> [element2 ...]")
        sys.exit(1)
    folder = sys.argv[1]
    elements = sys.argv[2:]
    update_scf_file(folder, elements)