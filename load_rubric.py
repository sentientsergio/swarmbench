import yaml

def load_benchmark_rubric(file_path):
    """Load the benchmark rubric from a YAML file and return it as a dictionary."""
    try:
        with open(file_path, 'r') as file:
            rubric = yaml.safe_load(file)
        print("Rubric loaded successfully.")
        return rubric
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing the YAML file {file_path}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    rubric_path = './benchmark_rubric.yml'  # Update this path to where your file is located
    rubric_data = load_benchmark_rubric(rubric_path)
    print(rubric_data)  # This will print the loaded rubric data if successful
