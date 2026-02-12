# 🚀 Geometry Dash Auto-Farmer

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Geode](https://img.shields.io/badge/Geode-Supported-pink?style=for-the-badge)
![User](https://img.shields.io/badge/Discord-skiesfr-5865F2?style=for-the-badge&logo=discord&logoColor=white)

A high-performance automation script designed to farm levels in Geometry Dash. Featuring **"Patient Hunter"** logic to handle slow loading times and automatic popup bypassing for various game warnings.

---

## ⚙️ Game Setup (REQUIRED)
To use this script effectively, your game **must** be configured as follows:

1.  **Window Mode:** Geometry Dash must be in **windowed mode** and positioned in the **center** of your screen.
2.  **Mod Loader:** Install **Geode**. [Download Geode here](https://geode-sdk.org/).
3.  **Mod Menu:** Install the **Eclipse Menu** (found within the Geode index).
4.  **Eclipse Settings:**
    * **Auto-Complete Level:** ON
    * **Auto-Claim Coins:** ON
    * **Speedhack:** Set to `50.000`

---

## 🛠️ Script Requirements
- **Python 3.x**
- **Libraries:** `pyautogui`, `opencv-python`, `Pillow`
- **Required Assets:** Ensure the following images are in the same folder as the script:
    * `get_it.png`
    * `play_main.png`
    * `play_popup.png`
    * `pink_arrow.png`

---

## 📦 Installation & Usage
1. Clone this repository or download the files.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
