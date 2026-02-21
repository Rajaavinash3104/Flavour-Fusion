

# 🍲 Flavour Fusion – AI-Driven Recipe Blog Generator

Flavour Fusion is an AI-powered web application that generates detailed, engaging, and well-structured recipe blogs using **Google Gemini (Generative AI)**. Built with **Streamlit**, this application allows users to enter a recipe topic and desired word count, and instantly receive a complete blog post including ingredients, preparation steps, tips, and conclusion.

To make the experience more fun, the app also displays a random programmer joke while generating the recipe blog.

---

## 🚀 Features

* 🔥 AI-generated detailed recipe blogs
* ✍️ Custom word count selection (200–2000 words)
* 🧠 Powered by Google Gemini (gemini-2.5-flash model)
* 🎭 Random programmer joke during content generation
* 📥 Download generated blog as a `.txt` file
* 🎨 Simple and interactive Streamlit UI
* 🔐 Secure API key handling using `.env` file

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (Frontend UI)
* **Google Generative AI (Gemini API)**
* **dotenv** (Environment variable management)
* **Random module** (Joke generation)

---

## 📌 How It Works

1. User enters:

   * Recipe Topic
   * Desired Word Count

2. The app:

   * Displays a random programming joke
   * Sends a structured prompt to the Gemini model
   * Generates a detailed recipe blog

3. The blog includes:

   * Engaging introduction
   * Ingredients list
   * Step-by-step instructions
   * Tips & variations
   * Short conclusion

4. User can:

   * View the blog inside the app
   * Download it as a text file

---

## 📂 Project Structure

```
Flavour-Fusion/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🔑 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/flavour-fusion.git
cd flavour-fusion
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Your Google API Key

Create a `.env` file and add:

```
GOOGLE_API_KEY=your_api_key_here
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧠 Model Configuration

The application uses:

* **Model:** `models/gemini-2.5-flash`
* Optimized prompt structure for structured blog generation
* Plain text output for easy download and publishing

---

## 🎯 Example Use Cases

* 🥗 Food bloggers generating recipe content
* 👩‍🍳 Culinary students writing practice blogs
* 🏠 Home cooks exploring new recipe ideas
* 📝 Content creators needing quick food blog drafts

---

## 📈 Future Enhancements

* Markdown export option
* PDF download feature
* Image generation for recipes
* Multi-language support
* User authentication
* Blog editing inside the app

---

## 💡 Learning Outcomes

This project demonstrates:

* Integration of LLM APIs (Gemini)
* Prompt engineering
* Streamlit app development
* Environment variable management
* Session state handling in Streamlit

---

## 👨‍💻 Author

**Karlapati Raja Avinash**

📍 India
