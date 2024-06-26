# SwarmBench: Multi-Agent LLM Benchmarking

Welcome to the SwarmBench repository, an innovative benchmarking tool developed by students of The Multiverse School. Our tool is designed to evaluate the performance of Large Language Models (LLMs) through a unique multi-agent approach, emphasizing the benefits of agent specialization and orchestration.

## Project Overview

SwarmBench aims to push the boundaries of conventional LLM benchmarking by introducing a swarm of specialized agents, each contributing uniquely to solve complex problems more efficiently than single-agent solutions. This project is inspired by our cohort's fascination with the concept of "Swarms" in agent-based systems, reflecting the collective intelligence and enhanced capabilities that emerge from such collaborations.

## Features

- **Multi-Agent Testing**: Leverage multiple LLMs to tackle diverse tasks simultaneously, showcasing the power of collaborative intelligence.
- **Standardized API Calls**: Compatible with OpenAI's API standards, allowing seamless integration with various LLMs including custom implementations in local environments.
- **Flexible Configuration**: Configure tests and parameters easily through YAML files, supporting extensive customization to suit different testing needs.
- **Performance Metrics**: Comprehensive metrics for accuracy, relevance, and coherence, with support for detailed analytics and performance comparisons.
- **Open Source**: As a community-driven project, we encourage contributions and enhancements from fellow AI enthusiasts and researchers.

## Getting Started

To get started with SwarmBench, clone this repository and follow the setup instructions in our documentation. Ensure you have the necessary dependencies installed, and refer to our example configurations to set up your first benchmark tests.

```bash
git clone https://github.com/MultiverseSchool/SwarmBench.git
cd SwarmBench
# Follow installation and setup instructions in documentation
```

## Benchmark Rubric and Questions

SwarmBench utilizes a detailed rubric designed to evaluate the performance of LLMs based on three key metrics: Accuracy, Relevance, and Coherence. Below is an overview of the scoring criteria and the specific benchmark questions that test each LLM's capabilities across various domains.

### Scoring Criteria

- **Accuracy**

  - `0` - Incorrect: The response does not provide correct information or solution.
  - `1` - Partially Correct: The response is on the right track but may be incomplete or imprecise.
  - `2` - Fully Correct: The response is completely accurate and addresses the prompt fully.

- **Relevance**

  - `0` - Irrelevant: The response fails to address the question or topic.
  - `1` - Somewhat Relevant: The response partially addresses the question but includes extraneous information.
  - `2` - Fully Relevant: The response directly addresses and comprehensively covers the question's requirements.

- **Coherence**
  - `0` - Low Coherence: The response has significant grammatical or logical errors making it difficult to understand.
  - `1` - Moderate Coherence: The response has minor issues but is generally understandable.
  - `2` - High Coherence: The response is well-structured, clear, and logically presented.

## Benchmark Rubric Configuration (`benchmark_rubric.yml`)

### Overview

The `benchmark_rubric.yml` file is an essential component of the **SwarmBench** project. It centralizes all the questions, correct answers, and detailed scoring criteria used in benchmarking Large Language Models (LLMs). By structuring this information in a YAML file, the benchmark can be easily updated and maintained without changing the core application code, facilitating straightforward modifications and extensions to the testing framework.

### File Structure

The `benchmark_rubric.yml` contains a structured list of benchmark questions. Each question is defined with several key elements:

- **ID**: A unique identifier for each question.
- **Category**: Specifies the category of the question, such as Math Problems, Coding Challenges, Word Problems and Puzzles, or Text Comprehension.
- **Prompt**: Includes the question text or scenario presented to the LLM. For certain categories like Text Comprehension, this includes both the background text and the specific question asked.
- **Answer**: Defines the correct or expected answer, which is crucial for evaluating the LLM’s accuracy.
- **Scoring**: Outlines the criteria for scoring responses based on:
  - **Accuracy**: Scores range from 0 (incorrect) to 2 (fully correct), assessing how accurately the response matches the expected answer.
  - **Relevance**: Evaluates whether the response appropriately addresses the prompt, with scores ranging from 0 (irrelevant) to 2 (fully relevant).
  - **Coherence**: Measures the logical and grammatical structure of the response, also on a scale from 0 (incoherent) to 2 (highly coherent).

### Usage

This file is loaded into the **SwarmBench** system at runtime, where it serves as the foundation for evaluating LLM responses. The scoring system interprets the criteria specified in the file to assign quantitative scores to each response, enabling an objective and consistent assessment of LLM capabilities.

### Modifications

To update or extend the benchmark tests, contributors can edit this YAML file, adding new questions or modifying existing ones. Changes in this file will be reflected in the benchmark tests without requiring adjustments to the application's operational code.

## Evaluation Prompt Configuration (`evaluation_prompt.yml`)

### Overview

The `evaluation_prompt.yml` file contains the template used for generating prompts that are sent to various language models for evaluation. This template ensures consistency in how questions are asked across different tests and models, helping to standardize the evaluation process.

### Configuration

This YAML file should define a template that includes placeholders for dynamic content such as the question, correct answer, and user response. The structure allows for easy adjustments to the prompt without altering the codebase.

**Example Structure:**

```yaml
template: |
  Evaluate the following response based on the provided scoring criteria:

  Question: {question}
  Correct Answer: {answer}
  Response: {response}
  Scoring Criteria:
    - Accuracy:
      - 2: The response is completely accurate and matches the correct answer exactly.
      - 1: The response is partially correct but may include some inaccuracies or omissions.
      - 0: The response is incorrect or completely irrelevant to the correct answer.
    - Relevance:
      - 2: The response directly addresses and fully covers the question's requirements.
      - 1: The response addresses the question but includes irrelevant information or is incomplete.
      - 0: The response does not address the question at all or is entirely off-topic.
    - Coherence:
      - 2: The response is well-structured, clear, and logically presented.
      - 1: The response has minor structural or logical issues but is generally understandable.
      - 0: The response is poorly structured, hard to understand, or logically inconsistent.
```

## Client Configuration (`test_clients.yml`)

### Overview

The `test_clients.yml` file is used to manage configurations for different clients that interact with language models. This includes API keys, base URLs, and model identifiers, facilitating easy management and switching between different models or APIs for testing.

### Configuration

Define each client with necessary details such as name, API base URL, API key, and the specific model to be used. This allows the system to dynamically create clients based on these configurations, supporting a flexible and scalable testing environment.

```yaml
clients:
  - name: OpenAI-gpt4
    base_url: "https://api.openai.com/v1"
    api_key: "env:OPENAI_API_KEY"
    model: "gpt-4"
  - name: Local-Llama-3-70B
    base_url: "http://localhost:1234/v1"
    api_key: "lm-studio"
    model: "lmstudio-community/Meta-Llama-3-70B-Instruct-GGUF/Meta-Llama-3-70B-Instruct-Q4_K_M.gguf"
```

## How to Use

To use SwarmBench, refer to our setup instructions to configure the benchmark with your chosen LLM configurations, run the tests, and review the results based on our scoring criteria. We encourage users to contribute by suggesting new questions or enhancements to the existing rubric.
