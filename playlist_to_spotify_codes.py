import os
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


#Picture Formating
CODES_FORMAT = "png"          
BG_HEX = "000000"             
CODE_COLOR = "white"          
SIZE = "640"                  
OUT_DIR = Path("spotify_codes")

SCANNABLES_BASE = "https://scannables.scdn.co/uri/plain"

#HELPERS
def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]+', "", name).strip()

def extract_playlist_id(playlist_link: str) -> str:
    """
    Accepts a playlist URL like:
      https://open.spotify.com/playlist/3cEYpjA9oz9GiPac4AsH4n
    or a URI like:
      spotify:playlist:3cEYpjA9oz9GiPac4AsH4n
    and returns the ID.
    """
    if playlist_link.startswith("spotify:"):
        parts = playlist_link.split(":")
        if len(parts) >= 3 and parts[1] == "playlist":
            return parts[2]
    path = urlparse(playlist_link).path
    return path.strip("/").split("/")[-1]

def build_code_url(spotify_uri: str) -> str:
    return f"{SCANNABLES_BASE}/{CODES_FORMAT}/{BG_HEX}/{CODE_COLOR}/{SIZE}/{spotify_uri}"

def download_image(url: str, out_path: Path, retries: int = 3):
    for attempt in range(retries):
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            out_path.write_bytes(r.content)
            return
        if r.status_code == 429:
            wait = int(r.headers.get("Retry-After", "2"))
            time.sleep(wait)
            continue
        time.sleep(1 + attempt)
    r.raise_for_status()

def playlist_to_codes(playlist_link: str):
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise RuntimeError("Set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables.")

    auth_manager = SpotifyClientCredentials()
    sp = Spotify(auth_manager=auth_manager, requests_timeout=30, retries=3, status_forcelist=(429, 500, 502, 503, 504))

    playlist_id = extract_playlist_id(playlist_link)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    results = sp.playlist_items(playlist_id, additional_types=("track",), limit=100)
    items = results["items"]
    while results.get("next"):
        results = sp.next(results)
        items.extend(results["items"])

    for idx, item in enumerate(items, start=1):
        track = item.get("track") or {}
        if track.get("type") != "track":
            continue
        track_id = track.get("id")
        name = track.get("name") or "Unknown Track"
        artists = ", ".join(a["name"] for a in track.get("artists", [])) or "Unknown Artist"
        if not track_id:
            continue

        uri = f"spotify:track:{track_id}"
        code_url = build_code_url(uri)

        filename = sanitize_filename(f"{artists} - {name}.{CODES_FORMAT}")
        out_path = OUT_DIR / filename
        try:
            download_image(code_url, out_path)
            print(f"[{idx}] Saved {out_path}")
        except Exception as e:
            print(f"[{idx}] Failed for {artists} - {name}: {e}")

if __name__ == "__main__":
    # Enter Playlist Link
    playlist_to_codes("...")
