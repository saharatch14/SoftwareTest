# Transaction Broadcasting and Monitoring Client

Installation Transaction Broadcasting and Monitoring Client

## Python

You must first install library:

```Bash
pip install requests
```

1. Create Instance from class TransactionClient in your application

    ```Python
    client = TransactionClient()
    ```

2. Call the broadcast_transaction method with the desired transaction data.
    Input: symbol (str), price (int), timestamp (int)
    Output: Returns the tx_hash (str) if successful; otherwise, it returns None.

    ```Python
    tx_hash = client.broadcast_transaction("BTC", 4500, 1678912345)
    ```

3. Call the monitor_status method using the received tx_hash.
   Strategy: This method automatically polls (sends repeated requests) every 5 seconds (defined by CHECK_INTERVAL_SECONDS) and stops when the status is CONFIRMED or DNE (Transaction does not exist) or when a specified number of attempts (MAX_ATTEMPTS) have been reached.

   Output: Returns the last status received (e.g., "CONFIRMED").

    ```Python
    if tx_hash:
        final_status = client.monitor_status(tx_hash)
        print(f"Status: {final_status}")
    ```

    Transaction Status Monitoring:
    | tx_status | monitor_status |
    | ---- | ---- |
    |`CONFIRMED`| Transaction has been processed and confirmed |
    |`FAILED`| Transaction failed to process |
    |`PENDING`| Transaction is awaiting processing |
    |`DNE`| Transaction does not exist |


## JavaScript

1. Setup:
   * Ensure you have a JavaScript runtime (e.g., Node.js for server-side, or a browser for client-side).
   * Install dependencies if needed: For Node.js, use `npm install node-fetch`
    
2. Initialization:
   * Create an instance of TransactionClient. It uses hardcoded URLs but can be customized if the API changes.

3. Broadcasting a Transaction:
   * Call broadcastTransaction(symbol, price, timestamp) with your data.
   * Returns a promise resolving to the tx_hash (string).
   * Example payload: { symbol: "ETH", price: 4500, timestamp: 1678912345 }.
  
4. Checking Status:
   * Call checkTransactionStatus(txHash) with the hash.
   * Returns a promise resolving to the status string.

5. Monitoring:
   * Call monitorTransaction(txHash, checkInterval, maxAttempts) to poll until resolution.
   * checkInterval: Seconds between checks (In case Set default: 5).
   * maxAttempts: Max polls before giving up (In case Set default: 20).
   * Returns a promise resolving to the final status.

6. Error Handling:
   * Wrap calls in try/catch for network errors or API failures.
   * The client throws errors on bad HTTP responses.

7. Best Practices:
    * Use in async functions with await.
    * For production: Add logging, retries, and handle rate limits.
    * Integration example: In a web app, broadcast on user action, then monitor and update UI.
    * Testing: Use the mock API for development; replace URLs for real nodes.

8. Customization:
   * Modify URLs in the constructor for different environments.
   * Extend methods for additional features (e.g., batch broadcasts).
