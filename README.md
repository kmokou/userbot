# 🤖 Telegram Userbot with Auto-Writing Code

A powerful Telegram userbot built with Telethon that can automatically generate and write Python code based on user descriptions.

## ✨ Features

- **Auto-Writing Code**: Generate Python code from natural language descriptions
- **File Management**: Create files with generated code
- **Modular Architecture**: Clean, extensible codebase
- **Multiple Code Templates**: Calculator, Web Scraper, Data Analyzer, API Client, and more

## 🚀 Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/code <description>` | Generate code based on description | `/code calculator` |
| `/create <filename> <description>` | Create file with generated code | `/create calc.py calculator` |
| `/list` | List all files in current directory | `/list` |
| `/help` | Show help message | `/help` |

## 📋 Available Code Templates

- **Calculator** - Basic arithmetic operations
- **File Handler** - Read and display file contents
- **Web Scraper** - Basic web scraping with BeautifulSoup
- **Data Analyzer** - Pandas data analysis
- **API Client** - REST API interactions

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/userbot.git
   cd userbot
   ```

2. **Install dependencies:**
   ```bash
   pip install telethon
   ```

3. **Configure API credentials:**
   Create `config/secrets.json` with your Telegram API credentials:
   ```json
   {
       "api_id": "YOUR_API_ID",
       "api_hash": "YOUR_API_HASH",
       "session_name": "userbot_session",
       "admin_id": "YOUR_TELEGRAM_ID"
   }
   ```

4. **Run the userbot:**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
userbot/
├── main.py                 # Entry point
├── core/
│   ├── bot.py             # Main bot logic
│   ├── client.py          # Telegram client
│   └── dispatcher.py      # Module loader
├── modules/
│   ├── ping.py            # Basic ping module
│   └── code_generator.py  # Auto-writing code module
├── config/
│   ├── settings.py        # Configuration settings
│   └── secrets.json       # API credentials (gitignored)
└── .gitignore            # Git ignore rules
```

## 🔧 Configuration

### Getting Telegram API Credentials

1. Go to [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Go to "API Development Tools"
4. Create a new application
5. Copy the `api_id` and `api_hash`

### Setting up secrets.json

Create `config/secrets.json` with your credentials:
```json
{
    "api_id": 12345678,
    "api_hash": "your_api_hash_here",
    "session_name": "userbot_session",
    "admin_id": 123456789
}
```

## 🚀 Usage

1. **Start the userbot:**
   ```bash
   python main.py
   ```

2. **First time setup:**
   - Enter your phone number when prompted
   - Enter the verification code sent to your Telegram
   - The session will be saved for future use

3. **Use the commands in Telegram:**
   - Send `/help` to see available commands
   - Send `/code calculator` to generate calculator code
   - Send `/create calc.py calculator` to create a file

## 🔒 Security

- API credentials are stored in `config/secrets.json` (gitignored)
- Session files are automatically gitignored
- Sensitive data is never committed to the repository

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This userbot is for educational purposes. Please comply with Telegram's Terms of Service and use responsibly.

## 🆘 Support

If you encounter any issues:
1. Check the [Issues](https://github.com/yourusername/userbot/issues) page
2. Create a new issue with detailed information
3. Include your Python version and error logs

---

**Made with ❤️ using Telethon** 