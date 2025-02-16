def load_audio_file(file_path):
    # Function to load an audio file
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the audio file: {e}")
        return None

def save_settings(settings, file_path):
    # Function to save settings to a file
    try:
        with open(file_path, 'w') as file:
            for key, value in settings.items():
                file.write(f"{key}={value}\n")
    except Exception as e:
        print(f"An error occurred while saving settings: {e}")

def load_settings(file_path):
    # Function to load settings from a file
    settings = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                settings[key] = value
    except FileNotFoundError:
        print(f"Error: The settings file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while loading settings: {e}")
    return settings