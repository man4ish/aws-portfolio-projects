import boto3

def analyze_image(image_path):
    rekognition = boto3.client('rekognition')
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = rekognition.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=10,
        MinConfidence=80
    )

    print("Image Analysis:")
    for label in response['Labels']:
        print(f"Label: {label['Name']}, Confidence: {label['Confidence']}")

def analyze_text(text):
    comprehend = boto3.client('comprehend')

    sentiment_response = comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )
    print(f"\nSentiment: {sentiment_response['Sentiment']}")
    print(f"Sentiment Score: {sentiment_response['SentimentScore']}")

    entities_response = comprehend.detect_entities(
        Text=text,
        LanguageCode='en'
    )
    print("Entities:")
    for entity in entities_response['Entities']:
        print(f"Entity: {entity['Text']}, Type: {entity['Type']}")

def translate_text(text, target_language="es"):
    translate = boto3.client('translate')

    translation_response = translate.translate_text(
        Text=text,
        SourceLanguageCode="en",
        TargetLanguageCode=target_language
    )

    print(f"\nTranslated Text: {translation_response['TranslatedText']}")

if __name__ == "__main__":
    image_path = "your_image.jpg"
    text = "AWS is a leader in cloud computing and artificial intelligence."

    # Image analysis
    analyze_image(image_path)

    # Text analysis
    analyze_text(text)

    # Text translation
    translate_text(text, "fr")  # Translate to French
