import subprocess
import sys


def run_custom_combo_maker():
    """Run the custom combo maker script"""
    print("Running custom combo maker...")
    subprocess.run([sys.executable, "custom-combo-maker.py"])


def run_roblox_checker():
    """Run the Roblox username checker script"""
    print("Running Roblox username checker...")
    subprocess.run([sys.executable, "roblox.py"])


def main():
    print("===  RBLX Username Sniper ===")
    print("1. Generate username combinations")
    print("2. Check Roblox username availability")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            run_custom_combo_maker()
        elif choice == "2":
            run_roblox_checker()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
