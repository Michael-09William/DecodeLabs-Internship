# Stateful Local Chatbot

A Python-based conversational assistant that maintains interaction history locally. The system utilizes Microsoft's Phi-3 LLM via Ollama for text generation, implementing structured validation gates and context window management to handle multi-turn dialogues efficiently without external API dependencies.

---

## Architecture Overview

The system operates entirely on the local infrastructure through the following pipeline:
1. **Structural Validation Gate:** Validates user inputs against empty strings or session termination commands (`EXIT`).
2. **Context Memory Pipeline:** Ingests user and assistant messages into a stateful matrix utilizing standard role-content schema.
3. **Local Inference Execution:** Routes the payload to the local Ollama instance hosting the `phi3` model configuration.
4. **Context Window Management:** Prunes historical logs dynamically once threshold limits are reached to maintain inference speed and prevent context length degradation.

---

## System Requirements

### Operational Environment
* **Operating System:** Windows 10/11, macOS, or Linux
* **Python Runtime:** Python 3.10 or higher
* **Local LLM Engine:** Ollama Link Runtime

### Hardware Recommendations
* **RAM:** Minimum 8 GB (16 GB recommended for low-latency token generation)
* **Storage:** At least 3 GB of available disk space for the Phi-3 model weight parameters.

---

## Installation and Environment Setup

### 1. Initialize the Core Inference Engine
Download and install the Ollama runtime platform executable compatible with your operating system from the official portal. Ensure the daemon process is running in your background environment.

### 2. Pull the Targeted Model Weights
Open your command-line interface and execute the following command to download the quantized weights for the Microsoft Phi-3 model:

```bash
ollama run phi3

