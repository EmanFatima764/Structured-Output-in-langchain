
# ChatGroq is used to connect LangChain with Groq LLMs.
from langchain_groq import ChatGroq

# Loads environment variables from the .env file.
from dotenv import load_dotenv

# Used to define the structure of the output.
from typing import TypedDict, Annotated, Literal

# Used to access environment variables like the API key.
import os


# Load Environment Variables

# Reads variables from the .env file.
load_dotenv()


# Initialize the Groq Model

# Create an LLM object.

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
# Define the Output Schema

# TypedDict tells the LLM what the output dictionary should look like.
class Review(TypedDict):

    # List all product features mentioned in the review.
    features: Annotated[
        list[str],
        "List the product features mentioned in the review."
    ]

    # Short summary of the review.
    summary: Annotated[
        str,
        "A brief summary of the review."
    ]

    # The sentiment must be one of these values only.
    sentiment: Annotated[
        Literal["positive", "negative", "neutral"],
        "Return the review sentiment."
    ]

    # List all positive points.
    pros: Annotated[
        list[str],
        "List the pros mentioned in the review."
    ]

    # List all negative points.
    cons: Annotated[
        list[str],
        "List the cons mentioned in the review."
    ]

    # Name of the reviewer.
    name: Annotated[
        str,
        "Return the reviewer's name if mentioned. Otherwise return an empty string."
    ]

# This tells the LLM to always return output
# matching the Review schema.
structured_model = model.with_structured_output(Review)

review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!

The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos.

The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often.

What really blew me away is the 200MP camera. The night mode is stunning, capturing crisp, vibrant images even in low light.

Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use.

Samsung’s One UI still comes with unnecessary bloatware.

The $1300 price tag is also very expensive.

Pros:
- Powerful Snapdragon 8 Gen 3 processor
- Amazing 200MP camera
- Long battery life
- 45W fast charging
- Useful S-Pen

Cons:
- Heavy phone
- Too much bloatware
- Expensive price

Review by Eman Fatima
"""
# Send the Review to the LLM
# The model extracts structured information according to the Review schema.
result = structured_model.invoke(review)

# Print the complete dictionary.
print(result)

# Print each field individually.
print("Reviewer :", result["name"])
print("Summary  :", result["summary"])
print("Sentiment:", result["sentiment"])
print("Features :", result["features"])
print("Pros     :", result["pros"])
print("Cons     :", result["cons"])