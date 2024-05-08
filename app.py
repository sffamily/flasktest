from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# GET /books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET /books/<id>
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404
             
# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201
             
# PUT /books/<id>
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book: 
        book.update(request.get_json())
        return jsonify(book)
    else:    
        return jsonify({"error": "Book not found"}), 404
             
# DELETE /books/<id>
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book: 
        books.remove(book)
        return jsonify({"message": "Book deleted"})
    else:    
        return jsonify({"error": "Book not found"}), 404
             
if __name__ == '__main__':
    app.run(debug=True)