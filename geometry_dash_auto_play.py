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
        pyautogui.click(pyautogui.center(location))
        print(f"[ACTION] Clicked {name}")
        return True
    return False

print("==========================================")
print("   GD FARMER: DIRECT HEALING EDITION     ")
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
            
            # STEP 2: Wait for Main Play button - FIXED GHOST CLICK
            print("[WAITING] Level selected. Waiting for Main Play button...")
            while True:
                location = safe_locate('play_main.png', conf=CONF_LEVEL)
                if location:
                    center = pyautogui.center(location)
                    time.sleep(0.2)
                    pyautogui.moveTo(center.x, center.y, duration=0.3)
                    time.sleep(0.15)
                    pyautogui.click()
                    print(f"[ACTION] Clicked MAIN ROUND PLAY")
                    break
                time.sleep(1)
            
            # STEP 3: THE POPUP HUNTER
            while True:
                time.sleep(1.2)
                if find_and_click('play_popup.png', 'RECTANGLE POPUP PLAY'):
                    continue 
                else:
                    break 
                    
            # STEP 4: FARMING (WAITING FOR THE FINISH ICON)
            print(f"Farming Level #{farmed_count}...")
            while True:
                # 'level_finished.png' is the list icon you sent
                if safe_locate('level_finished.png', conf=0.7):
                    print("[WIN] Level finished detected!")
                    break
                time.sleep(0.5)
            
            # STEP 5: EXIT AND START HEALING
            print("[EXITING] Level done. Doing ESC ESC then healing...")
            pyautogui.press('esc')   
            time.sleep(1.2)          
            pyautogui.press('esc')   
            
            # THE HEALING PROCESS
            while True:
                # CHECK A: Success - Found Purple Arrow -> Go to next search/scroll
                if safe_locate('pink_arrow.png', conf=0.7, region=right_half):
                    print("[SUCCESS] Found Purple Arrow. Proceeding...")
                    break
                
                # CHECK B: Stuck - Found Search Icon -> Click and go to next search/scroll
                elif find_and_click('search_icon.png', 'SEARCH ICON'):
                    print("[FIX] On search page. Clicking to return and starting scroll...")
                    time.sleep(1.5) # Small wait for list to load
                    break
                
                # CHECK C: Still Lost - Press ESC and try again
                else:
                    print("[RETRY] Still lost. Pressing ESC...")
                    pyautogui.press('esc')
                    time.sleep(1.2)
            
            time.sleep(1.5)
        
        else:
            # STEP 6: SCROLLING (8 ATTEMPTS FOR FULL COVERAGE)
            search_attempts += 1
            print(f"[SEARCHING] Attempt {search_attempts}/8 - Flicking Scroll...")
            
            for _ in range(15): 
                pyautogui.scroll(-140) 
                time.sleep(0.005) 
            
            time.sleep(0.6) 
            
            if search_attempts >= 8:
                print(">>> End of Page. Hunting for RIGHT Pink Arrow...")
                if find_and_click('pink_arrow.png', 'RIGHT PINK ARROW', region=right_half):
                    print("--- LOADING NEXT PAGE ---")
                    time.sleep(5) 
                    search_attempts = 0 
                else:
                    search_attempts = 0 
                    for _ in range(5):
                        pyautogui.scroll(-100)
                        time.sleep(0.005)

except pyautogui.FailSafeException:
    print("\n[STOPPED] Emergency stop triggered.")
except KeyboardInterrupt:
    print("\n[STOPPED] Manual stop.")
