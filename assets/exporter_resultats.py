#!/usr/bin/env python3
"""Exporter les résultats du kit existant, sans clés ni identifiants NFC."""
import json, urllib.request
from pathlib import Path

def main():
    keys = json.loads(Path("cles.json").read_text(encoding="utf-8"))
    request = urllib.request.Request("http://127.0.0.1:8765/api/state", headers={"Authorization": "Bearer " + keys["admin"]})
    with urllib.request.urlopen(request, timeout=20) as response:
        state = json.load(response)
    results = [{"name": r["name"], "laps": r["laps"], "best": r.get("best"), "pending": r.get("pending", 0)} for r in state["teams"]]
    out = Path("Resultats_Backyard_Magnee.json")
    out.write_text(json.dumps({"teams": results}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(str(len(results)) + " résultats exportés dans " + str(out))
    if any(r["pending"] for r in results):
        print("Des passages restent à vérifier dans le kit avant l'import sur le site.")
if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Export impossible. Lancez ce fichier depuis le dossier du kit de badges, avec le serveur local actif.")
        raise SystemExit(1)
