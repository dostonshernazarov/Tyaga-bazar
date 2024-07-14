# MoldingInfoBot

## Overview
MoldingInfoBot is a Telegram bot built using the aiogram 2.24 library. This bot allows users to get information about moldings, send messages to admins, and receive advertisements and notifications from admins. The bot utilizes SQLite for database management.

## Features
- **Information Retrieval**: Users can get detailed information about various moldings.
- **Admin Announcements**: Admins can send advertisements and notifications to all users.
- **User Messaging**: Users can send messages to the admins through the bot.
- **SQLite Database**: Stores user data, molding information, and admin announcements.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)
- A Telegram account and a bot token from BotFather

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/dostonshernazarov/Tyaga-bazar.git
    cd Tyaga-bazar
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your bot token and admin ID:
    - Create a `.env` file in the root directory.
    - Add your bot token and admin ID to the `.env` file:
      ```env
      BOT_TOKEN=your_bot_token_here
      ADMIN_ID=your_admin_id_here
      ```

### Usage
1. Run the bot:
    ```bash
    python app.py
    ```

2. Open your Telegram app and search for your bot using its username. Start a chat with your bot and use the available commands.

## Project Structure
- **app.py**: The main bot application file.
- **handlers/**: Directory containing handler modules for different bot commands and events.
- **utils/**: Utility functions and helpers.
- **database/**: Contains SQLite database files and scripts.
- **requirements.txt**: Lists all the dependencies required for the project.

## Dependencies
All the dependencies required for this project are listed in the `requirements.txt` file. Below are the main libraries used:
- **aiogram==2.24**: For building the Telegram bot.
- **python-dotenv**: For loading environment variables from a `.env` file.
- **sqlite3**: For database management.

To install the dependencies, run:
```bash
pip install -r requirements.txt
