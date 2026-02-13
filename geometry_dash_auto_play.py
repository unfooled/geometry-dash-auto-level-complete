import pyautogui
import time
import os

# --- PATH FIX ---
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):
    return os.path.join(BASE_PATH, filename)

# --- CONFIG ---
pyautogui.FAILSAFE = True 
CONF_LEVEL = 0.8  # Using the 0.8 you had in your script
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
        # THE FIX: Added duration=0.1 so GD cannot ignore the click
        pyautogui.click(pyautogui.center(location), duration=0.1)
        print(f"[ACTION] Clicked {name}")
        return True
    return False

print("==========================================")
print("   GD FARMER: ROBUST CLICK & HEAL        ")
print("==========================================")
print("Starting in 5 seconds...")
time.sleep(5)

farmed_count = 0
search_attempts = 0 
screen_width, screen_height = pyautogui.size()

try:
    while True:
        # STEP 1: Search for 'get_it.png'
        if find_and_click('get_it.png', 'GET IT'):
            farmed_count += 1
            search_attempts = 0 
            
            # STEP 2: WAIT FOR GREEN BUTTON (Exact loop from your old script)
            print("[WAITING] Level selected. Waiting for Main Play button...")
            while True:
                if find_and_click('play_main.png', 'MAIN ROUND PLAY'):
                    break 
                time.sleep(1) 
            
            # STEP 3: THE POPUP HUNTER (Exact loop from your old script)
            while True:
                time.sleep(1.2)
                if find_and_click('play_popup.png', 'RECTANGLE POPUP PLAY'):
                    continue 
                else:
                    break 
                    
            # STEP 4: FARMING (Wait for the finish icon you sent)
            print(f"Farming Level #{farmed_count}...")
            while True:
                # 'level_finished.png' is the icon with the dots/bars
                if safe_locate('level_finished.png', conf=0.7):
                    print("[WIN] Level finished icon detected!")
                    break
                time.sleep(0.5)
            
            # STEP 5: EXIT AND HEALING (ESC ESC -> Then Verify)
            print("[EXITING] Doing ESC ESC then starting healing...")
            pyautogui.press('esc')   
            time.sleep(1.2)          
            pyautogui.press('esc')   
            
            # THE HEALING PROCESS
            while True:
                # CHECK A: If Purple Arrow found -> Success, break and start scrolling
                if safe_locate('pink_arrow.png', conf=0.7):
                    print("[SUCCESS] Back at list. Moving to scrolling phase.")
                    break
                
                # CHECK B: If Search Icon found -> Click it, then break to start scrolling
                elif find_and_click('search_icon.png', 'SEARCH ICON'):
                    print("[FIX] On search page. Returning to list and starting scroll...")
                    time.sleep(1.5) 
                    break
                
                # CHECK C: Still Lost -> Press ESC and try checks again
                else:
                    print("[RETRY] Still lost. Pressing ESC...")
                    pyautogui.press('esc')
                    time.sleep(1.2)
            
            time.sleep(1.0)
        
        else:
            # STEP 6: SCROLLING (8 attempts for full page coverage)
            search_attempts += 1
            print(f"[SEARCHING] Attempt {search_attempts}/8 - Flicking Scroll...")
            
            # The "Flick" loop to make Windows scroll actually move
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
                    # Smaller flick if we are stuck at the bottom
                    for _ in range(5):
                        pyautogui.scroll(-100)
                        time.sleep(0.005)

except pyautogui.FailSafeException:
    print("\n[STOPPED] Emergency stop.")
except KeyboardInterrupt:
    print("\n[STOPPED] Manual stop.")
