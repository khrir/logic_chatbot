import os
import json

from dotenv import load_dotenv
load_dotenv()

import vertexai
from vertexai.language_models import TextGenerationModel

def load_sentences(filename: str):
    with open(filename, "r") as f:
        sentences = json.load(f)

    return sentences

def write_model_response(response: [str]):
    with open("public/model_response.json", "a", encoding="utf-8") as f:
        json.dump(response, f, ensure_ascii=False, indent=4, separators=(", ", ": "), default=str)

def sentences_analysis(
    sentences: [str],
    project_id: str,
    location: str,
) -> str:
    """Sentences analysis using a Large Language Model"""
    vertexai.init(project=project_id, location=location)
    parameters = {
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

    model = TextGenerationModel.from_pretrained("text-bison@002")
    response = model.predict(
        f"Sua função é determinar se a inferência lógica é verdadeira: {sentences}",
        **parameters,
    )

    return response.text

if __name__ == "__main__":
    PROJECT_ID = os.getenv('PROJECT_ID')

    data = load_sentences("./public/sentences.json")
    responseArr = []

    for row in data:
        response = sentences_analysis(row['sentences'], PROJECT_ID, "us-central1")
        message = {
            "sentences_id": row['id'],
            "response": response,
        }
        responseArr.append(message)
    
    write_model_response(responseArr)
    print("Done!")