import yaml

# Example of unsafe YAML loading
def unsafe_yaml_load(filepath):
    with open(filepath, 'r') as file:
        # Unsafe loading of YAML content
        data = yaml.load(file)
        return data

if __name__ == "__main__":
    filepath = 'example.yaml'  # Ensure you have a YAML file named 'example.yaml' in the same directory
    content = unsafe_yaml_load(filepath)
    print("Loaded data:", content)
