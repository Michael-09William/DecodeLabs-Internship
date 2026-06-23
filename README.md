# Automated Copywriting and Tone Transformer

A Python-based CLI application that automates marketing copy generation tailored for multiple platforms (e.g., LinkedIn, Instagram, Email) and brand tones. The system utilizes local Large Language Models (LLMs) via Ollama, enabling full control over dynamic prompt compilation and inference hyperparameters like Temperature and Top-P without external API costs or internet dependencies.

---

## System Architecture & Data Flow

1. **User Input**: The script accepts product details, target platform, desired tone, and inference parameters (`temperature`, `top_p`) directly within the Python environment.
2. **Dynamic Prompt Compilation**: The system injects these user variables into a structured prompt template optimized for copywriting tasks.
3. **Local Inference Execution**: The compiled prompt and hyperparameter configurations are dispatched via the `ollama` Python SDK to the local Ollama instance running the selected LLM (e.g., phi3).
4. **Console Output**: The system processes the response and prints the generated marketing copy directly to the terminal.

---

## Technical Features

* **Inference Parameter Tuning**: Direct control over text generation predictability and creativity by managing `temperature` and `top_p` options.
* **Local and Secure**: Runs entirely on local infrastructure, ensuring data privacy and zero API rate-limiting or subscription dependencies.

---

## Hyperparameter Behavior Analysis

During testing phase development, the following behaviors were documented regarding the `temperature` parameter:

| Temperature Setting | Output Characteristics | Behavioral Result |
| :--- | :--- | :--- |
| **Low (e.g., 0.2)** | Highly deterministic, predictable, and factual. Minimal structural variation. | Recommended for highly standardized emails or strict corporate messaging. |
| **Balanced (e.g., 0.9)** | Optimal structural flow, appropriate usage of platform-specific formatting and hashtags. | Standard operational threshold for professional marketing copy. |
| **High (e.g., 1.5)** | Extreme token randomness, high creativity, potential risk of severe hallucinations. | Can cause context-drift errors (e.g., misinterpreting office furniture as alternative kitchen appliances). |

---

## Installation and Setup

### Prerequisites
* Python 3.10 or higher
* Ollama installed and running locally

### 1. Local Environment Setup
Install the official Ollama Python library within your virtual environment:

```bash
pip install ollama
```
---

### 2. Pull the Required Model
ollama pull phi3

### 3. Run the Application
python main.py
---