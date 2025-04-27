
<img src="https://i.imgur.com/Bzkqs5I.png" alt="drawing" width="100"/>

# FCM 798 - Prompt Engineering - Annotating Labor/Human Trafficking indicators

## Table of Contents
- [Introduction](#Introduction)
  - [LLM Used](#LLM-Used)
  - [Pre Requisites](#Pre-Requisites)
- [Indictors Used](#Indicators-Used)
  - [Human Trafficking Indicators](#Human-Trafficking-Indicators)
- [Prompting Techiniques](#Prompting-Techniques)
- [OpenAI](#OpenAI)
  - [Comparing Prompting Styles](#Comparing-Prompting-Styles)
  - [Steps](#Steps)
- [Claude](#Claude)
  - [Comparing Prompting Styles](#Comparing-Prompting-Styles)
  - [Steps](#Steps)

# Introduction
**Description**: This is my FCM 798 Research Github Repository regarding the topic **Prompt Engineering: Annotating Labor/Human Trafficking indicators in court cases, etc. 

## LLM Used
- [OpenAI](https://platform.openai.com/)
- [Claude](https://www.anthropic.com/api)

## Pre Requisites
**Description**: In order to run the code below in your own system, you must have the following installed.
- Install latest [Python](https://www.python.org/downloads/) version on your system. I use **Python** as my main programming language.
- Install a code editor that you'd like to use. I personally used [Visual Studio Code](https://code.visualstudio.com/download). This will allow you to test out the code I've included in this Repository.
- Since I used [OpenAI](https://platform.openai.com/) and [Claude](https://www.anthropic.com/api), in order to use it's Prompts/API, you will need to have an account on each of the sites, as well as have paid for **Credits** based on how many calls you'd like to make to the API. In short, you'll have to spend money to test out my code.
- After getting credits for each of the LLMs, make sure you create an **API Key** for each. Save this API key somewhere, as we'll be using them to test the code.
- Finally, download the 'FCM_798' folder in this Repository, that contains all necessary files I used. Once downloaded, open the 'FCM_798' folder inside your code editor to begin testing the code.

---

# Indicators Used
**Description**: Below you will find the indicators I used to annotate Human Trafficking cases.

## Human Trafficking Indicators

### Behavioral Indicators
- Rehearsed responses, lack of eye contact, submissive or defensive behavior
- Fear of law enforcement, exhausted or withdrawn demeanor
- Limited knowledge of home, work address, or surroundings
- Restricted freedom, unhealthy attachment to trafficker

### Control Indicators
- Supervised at all times, particularly medical visits
- Recruitment via social networks, escort ads, or chat apps
- Threats of deportation or harm to family
- Lack of personal identification or control over documents
- Prepaid hotel bookings, possession of false IDs, multiple phones

### Physical Indicators
- Excessive work hours, lack of basic necessities
- Visible injuries, untreated medical conditions, distinct tattoos
- Inappropriate dress, lack of personal belongings
- Little control over money or freedom of movement

---

# Prompting Technique

**Description**: Below you will find the prompting techniques that I used to prompt my chosen LLMs (OpenAI & Claude). These terms refer to different ways of structuring prompts when interacting with language models like GPT-4 or Claude. Each method varies in the amount of prior information or examples provided to the model to guide its responses.

## Zero-shot Prompting

**Zero-shot prompting** means asking the model to perform a task without giving it any examples. The model is expected to generate a response based purely on the instructions in the prompt.

- **How it works**: You provide a clear, concise instruction and expect the model to generate the output based on its training, with no examples to guide it.
- **Example**:
    ```
    Prompt: "Translate the following sentence into French: 'I am learning machine learning.'"
    Model: "Je suis en train d'apprendre l'apprentissage automatique."
    ```
- **Use case**: When you want the model to generate an answer or perform a task without needing prior examples. This is often used when the task is clear and the model has learned enough general knowledge.

## One-shot Prompting

**One-shot prompting** involves providing one example to the model to guide its response. This example helps the model understand the format or type of output you're expecting.

- **How it works**: You provide a single example to the model, and it is expected to replicate or generalize from that example when asked to perform the task.
- **Example**:
    ```
    Prompt: 
    "Example: Translate 'I am learning machine learning' to French: 'Je suis en train d'apprendre l'apprentissage automatique.'
    Now, translate 'I am studying artificial intelligence' to French."
    Model: "Je suis en train d'étudier l'intelligence artificielle."
    ```
- **Use case**: When you want to guide the model's output more specifically but don’t want to overwhelm it with too many examples.

## Chain-of-Thought Prompting

**Chain-of-thought prompting** encourages the model to think through its reasoning process step-by-step before generating an answer. This type of prompt is useful for tasks that require multi-step reasoning or when you need the model to show its thought process.

- **How it works**: You prompt the model to work through the problem in a structured, logical manner. The model will generate an intermediate set of thoughts or steps that lead to the final answer.
- **Example**:
    ```
    Prompt:
    "Think step-by-step:
    First, identify the type of translation needed.
    Then, break down the sentence into smaller parts.
    Finally, translate the parts into French.
    
    Translate: 'I am learning machine learning.'"
    Model: "First, identify the sentence subject: 'I'. Then, the verb: 'am learning'. Next, the object: 'machine learning'. The translation is: 'Je suis en train d'apprendre l'apprentissage automatique.'"
    ```
- **Use case**: When you want the model to solve complex problems that require reasoning or explanation. It's also useful for tasks that require more transparency or when you want to ensure that each step is followed logically.

## Summary of Differences

| **Prompt Type**       | **Example**                                                                                     | **When to Use**                                 |
|-----------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------|
| **Zero-shot**          | "Translate 'I am learning machine learning' into French."                                        | Simple tasks where no prior examples are needed. |
| **One-shot**           | "Translate 'I am learning machine learning' into French. Example: 'I am studying AI' -> 'Je suis en train d'étudier l'IA.'" | When you want to provide one example for guidance. |
| **Chain-of-thought**   | "Think step-by-step: First, identify the subject, then the verb, and then the object."           | Tasks requiring reasoning or step-by-step logic. |


---

# OpenAI

## Comparing Prompting Styles
**Description**: In the python file **FCM_798/OpenAI/compare_prompting_styles.py**, you will find a *Python* script that tests the three Prompting Techniques (Zero-Shot, one-shot, and chain-of-thought prompting) I chose. The code defines a function to compare how different prompting styles (Zero-shot, One-shot, and Chain-of-thought) affect the responses from the OpenAI (GPT) API using a chosen **Court case, etc**. It prepares three distinct prompts for GPT and then sends each one to the API. The model’s responses are printed to the console to compare the effectiveness of each prompting technique in extracting the chosen **Indicators**. Follow the steps below to test out the code properly:

### Steps
- Make sure you are in your code Editor in the proper directory (*FCM_798/OpenAI/compare_prompting_styles.py*), and in the proper **terminal** directory.
- Then, make sure you run the following command `pip install openai`. This command installs the OpenAI Python package from the Python Package Index (PyPI). This package provides an easy way to interact with OpenAI's models, including GPT-3, GPT-4, DALL·E, Codex, and others, via API calls.
- Next, locate the `client` variable near the top of the file, and in the string replace it with your ** OpenAI (GPT) api key**
- Next, locate the `case_text` variable near the bottom of the file, and replace the string with the copy of the text (court cases, etc.) that you'd like to analyze based on the Indicators.
- Then, go to your terminal, and enter the command `python compare_prompting_styles.py` to run the Python script.
- Now, analyze the results.

---

# Claude
**Description**: If you'd like to run the code on this Repository on your personal system, follow the steps below.

## Comparing Prompting Styles
**Description**: In the python file **FCM_798/Claude/compare_prompting_styles.py**, you will find a *Python* script that tests the three Prompting Techniques (Zero-Shot, one-shot, and chain-of-thought prompting) I chose. The code defines a function to compare how different prompting styles (Zero-shot, One-shot, and Chain-of-thought) affect the responses from the Claude API using a chosen **Court case, etc**. It prepares three distinct prompts for Claude and then sends each one to the API. The model’s responses are printed to the console to compare the effectiveness of each prompting technique in extracting the chosen **Indicators**. Follow the steps below to test out the code properly:

### Steps
- Make sure you are in your code Editor in the proper directory (*FCM_798/Claude/compare_prompting_styles.py*), and in the proper **terminal** directory.
- Then, make sure you run the following command `pip install anthropic`. This command installs the Anthropic Python package from the Python Package Index (PyPI). This package provides an easy way to interact with Anthropic's Claude language models via API calls.
- Next, locate the `client` variable near the top of the file, and in the string replace it with your ** Claude (Anthropic) api key**
- Next, locate the `case_text` variable near the bottom of the file, and replace the string with the copy of the text (court cases, etc.) that you'd like to analyze based on the Indicators.
- Then, go to your terminal, and enter the command `python compare_prompting_styles.py` to run the Python script.
- Now, analyze the results.
