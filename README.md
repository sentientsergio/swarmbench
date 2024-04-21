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

### Benchmark Questions

The benchmark includes a set of questions designed to challenge the LLMs across different types of tasks, ensuring a comprehensive evaluation of their capabilities.

#### Math Problems
- **Zero-shot**: "Calculate the product of 123 and 456."
- **Multiple-shot**: "A rectangle's length is twice its width. If the area is 288 square units, what are the dimensions?"

#### Coding Challenges
- **Zero-shot**: "Write a function to check if a string is a palindrome."
- **Multiple-shot**: "Develop a function to merge two sorted lists into one without using built-in sort functions."

#### Word Problems and Puzzles
- **Zero-shot**: "What is the angle between the hour and the minute hands when a clock shows 3:15?"
- **Multiple-shot**: "Measure 45 minutes using two ropes that each take 60 minutes to burn unpredictably."

#### Memory Recall (Needle in Context Haystack)
- **Zero-shot**: "From the narrative about the development of wireless telegraph in March 1887: 'What critical technological breakthrough was reported to have occurred, and who was credited with this achievement?'"
- **Multiple-shot**: "Based on the series of articles on environmental policy development: 'Trace the timeline of key events as described across the articles and explain how public opinion influenced the policy changes.'"

These questions cover a range of difficulties and formats, from straightforward calculations to complex problem-solving scenarios, ensuring that each LLM's performance is rigorously tested under varied conditions.

## How to Use

To use SwarmBench, refer to our setup instructions to configure the benchmark with your chosen LLM configurations, run the tests, and review the results based on our scoring criteria. We encourage users to contribute by suggesting new questions or enhancements to the existing rubric.


