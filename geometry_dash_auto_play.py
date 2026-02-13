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
    try:
        img_path = get_path(image_name)
        return pyautogui.locateOnScreen(img_path, confidence=conf, region=region)
    except:
        return None

# HEAVY: For Main Button only to stop ghosting (Move + Click)
def main_button_click(image_name, name):
    location = safe_locate(image_name, CONF_LEVEL)
    if location:
        center_pt = pyautogui.center(location)
        pyautogui.moveTo(center_pt, duration=0.1) 
        pyautogui.click(center_pt)
        print(f"[ACTION] Clicked {name}")
        return True
    return False

# FAST: For Popups (Original snap logic)
def fast_click(image_name, name, region=None):
    location = safe_locate(image_name, CONF_LEVEL, region=region)
    if location:
        pyautogui.click(pyautogui.center(location))
        print(f"[ACTION] Fast-Clicked {name}")
        return True
    return False

print("==========================================")
print("     LOCKED FOUNDATION - NO SKIPPING     ")
print("==========================================")
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
            
            # STEP 2: RESTORED UNLIMITED WAIT (From your original script)
            print("[WAITING] Level selected. Waiting for Main Play button...")
            while True:
                # This loop will NOT break until the button is clicked
                if main_button_click('play_main.png', 'MAIN ROUND PLAY'):
                    break 
                time.sleep(0.5) 
            
            # STEP 3: THE POPUP HUNTER (Old script speed)
            print("[WAITING] Handling popups...")
            while True:
                if fast_click('play_popup.png', 'RECTANGLE POPUP PLAY'):
                    time.sleep(0.2)
                    continue 
                else:
                    break 
                    
            # STEP 4: FARMING (Icon Detection)
            print(f"Farming Level #{farmed_count}...")
            while True:
                if safe_locate('level_finished.png', conf=0.7):
                    break
                time.sleep(0.5)
            
            # STEP 5: ESCAPE AND HEALING
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
            # STEP 6: 8-ATTEMPT FLICK SCROLL
            search_attempts += 1
            print(f"[SEARCHING] Attempt {search_attempts}/8...")
            for _ in range(15): 
                pyautogui.scroll(-140) 
                time.sleep(0.005) 
            
            time.sleep(0.6) 
            
            if search_attempts >= 8:
                if fast_click('pink_arrow.png', 'RIGHT PINK ARROW', region=right_half):
                    time.sleep(5) 
                    search_attempts = 0 
                else:
                    search_attempts = 0 
                    for _ in range(5):
                        pyautogui.scroll(-100)
                        time.sleep(0.005)

except pyautogui.FailSafeException:
    print("\n[STOPPED]")
except KeyboardInterrupt:
    print("\n[STOPPED]")
