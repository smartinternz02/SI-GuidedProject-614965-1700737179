from flask import Flask, render_template, request
from text_summarization import get_summary  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        text_input = request.form.get('text_input')
        if url:
            summary = get_summary(url)
        elif text_input:
            summary = get_summary(text_input)
        else:
            summary = None
        return render_template('index.html', summary=summary)
    return render_template('index.html', summary=None)

if __name__ == '__main__':
    app.run(debug=True)
