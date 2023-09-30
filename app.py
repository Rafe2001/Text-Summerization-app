from flask import Flask, render_template, request, jsonify
from summary import summarize
import os

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        raw_text = request.form['text']
        final_summary, doc, summary_word_count, raw_word_count = summarize(raw_text)
    #return jsonify({final_summary, doc, summary_word_count, raw_word_count})
    return render_template('summary.html', raw_text=doc, final_summary=final_summary, 
                               summary_word_count=summary_word_count, raw_word_count=raw_word_count)
    
    
    
if __name__ == "__main__":
    app.run(debug=True)