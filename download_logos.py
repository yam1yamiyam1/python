import urllib.request
import json
import os
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')

output_dir = "cloud_drip_logos"
for folder in ["NBA", "NFL", "MLB", "NHL", "Brands"]:
    os.makedirs(f"{output_dir}/{folder}", exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

BRANDS = {
    "Supreme":           "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Supreme_logo.svg/800px-Supreme_logo.svg.png",
    "BAPE":              "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/A_Bathing_Ape_logo.svg/800px-A_Bathing_Ape_logo.svg.png",
    "Carhartt":          "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Carhartt_logo.svg/800px-Carhartt_logo.svg.png",
    "Stussy":            "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Stussy_logo.svg/800px-Stussy_logo.svg.png",
    "Patagonia":         "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Patagonia_logo.svg/800px-Patagonia_logo.svg.png",
    "Adidas":            "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Adidas_Logo.svg/800px-Adidas_Logo.svg.png",
    "Nike":              "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Logo_NIKE.svg/800px-Logo_NIKE.svg.png",
    "Vans":              "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Vans-logo.svg/800px-Vans-logo.svg.png",
    "The_North_Face":    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/The_North_Face_logo.svg/800px-The_North_Face_logo.svg.png",
    "Oakley":            "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Oakley_logo.svg/800px-Oakley_logo.svg.png",
    "New_Era":           "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/New_Era_Cap_Company_logo.svg/800px-New_Era_Cap_Company_logo.svg.png",
    "Thrasher":          "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Thrasher_magazine_logo.svg/800px-Thrasher_magazine_logo.svg.png",
    "Lacoste":           "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Lacoste_logo.svg/800px-Lacoste_logo.svg.png",
    "Polo_Ralph_Lauren": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Polo_Ralph_Lauren_logo.svg/800px-Polo_Ralph_Lauren_logo.svg.png",
    "DC_Shoes":          "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/DC_Shoes_logo.svg/800px-DC_Shoes_logo.svg.png",
    "Monster_Energy":    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Monster_Energy_logo.svg/800px-Monster_Energy_logo.svg.png",
    "Arcteryx":          "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Arc%27teryx_logo.svg/800px-Arc%27teryx_logo.svg.png",
    "Mitchell_and_Ness": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Mitchell_%26_Ness_logo.svg/800px-Mitchell_%26_Ness_logo.svg.png",
}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read()

def get_all_teams(api_path):
    url = f"https://site.api.espn.com/apis/site/v2/sports/{api_path}/teams?limit=100"
    try:
        data = json.loads(fetch(url))
        teams = data["sports"][0]["leagues"][0]["teams"]
        # return name and abbreviation (e.g. "nyy", "lal")
        return [(t["team"]["displayName"], t["team"]["abbreviation"].lower()) for t in teams]
    except Exception as e:
        print(f"  [FAIL] Could not fetch team list -- {e}")
        return []

def download_team_logo(name, league_slug, abbrev, folder):
    safe_name = name.replace(" ", "_").replace("/", "_")
    path = f"{output_dir}/{folder}/{safe_name}.png"
    if os.path.exists(path):
        print(f"  [SKIP]  {name}")
        return
    # New ESPN combiner URL format
    url = f"https://a.espncdn.com/combiner/i?img=/i/teamlogos/{league_slug}/500/{abbrev}.png&h=500&w=500"
    try:
        data = fetch(url)
        with open(path, "wb") as f:
            f.write(data)
        print(f"  [OK]    {name}  ({abbrev})")
    except Exception as e:
        print(f"  [FAIL]  {name} -- {e}")
    time.sleep(0.25)

def download_brand(name, url):
    path = f"{output_dir}/Brands/{name}.png"
    if os.path.exists(path):
        print(f"  [SKIP]  {name}")
        return
    try:
        data = fetch(url)
        with open(path, "wb") as f:
            f.write(data)
        print(f"  [OK]    {name}")
    except Exception as e:
        print(f"  [FAIL]  {name} -- {e}")
    time.sleep(0.25)

LEAGUES = [
    ("basketball/nba", "nba", "NBA"),
    ("football/nfl",   "nfl", "NFL"),
    ("baseball/mlb",   "mlb", "MLB"),
    ("hockey/nhl",     "nhl", "NHL"),
]

for api_path, logo_slug, folder in LEAGUES:
    print(f"\n[{folder}] Fetching team list...")
    teams = get_all_teams(api_path)
    print(f"  Found {len(teams)} teams. Downloading logos...")
    for name, abbrev in teams:
        download_team_logo(name, logo_slug, abbrev, folder)

print("\n[BRANDS] Downloading brand logos...")
for name, url in BRANDS.items():
    download_brand(name, url)

total = sum(
    len(os.listdir(f"{output_dir}/{f}"))
    for f in ["NBA", "NFL", "MLB", "NHL", "Brands"]
    if os.path.exists(f"{output_dir}/{f}")
)
print(f"\n[DONE] {total} logos saved to '{output_dir}' folder.")
for f in ["NBA", "NFL", "MLB", "NHL", "Brands"]:
    count = len(os.listdir(f"{output_dir}/{f}"))
    print(f"  {f}: {count} files")
