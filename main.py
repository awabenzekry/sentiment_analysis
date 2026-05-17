from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv(override=True)

def analyze_sentiment(review: str) -> str:
    """Analyse le sentiment d'un avis Amazon."""
    model = ChatOpenAI(model="gpt-4o", temperature=0)

    system_message = """
    Classify the sentiment of Amazon product reviews presented in the input as 'positive' or 'negative'.
    Amazon reviews will be delimited by triple backticks in the input.
    Answer only 'positive' or 'negative'.
    Do not explain your answer.
    """

    response = model.invoke([
        SystemMessage(system_message),
        HumanMessage(f"```{review}```")
    ])
    return response.content.strip()


if __name__ == "__main__":
    test_reviews = [
        "This product is absolutely amazing! Works perfectly and arrived on time.",
        "Complete waste of money. Broke after 2 days. Very disappointed.",
        "Exactly as described, fast shipping, will buy again!"
    ]

    for review in test_reviews:
        sentiment = analyze_sentiment(review)
        print(f"Review : {review[:60]}...")
        print(f"Sentiment : {sentiment}\n")
