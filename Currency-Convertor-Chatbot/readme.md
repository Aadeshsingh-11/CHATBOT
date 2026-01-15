# 🤖 Currency Converter Chatbot

A Currency Converter Chatbot built using **Python**, **Flask**, and **Dialogflow**, integrated with **Telegram**.  
The chatbot converts currency values based on natural language input like:

> **"500 USD to INR"**

---

## 📌 Project Overview

This project demonstrates how to build an end-to-end chatbot using:
- Natural Language Processing (Dialogflow)
- Backend Webhook (Flask)
- Third-party Currency Exchange API
- Telegram Bot integration

The bot understands user queries, extracts parameters (amount & currencies), fetches real-time exchange rates, and returns the converted value.

---

## ✨ Features

- 🌍 Real-time currency conversion  
- 🧠 NLP-based intent handling using Dialogflow  
- 🔗 Flask webhook integration  
- 🤖 Telegram chatbot support  
- 📡 Uses live exchange rate API  
- 📦 JSON-based request/response handling  

---

## 🧰 Tech Stack

- **Language:** Python 3  
- **Backend:** Flask  
- **NLP:** Dialogflow  
- **API:** ExchangeRate API  
- **Bot Platform:** Telegram  
- **HTTP Client:** Requests  

---

## 📂 Project Structure

```text
Currency-Converter-Chatbot/
│
├── main.py              # Flask webhook backend
├── requirements.txt     # Python dependencies
├── .idea/               # PyCharm project files
└── README.md
