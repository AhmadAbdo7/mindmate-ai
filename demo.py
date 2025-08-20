### 🐍 demo.py
```python
from transformers import pipeline

# Load Hugging Face sentiment model
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_entry(journal_entry):
    result = sentiment_analyzer(journal_entry)[0]
    label = result['label']
    score = round(result['score'], 2)

    print("\nJournal Entry:", journal_entry)
    print("Detected Sentiment:", label, "(confidence:", score, ")")

    if label == "NEGATIVE":
        print("💡 It looks like you're going through a tough time. Try taking a short break or practicing mindfulness.")
        print("   If these feelings persist, consider reaching out to someone you trust.")
    elif label == "POSITIVE":
        print("😊 You're in a good mood today! Keep up the positive habits.")
    else:
        print("😐 Your mood seems neutral. Maybe reflect on something small that brought you joy today.")

if __name__ == "__main__":
    # Example usage
    entry = input("Write your journal entry: ")
    analyze_entry(entry)
