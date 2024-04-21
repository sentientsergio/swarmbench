import yaml
import os
from openai import OpenAI

def load_client_config(file_path):
    """ Load client configurations from a YAML file. """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        print("Loaded data:", data)  # Debug print to check what's loaded
        return data
    except FileNotFoundError:
        print("Configuration file not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing the YAML file: {e}")
    return None


def create_clients(client_configs):
    """ Create client objects based on the configurations. """
    clients = []
    for config in client_configs.get('clients', []):
        try:
            # Check if API key should be sourced from the environment
            if config['api_key'].startswith('env:'):
                env_var_name = config['api_key'][4:]  # Extract the actual environment variable name
                api_key = os.getenv(env_var_name)
                if not api_key:
                    print(f"Warning: Environment variable '{env_var_name}' for {config['name']} is not set.")
                    continue
                # Create the client using the explicitly fetched environment variable
                client = OpenAI(base_url=config['base_url'], api_key=api_key)
            else:
                # Create the client using the provided API key
                client = OpenAI(base_url=config['base_url'], api_key=config['api_key'])

            clients.append({'client': client, 'model': config['model'], 'name': config['name']})
            print(f"Successfully created client for {config['name']}.")
        
        except Exception as e:
            print(f"Error creating client {config['name']}: {e}")

    return clients


if __name__ == "__main__":
    client_config_path = './test_clients.yml'
    client_configs = load_client_config(client_config_path)
    if client_configs:
        clients = create_clients(client_configs)
        for client in clients:
            print(f"Loaded client {client['name']} with model {client['model']}")
    else:
        print("No client configurations loaded.")

