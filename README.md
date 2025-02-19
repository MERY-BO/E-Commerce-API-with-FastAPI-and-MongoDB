# E-Commerce API with FastAPI and MongoDB

## Overview

This project sets up an API for an e-commerce platform using FastAPI and MongoDB. It provides endpoints to retrieve products and get product recommendations based on category.

## Features

- **Retrieve Products**: Fetch all available products from the database.
- **Product Recommendations**: Suggest similar products based on the same category.

## Database Structure

The application uses a MongoDB database with the following collection:

- **Products**: Contains product details such as name, category, price, and stock.

## API Endpoints

### 1. Get All Products

- **Endpoint**: `GET /products/`
- **Description**: Retrieves a list of all available products.

### 2. Get Product Recommendations

- **Endpoint**: `GET /recommendations/{product_id}`
- **Description**: Provides recommendations based on a given product's category.
- **Parameters**:
  - `product_id` (integer): The ID of the product for which recommendations are needed.
- **Response**: Returns a list of recommended products within the same category.

## Requirements

To run this project, you need:

- Python installed on your system.
- MongoDB running locally or remotely.
- The following Python libraries:
  - `fastapi`
  - `uvicorn`
  - `pymongo`

## Setup Instructions

1. **Install Dependencies**

   ```sh
   pip install fastapi uvicorn pymongo
   ```

2. **Ensure MongoDB is Running**

   - If running locally, start MongoDB using:
     ```sh
     mongod --dbpath /path/to/your/data
     ```
   - If using a remote MongoDB instance, update the connection string accordingly.

3. **Run the FastAPI Server**

   ```sh
   uvicorn main:app --reload
   ```

## Future Enhancements

- Add user authentication and authorization.
- Implement advanced product recommendations using machine learning.
- Expand the API with endpoints for order management and customer reviews.



