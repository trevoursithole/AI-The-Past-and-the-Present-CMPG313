# AI Evolution Lab
### Rule-Based (ELIZA) vs. Modern LLM (Qwen)
**Module:** Artificial Intelligence (CMPG 313) — Lab 3

---

## Overview

This project is a comparative study between two eras of AI. It pairs a legacy **ELIZA** chatbot , operating on hardcoded pattern matchingagainst a modern **Large Language Model** (Qwen2.5-1.5B-Instruct), which uses probabilistic text generation and instruction-tuning.

The goal was to observe how AI has evolved from simple keyword-triggered mirroring to deep contextual understanding and task-oriented instruction following.

---

## Components

### 1. The Past  `eliza.py`
ELIZA simulates a Rogerian psychotherapist. It does not "understand" the user; instead, it uses regular expressions to decompose input and reassemble it into a reflective question.

**Custom rules implemented (5+):**

| Topic | Trigger | Behaviour |
|---|---|---|
| Exam Stress | Academic pressure keywords | Targeted empathetic responses |
| Names | Name-related input | Personalised greetings via variable extraction |
| Health | "tired", "sleep" | Specific health-related prompts |
| Family | "strict", "parents" | Contextual family handling |
| Future / Worry | Anxiety-related input | Empathetic response templates |

---

### 2. The Present  `LLM.py`
Powered by the Hugging Face `transformers` library with an instruction-tuned model.

- **Model:** `Qwen/Qwen2.5-1.5B-Instruct`
- **Capability:** Follows complex instructions, generates structured advice (e.g. bulleted sleep hygiene tips), and maintains a consistent assistant persona across a conversation.

---

### 3. Comparison Interface  `chat_comparison.py`
A custom **Tkinter GUI** for real-time, side-by-side testing. Enter a single prompt and immediately see how a rule-based system and an LLM handle the same input.

---

## Key Observations

| Prompt | ELIZA (Rule-Based) | Qwen (Instruction-Tuned) |
|---|---|---|
| *"I feel stressed"* | Mirroring: *"Please tell me more."* | Provides physical and mental relaxation strategies |
| *"I need sleep"* | *"Why do you need sleep?"* | Explains sleep hygiene and regular schedules |
| *"I have exams"* | Asks about exam preparation | Offers study tips and time management advice |

---

## Setup

**1. Install dependencies**
```bash
pip install nltk transformers torch
```

**2. Run the comparison tool**
```bash
python chat_comparison.py
```

**3. Run scripts individually**
```bash
python eliza.py       # Terminal-based legacy ELIZA
python LLM.py         # Standalone modern LLM
```

---

## Repository Structure

```
├── eliza.py              # Rule-based chatbot
├── LLM.py                # Modern LLM implementation (Qwen)
├── chat_comparison.py    # GUI comparison application
├── README.md             # Documentation and analysis
└── screenshots/          # Visual evidence of model outputs
```

---

## Conclusion

This lab made clear that while ELIZA is fast and lightweight, its lack of semantic understanding makes it brittle and easily confused by novel inputs. Modern LLMs, by contrast, demonstrate a high degree of reasoning and instruction following  a significant leap in AI's capacity to assist users in genuinely meaningful ways.
