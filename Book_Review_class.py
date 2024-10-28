from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger
import book_review_module4

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

br = book_review_module4.BookReview()
class AllReview(Resource):
    def get(self):
        """
        This method responds to the GET request for retrieving all book reviews.
        ---
        tags:
        - Book Reviews
        parameters:
            - name: sort
              in: query
              type: string
              required: false
              enum: ["ASC", "DESC"]
              description: Sort reviews by rating in ascending or descending order (optional)
            - name: max_records
              in: query
              type: integer
              required: false
              description: Maximum number of records to retrieve (optional)
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: array
                        items:
                            type: object
                            properties:
                                book_title:
                                    type: string
                                    description: The title of the book
                                book_rating:
                                    type: number
                                    description: The rating of the book
                                book_notes:
                                    type: string
                                    description: The notes of the book
        """
        # Retrieve optional parameters from the query string
        sort = request.args.get('sort',default=None)
        max_records = int(request.args.get('max_records', default=10))

        #Validate the sort parameter
        if sort and sort not in ["ASC", "DESC"]:
            return{"error": "Invalid value for 'sort' parameter"},  400
        # Sort the reviews if sort parameter is provided
        if sort == "ASC":
            book_reviews = br.get_book_ratings(sort=sort, max_records=max_records)
        elif sort == "DESC":
            book_reviews = br.get_book_ratings(sort=sort, max_records=max_records)
        else:
            book_reviews = br.get_book_ratings(max_records=max_records)
        #delete below
        #else:
        #    book_reviews_sorted = book_reviews

        #(not needed handled in previous one) Limit the number of records if max_records parameter is provided
        #if max_records:
        #    book_reviews_sorted = book_reviews_sorted[:int(max_records)]

        return book_reviews, 200

class PostReview(Resource):
    def post(self):
        """
        This method responds to the GET request for retrieving all book reviews.
        ---
        tags:
        - Post Book Reviews
        parameters:
            - in: body
              name: body
              required: true
              schema:
                id: BookReview
                required:
                  - book
                  - rating
                properties:
                  book:
                    type: string
                    description: The title of the book
                  rating:
                    type: integer
                    description: Insert Book rating here (Required)
                  notes:
                    type: string
                    description: Insert notes here (Required)
                    
            # - name: book_title
            #   in: query
            #   type: string
            #   required: true
            #   description: Insert Book Title here (Required)
            # - name: book_rating
            #   in: query
            #   type: integer
            #   required: true
            #   description: Insert Book Rating here, example 1.0 (Required)
            # - name: notes
            #   in: query
            #   type: string
            #   required: false
            #   description: Notes about the book / summary (optional)
        responses:
            200:
                description: A successful POST request
            400: 
                description: Bad request, missing 'Book' or 'Rating' in the request body
        """    
        data = request.json()
        if not data:
          return{"error":"Request body must be in JSON format."}, 400
        
        book = data.get("book")
        rating = data.get("rating")
        notes = data.get("notes","")
        
        if not book or not rating:
          return {"error":"Both 'book' and 'rating' are required fields."}, 400
        
        br.add_book_ratings(book, rating, notes)
        return{"message":"Book Review added successfully."},201
      
# Add the resource to the API
api.add_resource(AllReview, '/all_reviews')
api.add_resource(PostReview, '/post_reviews')

if __name__ == "__main__":
    app.run(debug=True)