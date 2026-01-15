import json
from pathlib import Path
from typing import Optional, List, Dict

def load_vignettes() -> List[Dict]:
    path = Path(__file__).parent / "vignettes" / "ocd_core.json"
    return json.loads(path.read_text())

def pick_vignette(user_text: str, vignettes: List[Dict]) -> Optional[Dict]:
    t = user_text.lower()
    best = None
    best_score = 0

    for v in vignettes:
        score = 0
        for kw in v.get("keywords", []):
            if kw in t:
                score += 1
        if score > best_score:
            best_score = score
            best = v

    return best if best_score >= 1 else None