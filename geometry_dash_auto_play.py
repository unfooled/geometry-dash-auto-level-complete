import pyautogui
import time
import os

# --- PATH FIX ---
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):
    return os.path.join(BASE_PATH, filename)

# --- CONFIG ---
pyautogui.FAILSAFE = True 
CONF_LEVEL = 0.8  
# --------------

def safe_locate(image_name, conf=0.7, region=None):
    """Prevents crashing when image isn't found."""
    try:
        img_path = get_path(image_name)
        return pyautogui.locateOnScreen(img_path, confidence=conf, region=region)
    except:
        return None

def find_and_click(image_name, name, conf=CONF_LEVEL, region=None):
    location = safe_locate(image_name, conf, region)
    if location:
        # THE FIX: Explicit Move + Simple Click
        # This is what fixed the ghost clicks in the past!
        center_pt = pyautogui.center(location)
        pyautogui.moveTo(center_pt)
        time.sleep(0.05) # Tiny pause for GD to recognize the hover
        pyautogui.click(center_pt)
        print(f"[ACTION] Clicked {name}")
        return True
    return False

print("==========================================")
print("   GD FARMER: ULTIMATE GHOST-PROOF       ")
print("==========================================")
print("Starting in 5 seconds...")
time.sleep(5)

farmed_count = 0
search_attempts = 0 

try:
    while True:
        # STEP 1: Search for 'get_it.png'
        if find_and_click('get_it.png', 'GET IT'):
            farmed_count += 1
            search_attempts = 0 
            
            # STEP 2: THE MAIN PLAY HUNTER (Now using your 'Perfect' Popup logic)
            print("[WAITING] Level selected. Hunting for Main Play button...")
            while True:
                time.sleep(1.0) 
                # If it's still there, click it. If it's gone, move to popups.
                if find_and_click('play_main.png', 'MAIN ROUND PLAY'):
                    time.sleep(1.0)
                    continue 
                else:
                    break 
            
            # STEP 3: THE POPUP HUNTER (Kept exactly as you liked it)
            print("[WAITING] Handling popups...")
            while True:
                time.sleep(1.2)
                if find_and_click('play_popup.png', 'RECTANGLE POPUP PLAY'):
                    continue 
                else:
                    break 
                    
            # STEP 4: FARMING (WAITING FOR THE FINISH ICON)
            print(f"Farming Level #{farmed_count}...")
            while True:
                if safe_locate('level_finished.png', conf=0.7):
                    print("[WIN] Level finished icon detected!")
                    break
                time.sleep(0.5)
            
            # STEP 5: EXIT AND START HEALING (ESC ESC -> Then Verify)
            print("[EXITING] Doing ESC ESC then starting healing...")
            pyautogui.press('esc')   
            time.sleep(1.2)          
            pyautogui.press('esc')   
            
            # THE HEALING PROCESS
            while True:
                # CHECK A: Found Purple Arrow -> Go to next search/scroll
                if safe_locate('pink_arrow.png', conf=0.7):
                    print("[SUCCESS] Back at list. Moving to search/scroll phase.")
                    break
                
                # CHECK B: Found Search Icon -> Click it and then start scroll
                elif find_and_click('search_icon.png', 'SEARCH ICON'):
                    print("[FIX] On search page. Returning to list...")
                    time.sleep(1.5) 
                    break
                
                # CHECK C: Still Lost -> Press ESC and try again
                else:
                    print("[RETRY] Still lost. Pressing ESC...")
                    pyautogui.press('esc')
                    time.sleep(1.2)
            
            time.sleep(1.0)
        
        else:
            # STEP 6: SCROLLING (8 attempts for full coverage)
            search_attempts += 1
            print(f"[SEARCHING] Attempt {search_attempts}/8 - Flicking Scroll...")
            
            for _ in range(15): 
                pyautogui.scroll(-140) 
                time.sleep(0.005) 
            
            time.sleep(0.6) 
            
            if search_attempts >= 8:
                print(">>> End of Page. Hunting for RIGHT Pink Arrow...")
                if find_and_click('pink_arrow.png', 'RIGHT PINK ARROW'):
                    print("--- LOADING NEXT PAGE ---")
                    time.sleep(5) 
                    search_attempts = 0 
                else:
                    search_attempts = 0 
                    for _ in range(5):
                        pyautogui.scroll(-100)
                        time.sleep(0.005)

except pyautogui.FailSafeException:
    print("\n[STOPPED] Emergency stop.")
except KeyboardInterrupt:
    print("\n[STOPPED] Manual stop.")
