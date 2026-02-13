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

# NEW: Heavy-duty click for the Main Button only
def main_button_click(image_name, name):
    location = safe_locate(image_name, CONF_LEVEL)
    if location:
        center_pt = pyautogui.center(location)
        pyautogui.moveTo(center_pt, duration=0.1) # The move that fixed ghost clicks
        pyautogui.click(center_pt)
        print(f"[ACTION] Clicked {name}")
        return True
    return False

# OLD: The fast click from your original script
def fast_click(image_name, name):
    location = safe_locate(image_name, CONF_LEVEL)
    if location:
        pyautogui.click(pyautogui.center(location)) # Straight click, no movement
        print(f"[ACTION] Fast-Clicked {name}")
        return True
    return False

print("==========================================")
print("   GD FARMER: HYBRID LOGIC ACTIVE        ")
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
            
            # STEP 2: MAIN BUTTON (The "Fixed" Hunter Logic)
            print("[WAITING] Hunting Main Play button (Ghost-Proof)...")
            while True:
                if main_button_click('play_main.png', 'MAIN ROUND PLAY'):
                    time.sleep(0.5) 
                    continue 
                else:
                    break 
            
            # STEP 3: POPUP PLAY (Reverted to your Old Script Logic)
            print("[WAITING] Popups (Old Script Speed)...")
            while True:
                # No 1.2s delay, no moveTo. Just the old loop.
                if fast_click('play_popup.png', 'RECTANGLE POPUP PLAY'):
                    continue 
                else:
                    break 
                    
            # STEP 4: FARMING (WAITING FOR ICON)
            print(f"Farming Level #{farmed_count}...")
            while True:
                if safe_locate('level_finished.png', conf=0.7):
                    break
                time.sleep(0.5)
            
            # STEP 5: EXIT + HEALING
            pyautogui.press('esc')   
            time.sleep(1.2)          
            pyautogui.press('esc')   
            
            while True:
                if safe_locate('pink_arrow.png', conf=0.7):
                    break
                elif fast_click('search_icon.png', 'SEARCH ICON'):
                    time.sleep(1.0) 
                    break
                else:
                    pyautogui.press('esc')
                    time.sleep(1.2)
            
            time.sleep(1.0)
        
        else:
            # STEP 6: SCROLLING (Your exact -76 foundation)
            search_attempts += 1
            pyautogui.scroll(-76) 
            time.sleep(1.5) 
            
            if search_attempts >= 5:
                if fast_click('pink_arrow.png', 'RIGHT PINK ARROW'):
                    time.sleep(5) 
                    search_attempts = 0 
                else:
                    search_attempts = 0 
                    pyautogui.scroll(-10)

except pyautogui.FailSafeException:
    print("\n[STOPPED] Emergency stop.")
except KeyboardInterrupt:
    print("\n[STOPPED] Manual stop.")
