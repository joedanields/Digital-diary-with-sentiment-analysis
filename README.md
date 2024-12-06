# Digital Diary with Sentiment Analysis

## Overview

This is a simple command-line Python application that allows users to write daily journal entries. Each entry is analyzed for sentiment using the `TextBlob` library to classify it as positive, negative, or neutral. The app helps users track their emotional well-being over time by providing sentiment summaries and allowing them to view and search past entries.

## Features

- **Add New Entry**: Write a journal entry, which is analyzed for sentiment.
- **View All Entries**: See all past journal entries with sentiment feedback.
- **Search Entries**: Search through entries by keywords.
- **Mood Summary**: View a summary of moods (positive, negative, neutral) from all entries.
- **Persistent Storage**: Entries are saved in a text file for future access.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- `TextBlob` library

To install `TextBlob`, run:

```bash
pip install textblob
```

## Usage

1. Clone the repository or download the project files.
2. Navigate to the project folder and run the script:

```bash
python diary.py
```

3. Follow the on-screen prompts to add, view, search, or summarize journal entries.

## File Structure

- `diary.py`: Main Python script containing the application logic.
- `diary.txt`: Text file where all journal entries are stored (created automatically).

## Example Usage

1. **Add New Entry**:
    - You will be prompted to write a journal entry, which will be analyzed for sentiment.
    - Example:
      ```bash
      Write your journal entry: Today was a great day!
      ```

2. **View All Entries**:
    - Display all past journal entries with sentiment feedback.
    - Example:
      ```bash
      Date: 2024-12-04 10:00:00
      Mood: Positive
      Entry: Today was a great day!
      ```

3. **Mood Summary**:
    - View a breakdown of your emotional moods over time.
    - Example:
      ```bash
      Positive: 3 (60.0%)
      Negative: 2 (40.0%)
      Neutral: 0 (0.0%)
      ```

## How Sentiment Analysis Works

- The sentiment analysis is performed using the `TextBlob` library, which evaluates the text's polarity to classify it as:
  - **Positive**: Sentiment score greater than 0
  - **Negative**: Sentiment score less than 0
  - **Neutral**: Sentiment score equal to 0

## Contributions

Feel free to fork the repository and contribute by opening issues, submitting pull requests, or suggesting features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides an overview, installation instructions, usage examples, and a brief explanation of how the sentiment analysis works. You can further customize it based on the specific details of your project.
