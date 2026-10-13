import subprocess
import os

SCRIPTS = [
    "build_ch1_full.py",
    "build_ch2_full.py",
    "build_ch3_full.py",
    "build_ch4_full.py",
    "build_ch5_full.py",
    "build_ch6_full.py",
    "build_ch7_full.py",
]

def main():
    print("Building all 7 comprehensive chapter guides...")
    for s in SCRIPTS:
        print(f"Running {s}...")
        res = subprocess.run(["python", s], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error in {s}:\n{res.stderr}")
        else:
            print(f"  {res.stdout.strip()}")

    print("\nAll chapters successfully compiled!")

if __name__ == "__main__":
    main()
