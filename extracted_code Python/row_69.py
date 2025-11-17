import os
import pickle
from abc import ABC, abstractmethod

class Plugin(ABC):
    """ Abstract base class for all plugins """
    
    @abstractmethod
    def execute(self):
        pass

class SimplePlugin(Plugin):
    """ Example plugin that implements the execute method """
    
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing {self.name} plugin.")

def load_plugin(file_path):
    """ Load a plugin object from a pickle file """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    with open(file_path, 'rb') as f:
        plugin = pickle.load(f)
        
    # Ensure the loaded object is a subclass of Plugin
    if not isinstance(plugin, Plugin):
        raise TypeError("The file does not contain a valid plugin instance.")
    
    return plugin

class PluginLoader:
    """ Manages loading and executing plugins from pickle files """
    
    def __init__(self):
        self.plugins = []
    
    def add_plugin(self, file_path):
        """ Add a plugin object to the loader """
        plugin = load_plugin(file_path)
        self.plugins.append(plugin)
    
    def execute_all(self):
        """ Execute all loaded plugins """
        for plugin in self.plugins:
            plugin.execute()

# Example usage:
if __name__ == "__main__":
    loader = PluginLoader()
    # Add a plugin file path here, replace 'path/to/plugin' with the actual path to your pickle file
    loader.add_plugin('path/to/plugin')
    loader.execute_all()