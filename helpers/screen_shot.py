from datetime import datetime
import os


def take_screen_shot(driver, prefix=''):
    try:
        current_time = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'Screenshot_{prefix}_{current_time}'
        current_directory = os.getcwd()
        screenshot_folder_path = os.path.join(current_directory, 'screenshots')
        screenshot_file_path = os.path.join(screenshot_folder_path, f'{file_name}.png')
        if not os.path.exists(screenshot_folder_path):
            os.mkdir(screenshot_folder_path)
        driver.save_screenshot(screenshot_file_path)
        return screenshot_file_path
    except Exception as ex:
        print(f'Handled exception in CaptureScreenShot: {ex}')
