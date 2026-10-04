import json
import os
import time
from datetime import datetime

# Clear console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Load config.json
def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

def print_banner():
    print("\033[96m" + "+" + "-"*75 + "+")
    print("""|\033[97m
    ██████╗  ██████╗ ██╗     ██╗     ███████╗██████╗ 
    ██╔══██╗██╔═══██╗██║     ██║     ██╔════╝██╔══██╗
    ██████╔╝██║   ██║██║     ██║     █████╗  ██████╔╝
    ██╔══██╗██║   ██║██║     ██║     ██╔══╝  ██╔══██╗
    ██║  ██║╚██████╔╝███████╗███████╗███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝\033[96m
    """)
    print("  ROLLERCOIN AUTOMATION SYSTEM v2.0")
    print("  G H O F U R")
    print("+" + "-"*75 + "+\033[0m\n")

def main():
    clear_screen()
    print_banner()
    
    config = load_config()

    print("\033[93m" + "="*40 + " PILIH FITUR YANG AKAN DIJALANKAN " + "="*40 + "\033[0m\n")
    print(" [1] \U0001f439 Hamster (upgrade + expedition)")
    print(" [2] \U0001f3ae Game (main game otomatis)")
    print(" [3] \U0001f9ec Merge Miner")
    print(" [A] Jalankan SEMUA fitur di atas")
    print(" [Q] Keluar\n")

    choice = input("\033[96mPilih fitur (contoh: 1,2 atau A untuk semua): \033[0m").strip().lower()

    if choice == '1':
        feature = "hamster"
    elif choice == '2':
        feature = "game"
    elif choice == '3':
        feature = "merge"
    elif choice == 'a':
        feature = "semua"
    elif choice == 'q':
        print("Keluar...")
        return
    else:
        print("\033[91mPilihan tidak valid!\033[0m")
        return

    print(f"\n\033[92m✔ Fitur dipilih: {feature}\033[0m\n")

    if feature in ["game", "semua"]:
        print("\033[93m" + "="*40 + " KONFIGURASI GAME " + "="*40 + "\033[0m\n")
        print("Pilih game yang mau dimainkan (ketik nomor, pisahkan dengan koma):")
        print(" [A] Semua game (1-15)")
        games_list = [
            "Coin Click", "Token Blaster", "Flappy Rocket", "Cryptonoid", "Coin Match",
            "Crypto Hamster", "2048 Coin", "Coin Flip", "Dr. Hamster", "Token Surfer: Snow Ride",
            "Lambo Rider", "Hamster Climber", "Coin Fisher", "Mission Hampossible", "Crypto Hex"
        ]
        for idx, g in enumerate(games_list, 1):
            print(f" [{idx}] {g}")
        
        game_choice = input("\nPilih game (contoh: 1,2,3 atau A): ").strip()
        
        if game_choice.lower() == 'a':
            selected_games = list(range(1, 16))
            game_name_display = "Semua Game"
        else:
            try:
                selected_games = [int(x.strip()) for x in game_choice.split(",")]
                game_name_display = games_list[selected_games[0] - 1] if len(selected_games) == 1 else "Beberapa Game"
            except:
                selected_games = [3]
                game_name_display = "Flappy Rocket"

        print(f"\n\033[92m✔ Game dipilih: {game_name_display}\033[0m")
        print("Target level untuk setiap game (1-10, default 10):")
        print("Target win per game per level (default 15):")
        print("Durasi running (jam, default 1):\n")

        print("\033[93m📋 Konfigurasi Game:\033[0m")
        print(f"  • Game      : {game_name_display}")
        print(f"  • Target Level : {config.get('max_level_game', 10)}")
        print(f"  • Win/Level    : {config.get('win_per_level', 15)}")
        print(f"  • Durasi       : {config.get('time_game', 1)} jam")

        now = datetime.now().strftime("%Y:%m:%d ~ %H:%M:%S")
        print(f"\n\033[92m[{now}] → ✔ Config loaded\033[0m")
        print(f"\033[92m[{now}] → ✔ Tokens berhasil dimuat dari config.json\033[0m")

if __name__ == "__main__":
    main()