from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="Your OpenAI (GPT) API Key here")

def compare_prompting_styles(case_text):
    # Define the prompts
    zero_shot_prompt = f"Find human trafficking indicators in the following case:\n\n{case_text}"

    one_shot_prompt = f"""
    Example:\n
    Case: 'The individual showed signs of fear and lacked control over their documents.'\n
    Annotation: Behavioral Indicator (fear), Control Methods (lack of control over documents)

    Now, analyze the following case:\n\n{case_text}
    """

    chain_of_thought_prompt = f"""
    Think step-by-step:
    First, extract key facts from the case.
    Then match them to trafficking indicators (behavioral, control methods, physical).

    Case Text:\n\n{case_text}
    """

    # Zero-shot completion
    zero_response = client.chat.completions.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "user", "content": zero_shot_prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    # One-shot completion
    one_response = client.chat.completions.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "user", "content": one_shot_prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    # Chain-of-thought completion
    chain_response = client.chat.completions.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "user", "content": chain_of_thought_prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    # Extract and return the results
    return {
        "Zero-Shot Output": zero_response.choices[0].message.content.strip(),
        "One-Shot Output": one_response.choices[0].message.content.strip(),
        "Chain-of-Thought Output": chain_response.choices[0].message.content.strip()
    }

# Example usage
case_text = """Input your Case text here"""
outputs = compare_prompting_styles(case_text)
print("Zero-Shot:\n", outputs['Zero-Shot Output'])
print("\nOne-Shot:\n", outputs['One-Shot Output'])
print("\nChain-of-Thought:\n", outputs['Chain-of-Thought Output'])
