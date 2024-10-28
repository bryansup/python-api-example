from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class UppercaseText(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        return {"text": text.upper()}, 200

class LowercaseText(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in lowercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to lowercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in lowercase
        """
        text=request.args.get("text")
        lowercaseText = text.lower()
        return  {"text": lowercaseText}, 200

class MixedcaseText(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in lowercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase and lowercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            Mixedtext:
                                type: string
                                description: The text in mixed case
        """
        text=request.args.get("text")
        uppercase=text.upper()
        lowercase=text.lower()
        Mixedtext = uppercase + " " + lowercase
        #Mixedtext = uppercase, lowercase
        print (lowercase)
        print (uppercase)
        return  {"Mixedtext": Mixedtext}, 200

class ProcessText(Resource):
    def get(self):
        """
        This method responds to the GET request for processing text and returns the processed text.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be processed
            - name: duplication_factor
              in: query
              type: integer
              required: false
              description: The number of times to duplicate the text
            - name: capitalization
              in: query
              type: string
              required: false
              enum: [UPPER, lower, Mixed, None]
              description: The capitalization style for the text
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            processed_text:
                                type: string
                                description: The processed text
        """
        text = request.args.get('text')
        duplication_factor = int(request.args.get('duplication_factor', 1))
        capitalization = request.args.get('capitalization', 'None')

        # Validate capitalization input
        if capitalization not in ['UPPER', 'lower','Mixed', 'None']:
            return {"error": "Invalid capitalization value"}, 400

        # Process the text based on duplication_factor and capitalization
        if capitalization == 'UPPER':
            text = text.upper()
        elif capitalization == 'lower':
            text = text.lower()
        elif capitalization == 'Mixed':
            uppertext = text.upper()
            lowertext = text.lower()
            mixed_text = uppertext + " " + lowertext + "//"
            text = mixed_text

        processed_text = (text + " ") * duplication_factor

        return {"processed_text": processed_text}, 200


class BrianCase(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to variation of capitalization
            - name: Capitalization
              in: query
              type: string
              required: true
              enum: [UPPERCASE, lowercase, None]
              description: Option for the capitalization output
            - name: duplication
              in: query
              type: integer
              required: true
              description: Option for the duplication factor output
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        return {"text": text.upper()}, 200

api.add_resource(ProcessText, "/process_text")
api.add_resource(MixedcaseText, "/mixedcase")
api.add_resource(UppercaseText, "/uppercase")
api.add_resource(LowercaseText, "/lowercase")
api.add_resource(BrianCase, "/briancase")

if __name__ == "__main__":
    app.run(debug=True)