"""
Get data. 
"""
from textblob import TextBlob

def main():
    print("starting...")
    with open("complete_doc.txt", encoding='utf-8', newline="") as f:
        lines = f.read()

    blob = TextBlob(lines)

    with open("results.txt", "w") as f:
        # Clean up formatting (doesn't affect analysis)
        blob = blob.replace("\n", " ")
        blob = blob.replace("\t", " ")
        blob = blob.replace("\r", " ")
        blob = blob.replace("  ", " ")

        sentences = blob.sentences
        for sentence in sentences: 
            # Get polarity and subjectivity
            sentiment_polarity = sentence.sentiment.polarity
            sentiment_subjectivity = sentence.sentiment.subjectivity
            
            if "Caltrans Bat Mitigation: A Guide to Developing" in sentence:  # ignore footer
                continue
            
            if sentiment_polarity >= 0.5:  # Switch to <= -0.5 for negative:
                print("Sentiment: POSITIVE")
                # print("Sentiment: NEGATIVE")
                print(f"\n---SENTENCE---\n")
                print(f"{sentence}", end="")
                print(f"Polarity: {sentiment_polarity}")
                print(f"Subjectivity: {sentiment_subjectivity}")
                try:
                    f.write(f"\nRESULT: {sentiment_polarity} {sentiment_subjectivity}\n {sentence}")
                except Exception as e:  # One bad special character 
                    print(f"Error: {e}\n {sentence}")

if __name__ == "__main__":
    main()