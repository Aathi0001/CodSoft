from flask import Flask, Response, render_template, request, redirect, url_for
import sqlite3
import math

app = Flask(__name__)

def get_db_connection():
    # Establish a connection to your SQLite database
    return sqlite3.connect('tech_reviews.db')

# Define the number of images per page
images_per_page = 24  # Adjust as needed

@app.route('/image/<int:image_id>')
def get_image(image_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT image FROM TechReviews WHERE id = ?", (image_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        image_data = result[0]
        response = Response(image_data, content_type='image/jpeg')
        return response
    else:
        return "Image not found", 404
    
@app.route("/")
def work():
    page = int(request.args.get('page', 1))

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM TechReviews")
    total_images = cursor.fetchone()[0]

    total_pages = math.ceil(total_images / images_per_page)

    start_index = (page - 1) * images_per_page
    cursor.execute("SELECT id FROM TechReviews ORDER BY id DESC LIMIT ? OFFSET ?", (images_per_page, start_index))
    image_ids = [row[0] for row in cursor.fetchall()]

    places = []
    for image_id in image_ids:
        cursor.execute("SELECT name, description FROM TechReviews WHERE id = ?", (image_id,))
        result = cursor.fetchone()
        if result:
            name, description = result
            places.append({'id': image_id, 'name': name, 'des': description})

    cursor.close()
    connection.close()

    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None

    page_nums = range(1, total_pages + 1)

    return render_template("home.html", places=places, prev_page=prev_page, next_page=next_page, page_nums=page_nums)

@app.route('/submit_message', methods=['POST'])
def submit_message():
    if request.method == 'POST':
        message = request.form['message']

        if message:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO messages (message) VALUES (?)", (message,))

            connection.commit()
            cursor.close()
            connection.close()

        return redirect(url_for('work'))

    return render_template('home.html')

@app.route("/show_place/<int:place_id>", methods=['GET', 'POST'])
def show_place(place_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        comment_text = request.form.get('comment_text')
        if comment_text:
            cursor.execute("INSERT INTO Comment (text, place_id) VALUES (?, ?)", (comment_text, place_id))
            connection.commit()

    cursor.execute("SELECT name, description FROM TechReviews WHERE id = ?", (place_id,))
    result = cursor.fetchone()

    if result:
        name, description = result
    else:
        cursor.close()
        connection.close()
        return "Error: Place not found", 404

    cursor.execute("SELECT text FROM Comment WHERE place_id = ?", (place_id,))
    comments = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    place = {'id': place_id, 'name': name, 'des': description}

    return render_template("show_place.html", place=place, comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
