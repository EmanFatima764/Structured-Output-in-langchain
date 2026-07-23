# Structured Output in LangChain with Groq

Learn how to generate **reliable, structured responses** from Large Language Models using LangChain's `with_structured_output()` API and the Groq API.

This repository contains simple, beginner-friendly examples showing how to extract structured information from natural language using three different schema definitions:

- **Pydantic**
- **TypedDict**
- **JSON Schema**

Instead of parsing raw text manually, you define the expected structure once, and LangChain returns data that follows that schema.

---

## What You'll Learn

- How `with_structured_output()` works in LangChain
- Creating structured outputs with **Pydantic**
- Using **TypedDict** as a schema
- Using **JSON Schema** for structured responses
- Running LangChain with the **Groq API**

---

## Project Structure

```text
.
├── pydantic.py
├── typedict.py
├── json_schema.py
├── requirements.txt
├── .env.example
└── README.md
```

> File names may vary slightly depending on your implementation.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/structured-output-langchain.git

cd structured-output-langchain
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install langchain langchain-groq python-dotenv pydantic
```

### 3. Configure your API key

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

You can generate an API key from the Groq Console.

---

## Examples

### Pydantic

Define your output using a Pydantic model.

```python
class Review(BaseModel):
    summary: str
    sentiment: Literal["pos", "neg"]
```

Run:

```bash
python pydantic.py
```

---

### TypedDict

Use Python's `TypedDict` to define the response structure.

```bash
python typedict.py
```

---

### JSON Schema

Provide a standard JSON Schema and let the model return matching JSON.

```bash
python json_schema.py
```

---

## Example Output

```python
{
    "key_themes": [
        "Performance",
        "Battery",
        "Camera",
        "S-Pen"
    ],
    "summary": "The Galaxy S24 Ultra delivers excellent performance, camera quality, and battery life, but its price and size may not suit everyone.",
    "sentiment": "pos",
    "pros": [
        "Fast processor",
        "Excellent camera",
        "Long battery life",
        "S-Pen support"
    ],
    "cons": [
        "Heavy",
        "Expensive",
        "Pre-installed apps"
    ],
    "name": "Nitish Singh"
}
```

---

## Tech Stack

- Python
- LangChain
- Groq API
- Pydantic
- python-dotenv

---

## Requirements

- Python 3.10+
- Groq API Key

---

## Resources

- LangChain Documentation: https://python.langchain.com/
- Groq Documentation: https://console.groq.com/docs
- Pydantic Documentation: https://docs.pydantic.dev/

---

## Contributing

Contributions are welcome. If you have ideas for improvements, discover an issue, or want to add more examples, feel free to open a pull request.


