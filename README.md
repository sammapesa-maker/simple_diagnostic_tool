# Simple Diagnostic Tool (Forward-Chaining Expert System)

## Overview

This project is a **console-based medical diagnostic assistant** built using **forward-chaining reasoning**, a core concept in **Artificial Intelligence and Expert Systems**.

The system collects patient symptoms, reasons through a structured medical knowledge base, and infers **possible diseases ranked by support score**.

It is designed for **educational purposes**, demonstrating:

* Knowledge representation
* Inference engines
* Forward chaining
* Separation of concerns (UI, logic, knowledge)


## Project Structure

```
diagnostic_tool/
├── ansi.py
├── knowledge_base.py
├── main.py
├── reasoning_engine.py
├── pseudocodes/
│   ├── ansi.txt
│   ├── general.txt
│   ├── knowledge_base.txt
│   ├── main.txt
│   └── reasoning_engine.txt
└── __pycache__/
```

---

## File Descriptions

### 1. `main.py` — Application Entry Point (User Interface)

**Responsibility**

* Manages user interaction
* Collects symptoms
* Displays diagnostic results
* Handles multiple patients per session

**Key Features**

* Converts user input to `snake_case`
* Displays readable output
* Uses ANSI styling for clarity
* Controls program flow

**Concepts Used**

* Input validation
* Presentation layer
* Session control

---

### 2. `reasoning_engine.py` — Inference Engine

**Responsibility**

* Implements **forward-chaining reasoning**
* Translates symptoms into diseases
* Scores diseases based on evidence

**Inference Path**

```
Symptom → Finding → Condition → Disease
```

**Output**

* List of diseases
* Support score
* Supporting symptoms

**Concepts Used**

* Forward chaining
* Rule-based reasoning
* Evidence accumulation

---

### 3. `knowledge_base.py` — Medical Knowledge Base

**Responsibility**

* Stores all domain knowledge
* Contains no executable logic

**Knowledge Layers**

* Symptoms
* Findings
* Conditions
* Diseases

**Role in Expert Systems**

* Represents **facts and rules**
* Can be extended without changing code logic

---

### 4. `ansi.py` — ANSI Text Styling Utility

**Responsibility**

* Formats console output with colors and styles

**Public API**

* `design(text, fg, bg, styles, reset)`

**Purpose**

* Improves readability
* Separates presentation from logic

---

### 5. `pseudocodes/` — Algorithm Documentation

Contains **plain-text pseudocode** versions of each major module.

| File                   | Description                  |
| ---------------------- | ---------------------------- |
| `main.txt`             | UI and session control logic |
| `reasoning_engine.txt` | Forward-chaining inference   |
| `knowledge_base.txt`   | Knowledge structure          |
| `ansi.txt`             | Text styling logic           |
| `general.txt`          | Overall system flow          |

**Use Case**

* Exam revision
* Algorithm explanation
* System design documentation

---

## How the System Works (High-Level)

1. User enters symptoms
2. System maps symptoms to findings
3. Findings map to conditions
4. Conditions map to diseases
5. Diseases are scored
6. Results are ranked and displayed

---

## How to Run

```bash
python3 main.py
```

---

## Educational Focus

This project demonstrates:

* Expert systems architecture
* Knowledge-based AI
* Separation of concerns
* Deterministic reasoning
* Explainable AI output

---

## Limitations

* Not a medical diagnostic tool
* No probabilistic reasoning
* No machine learning
* No persistence or database

---

## Possible Extensions

* Add certainty factors
* Introduce backward chaining
* Replace CLI with GUI or web app
* Store data in a database
* Add patient history tracking

---

## License

Educational / Academic use only.

