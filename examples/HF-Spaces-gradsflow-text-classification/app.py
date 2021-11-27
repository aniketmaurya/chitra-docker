from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

from chitra.serve.app import GradioApp

tokenizer = AutoTokenizer.from_pretrained(
    "finiteautomata/beto-sentiment-analysis")
model = AutoModelForSequenceClassification.from_pretrained(
    "finiteautomata/beto-sentiment-analysis")
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


app = GradioApp(
    "text-classification",
    model=classifier,
)
app.run()
