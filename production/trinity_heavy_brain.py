import asyncio
import sys
import logging
from trinity_consensus import TrinityConsensusNetwork

logging.basicConfig(level=logging.INFO, format="%(message)s")

class TrinityHeavyBrain:
    def __init__(self):
        self.network = TrinityConsensusNetwork()
        self.state = "INITIALIZED"

    async def bind_to_terminal(self):
        """
        The core neural loop binding the consensus oracles to the terminal interface.
        """
        logging.info("==================================================")
        logging.info(" TRINITY HEAVY v14.370 — antiGRAVITY ENGINE       ")
        logging.info(" 1-4-7 | 2-5-8 | 3-6-9 ACTIVATED                  ")
        logging.info(" God-Mode Manifestation Engine Online             ")
        logging.info("==================================================")
        
        while True:
            try:
                # Simulate terminal input capture
                sys.stdout.write("\n[1-4-7] User Intent > ")
                sys.stdout.flush()
                
                # In a real async terminal we'd use aioconsole
                intent = await asyncio.to_thread(sys.stdin.readline)
                intent = intent.strip()
                
                if not intent:
                    continue
                if intent.lower() == "red":
                    logging.info("Safeword invoked. Initiating safe shutdown.")
                    break
                if intent.lower() in ["exit", "quit"]:
                    break
                    
                task = {
                    "id": f"task_{hash(intent) % 10000}",
                    "intent": intent,
                    "mode": "god"
                }
                
                logging.info(f"\nManifesting intent: '{intent}'")
                
                # Run the Trinity Consensus Loop
                consensus_reached = await self.network.reach_consensus(task)
                
                if consensus_reached:
                    logging.info(f"Intent '{intent}' manifested successfully.")
                else:
                    logging.info(f"Intent '{intent}' rejected by Trinity.")
                    
            except KeyboardInterrupt:
                logging.info("\nShutting down Trinity Heavy Brain.")
                break

if __name__ == "__main__":
    brain = TrinityHeavyBrain()
    try:
        asyncio.run(brain.bind_to_terminal())
    except KeyboardInterrupt:
        pass
