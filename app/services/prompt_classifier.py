import re
from typing import Literal

class PromptClassifier:
    """
    A class to classify prompts as 'simple' or 'complex' based on predefined criteria.
    """

    def __init__(self):
        # Define thresholds and patterns for classification
        self.length_threshold = 50  
        self.keyword_threshold = 5 
        self.complex_word_pattern = re.compile(r'\b(?:sophisticated|advanced|technical|intricate)\b', re.IGNORECASE)
        self.simple_pattern = re.compile(r'\b(?:what is|solve|explain)\b', re.IGNORECASE)
        self.complex_pattern = re.compile(r'\b(?:make a|plan|design|create)\b', re.IGNORECASE)

    def classify(self, prompt: str) -> Literal['simple', 'complex']:
        """
        Classify the given prompt as 'simple' or 'complex'.

        Args:
            prompt (str): The input prompt to classify.

        Returns:
            Literal['simple', 'complex']: The classification result.
        """
        # Check for simple patterns
        if self.simple_pattern.search(prompt):
            return 'simple'

        # Check for complex patterns
        if self.complex_pattern.search(prompt):
            return 'complex'

        # Check length
        if len(prompt) > self.length_threshold:
            return 'complex'

        # Check for unique keywords
        words = set(re.findall(r'\w+', prompt.lower()))
        if len(words) > self.keyword_threshold:
            return 'complex'

        # Check for complex words
        if self.complex_word_pattern.search(prompt):
            return 'complex'

        return 'complex'

# Example usage
if __name__ == "__main__":
    classifier = PromptClassifier()
    example_prompt = "What is the solution to this problem?"
    print(f"Prompt: {example_prompt}\nClassification: {classifier.classify(example_prompt)}")

    example_prompt = "Make a detailed plan for the project."
    print(f"Prompt: {example_prompt}\nClassification: {classifier.classify(example_prompt)}")
