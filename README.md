# Text Summarization Web App
![image](https://github.com/Rafe2001/Text-Summerization-app/assets/108533597/dc171ecf-aba2-4725-8159-4484fc4f79b3)
![image](https://github.com/Rafe2001/Text-Summerization-app/assets/108533597/4195569e-597c-4922-9622-59da033d0caa)


**Text Summarization Web App** is a web application that allows users to summarize text documents and visualize the results. It leverages natural language processing (NLP) techniques to generate concise summaries from lengthy texts.

## Features

- **Text Summarization:** Summarize long paragraphs or documents into shorter, more digestible versions.
- **Word Tokenization:** Break down text into individual words for analysis.
- **Sentence Tokenization:** Split text into sentences, making it easier to identify key information.
- **Word Frequency Analysis:** Calculate the frequency of words to determine their importance in the text.
- **User-Friendly Interface:** A web-based interface for easy interaction and text analysis.

## How to Use

Follow these steps to run the Text Summarization Web App on your local machine:

1. **Clone the Repository:**

   ```shell
   git clone https://github.com/Rafe2001/Text-Summerization-app.git
   ```

2. **Navigate to the Project Directory:**

   ```shell
   cd text-summarization-web-app
   ```

3. **Install Dependencies:**

   ```shell
   pip install -r requirements.txt
   ```

4. **Run the App:**

   ```shell
   python app.py
   ```

5. **Open the App in Your Browser:**

   The app should be accessible in your web browser at `http://localhost:5000`. If it doesn't open automatically, navigate to this URL.

6. **Enter Text for Summarization:**

   In the app's web interface, enter or paste the text you want to summarize into the input field.

7. **Click "Submit":**

   After entering the text, click the "Submit" button to start the summarization process.

8. **View Summary:**

   The app will generate a summary of the input text based on its content. You can see the original text and the generated summary side by side.

9. **Analyze Word Frequency:**

   Explore the word frequency analysis to understand which words are most significant in the text.

## Requirements

- Python 3.x
- Flask
- spaCy (for NLP)
- HTML/CSS knowledge (for customization)

## Project Structure

The project is organized as follows:

- `app.py`: The Flask web application that handles user requests and communicates with the summarization module.
- `summary.py`: The summarization module that uses spaCy for text processing and summarization.
- `templates/`: Contains HTML templates for the web interface.
- `static/`: Contains static assets such as CSS files and images.

## Author

- [Abdul Rafe Khan](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Flask](https://flask.palletsprojects.com/) for making it easy to create web applications.
- [spaCy](https://spacy.io/) is used for natural language processing tasks in this project.

