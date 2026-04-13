import os
import sys
import subprocess
import platform

class UltimateJarvisSetup:
    def __init__(self):
        self.requirements_file = 'requirements.txt'
        self.config_file = 'config.json'
        self.setup_configurations()  

    def setup_configurations(self):
        # Check for existing configuration
        if not os.path.exists(self.config_file):
            print("Setting up initial configuration...")
            self.create_initial_config()
            print("Initial configuration created.")
        else:
            print("Configuration file already exists. Proceeding to install dependencies...")
        self.install_requirements()

    def create_initial_config(self):
        initial_config = {
            "api_key": "",  # Add your API key here
            "setting_1": "value1",
            "setting_2": "value2"
        }
        with open(self.config_file, 'w') as config_file:
            json.dump(initial_config, config_file, indent=4)

    def install_requirements(self):
        if os.path.exists(self.requirements_file):
            print("Installing dependencies...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', self.requirements_file])
            print("Dependencies installed.")
        else:
            print("Requirements file not found.")

    def run_setup(self):
        print("Ultimate Jarvis AI Companion setup complete!")

if __name__ == '__main__':
    setup = UltimateJarvisSetup()
    setup.run_setup()