from playwright.sync_api import sync_playwright
import os

def capture_screenshot():
    os.makedirs('/home/jules/verification', exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 414, 'height': 896})  # Mobile layout
        page.goto(f"file://{os.path.abspath('index.html')}")
        page.screenshot(path='/home/jules/verification/slides.png', full_page=True)
        browser.close()

if __name__ == '__main__':
    capture_screenshot()
