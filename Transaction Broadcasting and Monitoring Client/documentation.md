# Transaction Broadcasting and Monitoring Client
Broadcast Transaction

request to
`https://mock-node-wgqbnxruha-as.a.run.app/broadcast`.

Endpoint: /broadcast

Method: POST

Input Parameters: symbol (string), price (uint64), timestamp (uint64)

Payload (JSON):

|Json structure
|{|
|  "symbol": string,|
|  "price": uint64,|
|  "timestamp": uint64|
|}|
|----------------------------------------------|

Installation Transaction Broadcasting and Monitoring Client

## Python
===

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
    tx_hash = client.broadcast_transaction("BTC", 65000, 1700000000)
    ```

3. Call the monitor_status method using the received tx_hash.
   Strategy: This method automatically polls (sends repeated requests) every 5 seconds (defined by CHECK_INTERVAL_SECONDS) and stops when the status is CONFIRMED or DNE (Transaction does not exist) or when a specified number of attempts (MAX_ATTEMPTS) have been reached.

   Output: Returns the last status received (e.g., "CONFIRMED").

    ```Python
    if tx_hash:
        final_status = client.monitor_status(tx_hash)
        print(f"Status: {final_status}")
    ```