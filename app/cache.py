import json
_cache = {}

def get_user_profile(user_id: str):
    key = f"user:{user_id}"
    if key in _cache:
        print(f"✅ CACHE HIT: {key}")
        return _cache[key]
    
    print(f"💾 NEW CACHE: {key}")
    profile = {"country": "India", "risk": 25}
    _cache[key] = profile
    return profile
