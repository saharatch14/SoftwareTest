class TransactionClient {
    static BASE_URL = "https://mock-node-wgqbnnxruha-as.a.run.app";
    static MAX_ATTEMPTS = 15;
    static CHECK_INTERVAL_SECONDS = 5;

    constructor() {
        console.log(`Client initialized with base URL: ${this.constructor.BASE_URL}`);
    }

    async broadcastTransaction(symbol, price, timestamp) {
        const endpoint = `${this.constructor.BASE_URL}/broadcast`;
        const payload = { symbol, price, timestamp };
        
        console.log(`Broadcasting: ${JSON.stringify(payload)}`);
        
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            const data = await response.json();
            const txHash = data.tx_hash;
            if (txHash) {
                console.log(`Success! Hash: ${txHash}`);
                return txHash;
            } else {
                console.log(`Failed: No tx_hash in response: ${JSON.stringify(data)}`);
                return null;
            }
        } catch (e) {
            console.log(`Error: ${e.message}`);
            return null;
        }
    }

    async monitorStatus(txHash) {
        console.log(`Monitoring hash: ${txHash}`);
        
        for (let attempt = 1; attempt <= this.constructor.MAX_ATTEMPTS; attempt++) {
            const endpoint = `${this.constructor.BASE_URL}/check/${txHash}`;
            
            try {
                const response = await fetch(endpoint);
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                const data = await response.json();
                const status = data.tx_status;
                
                if (status === "CONFIRMED" || status === "DNE") {
                    console.log(`Final status (attempt ${attempt}): ${status}`);
                    return status;
                } else if (status) {
                    console.log(`Status (attempt ${attempt}): ${status}. Retrying in ${this.constructor.CHECK_INTERVAL_SECONDS}s...`);
                } else {
                    console.log(`No status (attempt ${attempt}). Retrying in ${this.constructor.CHECK_INTERVAL_SECONDS}s...`);
                }
            } catch (e) {
                console.log(`Error (attempt ${attempt}): ${e.message}. Retrying...`);
            }
            
            // Wait before retrying
            await new Promise(resolve => setTimeout(resolve, this.constructor.CHECK_INTERVAL_SECONDS * 1000));
        }
        
        console.log(`Timeout after ${this.constructor.MAX_ATTEMPTS} attempts.`);
        return "TIMEOUT";
    }
}

// Example usage
async function example() {
    const client = new TransactionClient();
    const symbol = "ETH";
    const price = 4500;
    const timestamp = Math.floor(Date.now() / 1000);
    
    const txHash = await client.broadcastTransaction(symbol, price, timestamp);
    if (txHash) {
        const finalStatus = await client.monitorStatus(txHash);
        console.log(`Done. Hash: ${txHash}, Status: ${finalStatus}`);
    } else {
        console.log("Broadcast failed.");
    }
}

// Run example if this script is executed directly (in Node.js or browser)
if (typeof window === 'undefined') {
    // Node.js
    example();
} else {
    // Browser: call example() manually or on load
    window.addEventListener('load', example);
}
