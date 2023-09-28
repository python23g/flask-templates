from flask import Flask, render_template
from db import featured_posts, recent_posts, get_post


app = Flask(__name__)


@app.route('/')
def home():
    featured = featured_posts()
    recent = recent_posts()

    context = {
        'featured': featured,
        'recent': recent,
    }

    return render_template('home.html', context=context)


@app.route('/blog/<int:pk>')
def blog(pk: int):
    post = get_post(pk)

    return render_template('blog.html', post=post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
