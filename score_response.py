# Import necessary library to handle YAML files
from load_rubric import load_benchmark_rubric

def score_response(question_id, user_response, rubric):
    """
    Score a user response based on the specified rubric.

    Args:
        question_id (int): The unique identifier for the question being answered.
        user_response (str): The response provided by the LLM for scoring.
        rubric (dict): The loaded rubric dictionary containing scoring criteria.

    Returns:
        int: The total score calculated for the response based on the rubric.
    """
    # Find the question in the rubric using the question ID
    question_data = next((q for q in rubric['questions'] if q['id'] == question_id), None)
    if not question_data:
        print(f"No question found with ID: {question_id}")
        return None

    # Initialize score to zero
    total_score = 0

    # Evaluate accuracy by comparing user response with the correct answer
    if user_response == question_data['answer']:
        total_score += question_data['scoring']['accuracy']['correct']
    else:
        total_score += question_data['scoring']['accuracy']['incorrect']

    # Return the total score for this response
    return total_score

if __name__ == "__main__":
    # Specify the path to the rubric YAML file
    rubric_path = './benchmark_rubric.yml'
    
    # Load the rubric data from the specified YAML file
    rubric = load_benchmark_rubric(rubric_path)

    # Check if rubric loaded successfully; exit if failed
    if not rubric:
        print("Failed to load the rubric.")
        exit(1)

    # List of test cases with question IDs and responses for scoring
    responses = [
        (1, "56088"),  # Correct answer, should score maximum for accuracy
        (1, "12345"),  # Incorrect answer, should score minimum for accuracy
        (2, "Length: 24 units, Width: 12 units"),  # Correct answer for a different question
    ]

    # Iterate through each test case and score them
    for question_id, response in responses:
        score = score_response(question_id, response, rubric)
        print(f"Question ID {question_id} with response '{response}' scored {score}.")
