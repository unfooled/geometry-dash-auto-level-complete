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
LEVEL_TIME = 6    
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
        center = pyautogui.center(location)
        pyautogui.click(center)
        
        # ONLY FIX: Double click for main button
        if 'play_main' in image_name:
            time.sleep(0.3)
            pyautogui.click(center)
        
        print(f"[ACTION] Clicked {name}")
        return True
    return False

print("==========================================")
print("   GD FARMER: PATIENT HUNTER EDITION      ")
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
        if find_and_click('get_it.png', 'GET IT'):
            farmed_count += 1
            search_attempts = 0 
            
            # --- NEW: UNLIMITED WAIT FOR GREEN BUTTON ---
            print("[WAITING] Level selected. Waiting for Main Play button to load...")
            while True:
                if find_and_click('play_main.png', 'MAIN ROUND PLAY'):
                    break # Exit this loop and move to popups only when button is clicked
                time.sleep(1) # Check every second so it doesn't lag your PC
            
            # STEP 3: THE POPUP HUNTER
            while True:
                time.sleep(1.2)
                if find_and_click('play_popup.png', 'RECTANGLE POPUP PLAY'):
                    continue 
                else:
                    break 
                    
            # STEP 4: Farming
            print(f"Farming Level #{farmed_count}...")
            time.sleep(LEVEL_TIME)
            
            # STEP 5: ESC-SEQUENCE
            pyautogui.press('esc')   
            time.sleep(1.2)          
            pyautogui.press('esc')   
            print("Back at list.")
            time.sleep(1.5)
        
        else:
            # STEP 6: STRONGER SCROLLING LOGIC
            search_attempts += 1
            print(f"[SEARCHING] Attempt {search_attempts}/5 - Scrolling Hard...")
            
            # Boosted to -40 for maximum strength
            pyautogui.scroll(-76) 
            time.sleep(1.5) 
            
            if search_attempts >= 5:
                print(">>> End of Page. Hunting for RIGHT Pink Arrow...")
                if find_and_click('pink_arrow.png', 'RIGHT PINK ARROW', region=right_half):
                    print("--- LOADING NEXT PAGE ---")
                    time.sleep(5) # Extra time for next page load
                    search_attempts = 0 
                else:
                    search_attempts = 0 
                    pyautogui.scroll(-10)

except pyautogui.FailSafeException:
    print("\n[STOPPED] Emergency stop.")
except KeyboardInterrupt:
    print("\n[STOPPED] Manual stop.")
