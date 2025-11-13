import requests
import json
import time

class TransactionClient:
    BASE_URL = "https://mock-node-wgqbnnxruha-as.a.run.app"
    MAX_ATTEMPTS = 15
    CHECK_INTERVAL_SECONDS = 5

    def __init__(self):
        print(f"Client initialized with base URL: {self.BASE_URL}")

    def broadcast_transaction(self, symbol: str, price: int, timestamp: int) -> str | None:
        endpoint = f"{self.BASE_URL}/broadcast"
        payload = {"symbol": symbol, "price": price, "timestamp": timestamp}
        
        print(f"Broadcasting: {json.dumps(payload)}")
        
        try:
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()
            data = response.json()
            tx_hash = data.get("tx_hash")
            if tx_hash:
                print(f"Success! Hash: {tx_hash}")
                return tx_hash
            else:
                print(f"Failed: No tx_hash in response: {data}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def monitor_status(self, tx_hash: str) -> str:
        print(f"Monitoring hash: {tx_hash}")
        
        for attempt in range(1, self.MAX_ATTEMPTS + 1):
            endpoint = f"{self.BASE_URL}/check/{tx_hash}"
            
            try:
                response = requests.get(endpoint)
                response.raise_for_status()
                data = response.json()
                status = data.get("tx_status")
                
                if status in ["CONFIRMED", "DNE"]:
                    print(f"Final status (attempt {attempt}): {status}")
                    return status
                elif status:
                    print(f"Status (attempt {attempt}): {status}. Retrying in {self.CHECK_INTERVAL_SECONDS}s...")
                else:
                    print(f"No status (attempt {attempt}). Retrying in {self.CHECK_INTERVAL_SECONDS}s...")
                    
            except requests.exceptions.RequestException as e:
                print(f"Error (attempt {attempt}): {e}. Retrying...")
            
            time.sleep(self.CHECK_INTERVAL_SECONDS)
        
        print(f"Timeout after {self.MAX_ATTEMPTS} attempts.")
        return "TIMEOUT"

# Example usage
def example():
    client = TransactionClient()
    symbol = "ETH"
    price = 4500
    timestamp = int(time.time())
    
    tx_hash = client.broadcast_transaction(symbol, price, timestamp)
    if tx_hash:
        final_status = client.monitor_status(tx_hash)
        print(f"Done. Hash: {tx_hash}, Status: {final_status}")
    else:
        print("Broadcast failed.")

if __name__ == "__main__":
    example()
