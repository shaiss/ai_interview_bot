# AI Interview Bot

AI Interview Bot is a simple conversation simulation between a guest, a podcast host, and an AI-powered Q&A provider. The guest provides a topic, the Q&A provider generates relevant questions, and the host asks one of the questions to the guest.

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/ai-interview-bot.git
cd ai-interview-bot
```

2. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project's root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Run the main script:

```
python main.py
```

2. Follow the prompts to provide a topic and answer the host's questions. Type `stop` to end the conversation.

3. After the conversation, a subtitle file (`transcript.srt`) will be generated in the project's root directory, containing the conversation's timestamps and text.

## License

This project is licensed under the [MIT License](LICENSE).

---

Replace `https://github.com/yourusername/ai-interview-bot.git` with the actual URL of your GitHub repository. Save this content as a `README.md` file in your project's root directory.