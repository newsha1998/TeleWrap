# TeleWrap 🚀

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue)](https://pypi.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Support](https://img.shields.io/badge/python-3.8%2B-brightgreen)](https://www.python.org/)

**TeleWrap** is a frictionless Python wrapper for the Telegram Bot API. It focuses on developer ergonomics, allowing you to move from idea to production-ready bot with minimal boilerplate and maximum readability.

---

## ✨ Key Features

* **Zero-Boilerplate Setup:** Get a bot running in under 10 lines of code.
* **Intuitive Decorators:** Clean routing for commands, messages, and callbacks.
* **Smart State Management:** Simple tools for handling complex user conversations.
* **Built-in Smoothness:** Automatic handling of common API headaches like Markdown parsing and rate limits.

## 📦 Installation

Install TeleWrap via pip:

```bash
pip install telewrap

```

## 🚀 Quick Start

Build a simple "Hello World" bot in seconds:

```python
from telewrap import TeleBot

# Initialize your bot
bot = TeleBot("YOUR_BOT_TOKEN")

@bot.command("start")
def handle_start(chat):
    chat.send_message("Welcome! This bot was built smoothly with TeleWrap. 🚀")

@bot.on_message()
def echo(chat, message):
    chat.reply(f"You said: {message.text}")

if __name__ == "__main__":
    bot.run()

```

## 🛠 Why TeleWrap?

Building bots should be fun, not frustrating. Here is how **TeleWrap** makes your code smoother:

| Feature | Standard Libraries | TeleWrap |
| --- | --- | --- |
| **Keyboard Creation** | Nested JSON dictionaries | Simple Python lists |
| **Markdown** | Manual escape characters | Automatic smart-parsing |
| **Error Handling** | Try/Except blocks everywhere | Built-in graceful recovery |
| **Media Sending** | Complex InputFile objects | Pass a simple URL or path string |

## 📖 Documentation

*(Coming Soon)* - We are working on comprehensive docs to help you master every feature of TeleWrap.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
