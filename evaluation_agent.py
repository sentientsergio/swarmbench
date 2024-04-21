import yaml
from openai import OpenAI
import os
import re

def load_prompt_template(file_path):
    """Load the prompt template from a YAML file."""
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        if data is None:
            print("The YAML file is empty or improperly formatted.")
            return None
        return data['template']
    except FileNotFoundError:
        print("The YAML file was not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing the YAML file: {e}")
        return None


def create_evaluation_prompt(question, user_response, template):
    """Generate a prompt for GPT to evaluate a given response using a template."""
    formatted_prompt = template.format(
        question=question['prompt'],
        answer=question['answer'],
        response=user_response
    )
    return formatted_prompt


def evaluate_response_with_gpt(prompt):
    """Send the constructed prompt to GPT and retrieve the evaluation."""
    try:
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        return response.choices[0].message

    except Exception as e:
        print(f"An error occurred while communicating with OpenAI API: {e}")
        return None
    
if __name__ == "__main__":
    template_path = './evaluation_prompt.yml'
    prompt_template = load_prompt_template(template_path)
    if prompt_template:
        question = {
            'prompt': 'Calculate the product of 123 and 456.',
            'answer': '56088'
        }
        user_response = "56088"  # Example response, should match for testing purposes
        prompt = create_evaluation_prompt(question, user_response, prompt_template)
        evaluation_result = evaluate_response_with_gpt(prompt)
        print(f"Evaluation Result:\n{evaluation_result.content}")
    else:
        print("Failed to load the prompt template.")