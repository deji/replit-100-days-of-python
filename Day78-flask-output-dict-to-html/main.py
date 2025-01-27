import re

from flask import Flask, render_template_string

app = Flask(__name__)

# Sample dictionary with page numbers as keys
pages = {
    "2":
    "<h1>About Us</h1><p>This page contains information about us.</p>",
    "3":
    "<h1>Contact</h1><p>Reach us at contact@example.com.</p>",
    "78":
    "<h1>Flask challenge</h1><p>Wow! It has being a long time I worked with HTML/CSS and this was quite refreshing</p>",
}

# Basic CSS for styling
css_style = """
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; padding: 20px; background-color: #f4f4f4; }
        .container { max-width: 600px; background: white; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        p { font-size: 16px; color: #666; }
    </style>
"""

show_page_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Page {{ page_number }}</title>
        {{ css_style | safe  }}
    </head>
    <body>
        <div class='container'>
            {{ content | safe }}
            <p>&nbsp;</p>
            <p><a href="/">List page</a></p>
        </div>
    </body>
    </html>
"""

list_page_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>List Page</title>
        {{ css_style | safe  }}
    </head>
    <body>
        <div class='container'>
            {{ content | safe }}
        </div>
    </body>
    </html>
"""


@app.route("/")
def list_page():
    content = "<h1>List Page</h1>"
    for page, page_content in pages.items():
        page_title = re.search(r'<h1>(.*?)</h1>', page_content).group(1)
        content += f"\n<p><a href='/{page}'>Page {page}</a>: {page_title}</p>"
    return render_template_string(list_page_template,
                                  css_style=css_style,
                                  content=content)


@app.route("/<page_number>")
def show_page(page_number):
    return_code = 200 if page_number in pages else 404
    content = pages.get(page_number,
                        "<h1>404 Not Found</h1><p>Page does not exist.</p>")
    return render_template_string(show_page_template,
                                  page_number=page_number,
                                  css_style=css_style,
                                  content=content), return_code


if __name__ == "__main__":
    app.run()
