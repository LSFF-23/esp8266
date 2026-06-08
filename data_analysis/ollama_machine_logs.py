# step 1: download ollama - https://ollama.com/
# step 2: download phi3:mini model - ollama pull phi3:mini
# step 3: download ollama's lib - pip install ollama

import ollama
import json

def classify_machine_logs():
    print("Starting machine log analysis with SLM at the Edge...")

    machine_logs = [
        "Cycle 345 completed successfully. Parts produced: 50.",
        "EMERGENCY STOP TRIGGERED. Machine stopped. Coolant pressure critically low.",
        "Lubrication system pressure at 50 psi, within normal range.",
        "Temperature above limit. Monitoring advised."
    ]

    for log_message in machine_logs:
        prompt = f"""
You are an industrial automation assistant. Your task is to classify the severity
of the following machine log message.
Use only one of three categories: 'Informative', 'Warning', 'Critical'.
Respond only with a JSON object containing the key "classification".

Example 1:
Log: "Normal operation."
Response: {{"classification": "Informative"}}

Example 2:
Log: "Vibration above limit."
Response: {{"classification": "Warning"}}

Example 3:
Log: "Catastrophic main motor failure."
Response: {{"classification": "Critical"}}

---
Now, classify the following log message:
Log: "{log_message}"
Response:
"""

        try:
            response = ollama.chat(
                model='phi3:mini',
                messages=[{'role': 'user', 'content': prompt}],
                format='json'
            )

            content_str = response['message']['content']
            classification_data = json.loads(content_str)
            classification = classification_data.get("classification", "Not classified")

            print(f"\n[LOG]: '{log_message}'")
            print(f"  -> [SLM Classification]: {classification}")

        except Exception as e:
            print(f"\n[LOG]: '{log_message}'")
            print(f"  -> Error processing log: {e}")

if __name__ == "__main__":
    classify_machine_logs()