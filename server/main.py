import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Text(BaseModel):
	text: str

@app.post("/summarize")
async def summarize(text: Text):
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum", cache_dir='tokenizer_cache')
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
    tokens = tokenizer(text.text, truncation=True, padding="longest", return_tensors="pt")
    summary = model.generate(**tokens)
    return {"summary": tokenizer.decode(summary[0])}


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
