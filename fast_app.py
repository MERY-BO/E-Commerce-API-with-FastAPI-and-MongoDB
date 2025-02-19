from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client['e_commerce_db']

@app.get("/products/")
def get_products():
    products = list(db.products.find({}, {"_id": 0}))
    return {"products": products}

@app.get("/recommendations/{product_id}")
def get_recommendations(product_id: int):
    product = db.products.find_one({"product_id": product_id})
    recommendations = list(db.products.find({"category": product["category"], "product_id": {"$ne": product_id}}, {"_id": 0}))
    return {"recommended_products": recommendations}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
