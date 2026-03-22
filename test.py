import os
import time

import requests

# Base URL from Mobalytics
BASE_URL = "https://cdn.mobalytics.gg/assets/tft/images/game-items/set16/{}.png?v=70"

# Your specific path
DOWNLOAD_DIR = r"C:\Users\Yuan\Documents\tft-assets"

# Dictionary using the exact CDN asset names (with apostrophes included)
TFT_ITEMS = {
    # --- BASE COMPONENTS ---
    "bf-sword": [],
    "chain-vest": [],
    "giant's-belt": [],
    "needlessly-large-rod": [],
    "negatron-cloak": [],
    "recurve-bow": [],
    "sparring-gloves": [],
    "spatula": [],
    "tear-of-the-goddess": [],
    "golden-frying-pan": [],  # Mobalytics uses golden-frying-pan for the base pan
    # --- CRAFTED ITEMS ---
    # B.F. Sword Combinations
    "deathblade": ["bf-sword", "bf-sword"],
    "giant-slayer": ["bf-sword", "recurve-bow"],
    "infinity-edge": ["bf-sword", "sparring-gloves"],
    "bloodthirster": ["bf-sword", "negatron-cloak"],
    "spear-of-shojin": ["bf-sword", "tear-of-the-goddess"],
    "hextech-gunblade": ["bf-sword", "needlessly-large-rod"],
    "edge-of-night": ["bf-sword", "chain-vest"],
    "sterak's-gage": ["bf-sword", "giant's-belt"],
    # Chain Vest Combinations
    "bramble-vest": ["chain-vest", "chain-vest"],
    "gargoyle-stoneplate": ["chain-vest", "negatron-cloak"],
    "sunfire-cape": ["chain-vest", "giant's-belt"],
    "protector's-vow": ["chain-vest", "tear-of-the-goddess"],
    "crownguard": ["chain-vest", "needlessly-large-rod"],
    "titan's-resolve": ["chain-vest", "recurve-bow"],
    "steadfast-amulet": ["chain-vest", "sparring-gloves"],  # Steadfast Heart asset name
    # Giant's Belt Combinations
    "warmog's-armor": ["giant's-belt", "giant's-belt"],
    "morellonomicon": ["giant's-belt", "needlessly-large-rod"],
    "red-buff": ["giant's-belt", "recurve-bow"],
    "evenshroud": ["giant's-belt", "negatron-cloak"],
    "adaptive-helm": ["giant's-belt", "tear-of-the-goddess"],
    "striker's-flail": ["giant's-belt", "sparring-gloves"],
    # Needlessly Large Rod Combinations
    "rabadon's-deathcap": ["needlessly-large-rod", "needlessly-large-rod"],
    "ionic-spark": ["needlessly-large-rod", "negatron-cloak"],
    "guinsoo's-rageblade": ["needlessly-large-rod", "recurve-bow"],
    "jeweled-gauntlet": ["needlessly-large-rod", "sparring-gloves"],
    "archangel's-staff": ["needlessly-large-rod", "tear-of-the-goddess"],
    # Negatron Cloak Combinations
    "dragon's-claw": ["negatron-cloak", "negatron-cloak"],
    "runaan's-hurricane": ["negatron-cloak", "recurve-bow"],
    "quicksilver": ["negatron-cloak", "sparring-gloves"],
    # Recurve Bow Combinations
    "kraken's-fury": ["recurve-bow", "recurve-bow"],
    "last-whisper": ["recurve-bow", "sparring-gloves"],
    "statikk-shiv": ["recurve-bow", "tear-of-the-goddess"],
    "nashor's-tooth": ["recurve-bow", "giant's-belt"],
    # Sparring Gloves Combinations
    "thief's-gloves": ["sparring-gloves", "sparring-gloves"],
    "hand-of-justice": ["sparring-gloves", "tear-of-the-goddess"],
    # Tear of the Goddess Combinations
    "blue-buff": ["tear-of-the-goddess", "tear-of-the-goddess"],
    # Spatula & Pan Combinations
    "tactician's-crown": ["spatula", "spatula"],
    "tactician's-shield": ["spatula", "golden-frying-pan"],
    "tactician's-cape": ["golden-frying-pan", "golden-frying-pan"],
}


def setup_directory():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
        print(f"Created folder: {DOWNLOAD_DIR}")


def download_item(item_slug):
    url = BASE_URL.format(item_slug)
    file_path = os.path.join(DOWNLOAD_DIR, f"{item_slug}.png")

    if os.path.exists(file_path):
        print(f"Skipping {item_slug}.png (Already exists)")
        return

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {item_slug}.png")
        else:
            print(f"Failed: {item_slug}.png (Status: {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {item_slug}.png: {e}")


def main():
    print(f"Starting download of {len(TFT_ITEMS)} TFT items...\n")
    setup_directory()

    for item_slug in TFT_ITEMS.keys():
        download_item(item_slug)
        time.sleep(0.1)

    print(f"\nAll done! Assets have been saved to {DOWNLOAD_DIR}")


if __name__ == "__main__":
    main()
