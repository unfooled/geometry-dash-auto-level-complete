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
        # Standard click from your working foundation
        pyautogui.click(pyautogui.center(location))
        print(f"[ACTION] Clicked {name}")
        return True
    return False

print("==========================================")
print("   GD FARMER: PERFECT HUNTER EDITION     ")
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
            
            # STEP 2: THE MAIN PLAY HUNTER (Now using your "Perfect" Popup logic)
            print("[WAITING] Level selected. Hunting for Main Play button...")
            while True:
                time.sleep(1.0) 
                if find_and_click('play_main.png', 'MAIN ROUND PLAY'):
                    # If it clicks but the button is still there, it clicks again
                    continue 
                else:
                    # Only moves on when the button is GONE
                    break 
            
            # STEP 3: THE POPUP HUNTER (Kept exactly as you liked it)
            while True:
                time.sleep(1.2)
                if find_and_click('play_popup.png', 'RECTANGLE POPUP PLAY'):
                    continue 
                else:
                    break 
                    
            # STEP 4: FARMING (WAITING FOR THE ICON)
            print(f"Farming Level #{farmed_count}...")
            while True:
                # This waits for the list icon you sent
                if safe_locate('level_finished.png', conf=0.7):
                    print("[WIN] Level finished icon detected!")
                    break
                time.sleep(0.5)
            
            # STEP 5: ESC-SEQUENCE + HEALING
            print("[EXITING] Doing ESC ESC then starting healing...")
            pyautogui.press('esc')   
            time.sleep(1.2)          
            pyautogui.press('esc')   
            
            # THE HEALING PROCESS
            while True:
                # CHECK A: Found Purple Arrow -> Break and start scrolling
                if safe_locate('pink_arrow.png', conf=0.7):
                    print("[SUCCESS] Found Purple Arrow. Proceeding to scroll...")
                    break
                
                # CHECK B: Found Search Icon -> Click it and then start scrolling
                elif find_and_click('search_icon.png', 'SEARCH ICON'):
                    print("[FIX] On search page. Returning to list and starting scroll...")
                    time.sleep(1.5) 
                    break
                
                # CHECK C: Still Lost -> Press ESC and try again
                else:
                    print("[RETRY] Still lost. Pressing ESC...")
                    pyautogui.press('esc')
                    time.sleep(1.2)
            
            time.sleep(1.0)
        
        else:
            # STEP 6: SCROLLING LOGIC (From your "worked" block)
            search_attempts += 1
            print(f"[SEARCHING] Attempt {search_attempts}/5 - Scrolling Hard...")
            
            pyautogui.scroll(-76) 
            time.sleep(1.5) 
            
            if search_attempts >= 5:
                print(">>> End of Page. Hunting for RIGHT Pink Arrow...")
                if find_and_click('pink_arrow.png', 'RIGHT PINK ARROW', region=right_half):
                    print("--- LOADING NEXT PAGE ---")
                    time.sleep(5) 
                    search_attempts = 0 
                else:
                    search_attempts = 0 
                    pyautogui.scroll(-10)

except pyautogui.FailSafeException:
    print("\n[STOPPED] Emergency stop.")
except KeyboardInterrupt:
    print("\n[STOPPED] Manual stop.")
