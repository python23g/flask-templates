from flask import Flask, render_template
from db import featured_posts, recent_posts


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


if __name__ == "__main__":
    app.run(debug=True, port=5001)
