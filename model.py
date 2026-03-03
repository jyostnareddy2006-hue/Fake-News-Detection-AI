def predict_news(text):
    fake_keywords = ["rumor", "fake", "not true", "gossip"]

    for word in fake_keywords:
        if word in text.lower():
            return "Fake News"

    return "Real News"
