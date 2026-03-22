import asyncio
import random
from datetime import datetime
import json

async def generate_transaction():
    return {
        "id": random.randint(1000, 9999),
        "user": f"user{random.randint(100,999)}",
        "amount": round(random.uniform(10, 5000), 2),
        "timestamp": datetime.now().isoformat(),
        "risk": random.choice(["LOW", "MEDIUM", "HIGH"])
    }

async def main():
    for i in range(5):
        tx = await generate_transaction()
        print(json.dumps(tx, indent=2))
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
