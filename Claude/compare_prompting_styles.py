import anthropic

# Initialize the client with your API key
client = anthropic.Anthropic(api_key="Your Claude (Anthropic) api key here")

def call_claude_api(prompt):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",  # Replace with the model you want to use
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def compare_prompting_styles_with_claude(case_text):
    # Define the prompts for Claude
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

    # Get responses from Claude API
    zero_response = call_claude_api(zero_shot_prompt)
    one_response = call_claude_api(one_shot_prompt)
    chain_response = call_claude_api(chain_of_thought_prompt)

    return {
        "Zero-Shot Output": zero_response,
        "One-Shot Output": one_response,
        "Chain-of-Thought Output": chain_response
    }

# Example usage
case_text = """Your case here"""
outputs = compare_prompting_styles_with_claude(case_text)

# Print the outputs
print("Zero-Shot:\n", outputs['Zero-Shot Output'])
print("\nOne-Shot:\n", outputs['One-Shot Output'])
print("\nChain-of-Thought:\n", outputs['Chain-of-Thought Output'])

