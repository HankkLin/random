# LLM Patient Guessing Game

This repository contains a simple project idea that uses a free online Large Language Model (LLM) to role-play as a patient. The goal is for the user to interact with the LLM, ask questions about symptoms, and try to determine what illness the patient has.

## How It Works
1. The LLM is prompted to act as a patient experiencing certain symptoms.
2. The user asks the patient questions to gather information.
3. Based on the answers, the user attempts to guess the sickness.

This project is for experimentation and entertainment only. It is **not** a source of medical advice.

## Getting Started
Because this repository does not include code, you can simply experiment by using your favorite free LLM service. Provide the LLM with a prompt similar to:

```
You are a patient experiencing a set of symptoms. Do not reveal your illness directly. Answer my questions as truthfully as possible based on the symptoms.
```

Then, begin asking questions to determine the illness.

## Windows Setup

This repository includes a small Python script, `patient_game.py`, that
demonstrates how you might interact with a free online LLM. The script requires
Python 3 and the `requests` package.

1. Install [Python](https://www.python.org/downloads/) if you do not already
   have it.
2. Install dependencies from `requirements.txt`:
   ```cmd
   pip install -r requirements.txt
   ```
3. Obtain a Hugging Face API token and set it in your environment:
   ```cmd
   set HF_API_TOKEN=your_token_here
   ```
4. Run the game:
   ```cmd
   python patient_game.py
   ```

The script will prompt you to ask the patient questions. Type `quit` to exit.

## License
This project is released under the MIT License. See [LICENSE](LICENSE) for details.
