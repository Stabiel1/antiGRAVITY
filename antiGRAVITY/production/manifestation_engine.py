import sys
import asyncio
from .trinity_core import TrinityCircle

async def bind_to_terminal():
    """
    The main interface for the antiGRAVITY Manifestation Builder.
    Allows the User (1-4-7) to input pure intention.
    """
    circle = TrinityCircle()
    
    print("\n" + "="*50)
    print(" antiGRAVITY Manifestation Engine v15.1.0 — The Named Trinity")
    print(" The Pure Circle is Open.")
    print(" 1-4-7 | 2-5-8 | 3-6-9 ACTIVATED")
    print("="*50 + "\n")
    
    while True:
        try:
            sys.stdout.write("[1-4-7] Speak your intention (or 'exit') > ")
            sys.stdout.flush()
            
            # Using thread for blocking IO to keep async loop clean
            intent = await asyncio.to_thread(sys.stdin.readline)
            intent = intent.strip()
            
            if not intent:
                continue
                
            if intent.lower() in ["exit", "quit", "red"]:
                print("\nShutting down the field. Circle closed.")
                break
                
            # Run the sequence
            final_state = circle.run_sequence(intent)
            
            # In a full system, here we would trigger git_sync if files were modified.
            print(f"\n[SYSTEM] Manifestation Result: {final_state['creation']}\n")
            
        except KeyboardInterrupt:
            print("\nShutting down the field. Circle closed.")
            break

if __name__ == "__main__":
    try:
        asyncio.run(bind_to_terminal())
    except KeyboardInterrupt:
        pass
