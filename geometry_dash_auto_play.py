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

# HEAVY-DUTY: Used ONLY for the Main Green Button to kill ghost clicks
def main_button_click(image_name, name):
    location = safe_locate(image_name, CONF_LEVEL)
    if location:
        center_pt = pyautogui.center(location)
        # The 'moveTo' wake-up call for GD that stops ghost clicks
        pyautogui.moveTo(center_pt, duration=0.1) 
        pyautogui.click(center_pt)
        print(f"[ACTION] Heavy-Clicked {name}")
        return True
    return False

# FAST-SNAP: Used for everything else (Exactly like your old code)
def fast_click(image_name, name, region=None):
    location = safe_locate(image_name, CONF_LEVEL, region=region)
    if location:
        pyautogui.click(pyautogui.center(location))
        print(f"[ACTION] Fast-Clicked {name}")
        return True
    return False

print("==========================================")
print("   GD FARMER: THE FINAL STRIKE           ")
print("==========================================")
print("Starting in 5 seconds...")
time.sleep(5)

farmed_count = 0
search_attempts = 0 
screen_width, screen_height = pyautogui.size()
right_half = (screen_width // 2, 0, screen_width // 2, screen_height)

try:
    while True:
        # STEP 1: Search for 'get_it.png'
        if fast_click('get_it.png', 'GET IT'):
            farmed_count += 1
            search_attempts = 0 
            
            # STEP 2: THE MAIN BUTTON (Heavy-Duty + Loop)
            print("[WAITING] Level selected. Hunting Main Play button...")
            while True:
                if main_button_click('play_main.png', 'MAIN ROUND PLAY'):
                    time.sleep(0.5) 
                    continue 
                else:
                    break 
            
            # STEP 3: THE POPUP SNAPPERS (Fast as hell)
            print("[WAITING] Snapping popups...")
            while True:
                if fast_click('play_popup.png', 'RECTANGLE POPUP PLAY'):
                    # No moveTo, no delay. Just snap it.
                    continue 
                else:
                    break 
                    
            # STEP 4: FARMING (WAITING FOR THE FINISH ICON)
            print(f"Farming Level #{farmed_count}...")
            while True:
                if safe_locate('level_finished.png', conf=0.7):
                    print("[WIN] Finish icon found!")
                    break
                time.sleep(0.5)
            
            # STEP 5: ESCAPE AND HEALING
            print("[EXITING] Doing ESC ESC then starting healing...")
            pyautogui.press('esc')   
            time.sleep(1.2)          
            pyautogui.press('esc')   
            
            # Verify we are back on the list before scrolling
            while True:
                if safe_locate('pink_arrow.png', conf=0.7):
                    print("[SUCCESS] Found Purple Arrow. Proceeding...")
                    break
                elif fast_click('search_icon.png', 'SEARCH ICON'):
                    print("[FIX] On search page. Returning to list...")
                    time.sleep(1.0) 
                    break
                else:
                    print("[RETRY] Still lost. Pressing ESC...")
                    pyautogui.press('esc')
                    time.sleep(1.2)
            
            time.sleep(1.0)
        
        else:
            # STEP 6: THE 8-ATTEMPT FLICK SCROLL (Your exact logic)
            search_attempts += 1
            print(f"[SEARCHING] Attempt {search_attempts}/8 - Flicking...")
            
            for _ in range(15): 
                pyautogui.scroll(-140) 
                time.sleep(0.005) 
            
            time.sleep(0.6) 
            
            if search_attempts >= 8:
                print(">>> Page End. Hunting Right Pink Arrow...")
                if fast_click('pink_arrow.png', 'RIGHT PINK ARROW', region=right_half):
                    print("--- LOADING NEXT PAGE ---")
                    time.sleep(5) 
                    search_attempts = 0 
                else:
                    search_attempts = 0 
                    # Bottom-of-page nudge
                    for _ in range(5):
                        pyautogui.scroll(-100)
                        time.sleep(0.005)

except pyautogui.FailSafeException:
    print("\n[STOPPED] Emergency stop.")
except KeyboardInterrupt:
    print("\n[STOPPED] Manual stop.")
