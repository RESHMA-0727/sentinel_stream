import asyncio
import json
from datetime import datetime, timedelta
from collections import defaultdict

class Sentinel:
    def __init__(self):
        self.rules = {
            "high_value": {"threshold": 1000, "action": "BLOCK"},
            "velocity": {"threshold": 3, "window": 3600, "action": "FLAG"}
        }
        self.user_history = defaultdict(list)
    
    async def score_transaction(self, tx):
        score = 0
        reasons = []
        
        # High value rule
        if tx["amount"] > self.rules["high_value"]["threshold"]:
            score += 80
            reasons.append("HIGH_VALUE")
        
        # Velocity rule
        history = self.user_history[tx["user"]]
        recent = [h for h in history if datetime.fromisoformat(h["timestamp"]) > 
                 datetime.now() - timedelta(hours=1)]
        if len(recent) > self.rules["velocity"]["threshold"]:
            score += 60
            reasons.append("VELOCITY")
        
        self.user_history[tx["user"]].append(tx)
        
        status = "BLOCK" if score > 70 else "ALLOW" if score > 30 else "OK"
        return {"score": score, "status": status, "reasons": reasons}

async def main():
    sentinel = Sentinel()
    tx = {"id": 1234, "user": "user456", "amount": 2500, "timestamp": datetime.now().isoformat()}
    result = await sentinel.score_transaction(tx)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
