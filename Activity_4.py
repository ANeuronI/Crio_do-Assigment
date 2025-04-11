import json
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
Open_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=Open_api_key)

# Example unstructured text from a research paper
content = """
Application of Quantum Algorithms in Interstellar Navigation: A New Frontier" is a research paper authored by Dr. Stella Voyager, Dr. Nova Star, and Dr. Lyra Hunter.
The paper explores how quantum algorithms can revolutionize interstellar navigation systems. By leveraging quantum superposition and entanglement, the proposed system calculates optimal travel paths through space-time anomalies with greater efficiency than traditional methods.
Simulation experiments demonstrated that the quantum-based navigation approach significantly reduces both travel time and fuel consumption during interstellar missions.
Key concepts covered include quantum algorithms, interstellar navigation, space-time anomalies, quantum superposition, quantum entanglement, and space travel. """


response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "system", "content": "You are an expert at structured data extraction. You will be given unstructured text from a research paper and should convert it into the given structure."},
        {"role": "user", "content": content}
    ],
    text={
        "format": {
              "type": "json_schema",
              "name": "research_paper_extraction",
              "schema": {
                "type": "object",
                "properties": {
                    "title": { "type": "string" },
                    "authors": { 
                        "type": "array",
                        "items": { "type": "string" }
                    },
                    "abstract": { "type": "string" },
                    "keywords": { 
                        "type": "array", 
                        "items": { "type": "string" }
                    }
                },
                "required": ["title", "authors", "abstract", "keywords"],
                "additionalProperties": False
            },
            "strict": True
        },
    },
)

research_paper = json.loads(response.output_text)

