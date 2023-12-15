from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)

app.get("/")
def get_trades():
    return "<h1>Хоспаде, оно работает</h1>"
