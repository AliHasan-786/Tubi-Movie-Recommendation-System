# 🎥 Tubi Movie Recommendation System

### Personalized Movie Discovery with AI-Powered Explanations

## 📌 Overview
This project delivers a **personalized recommendation engine** designed for Tubi’s vast content library. Users select a movie they enjoy, and the system provides **five tailored recommendations**, along with **a natural-language explanation** generated using OpenAI’s GPT-3.5-Turbo.

This combines **data-driven recommendation algorithms** with **human-readable context**, helping users confidently discover new content aligned with their tastes.

🔗 [Live Demo on Hugging Face Spaces]((https://huggingface.co/spaces/ah786/Tubi-Movie-Recommendation-System))  
📊 [GitHub Repository](https://github.com/alihasan-786/Tubi-Movie-Recommendation-System)

---

## 💻 Tech Stack
| Technology      | Purpose                                          |
|-----------------|--------------------------------------------------|
| **Gradio**      | Interactive User Interface                       |
| **OpenAI API**  | AI-generated explanations                        |
| **pandas**      | Data cleaning & processing                       |
| **scikit-learn**| TF-IDF Vectorizer & Cosine Similarity            |
| **Hugging Face Spaces** | Hosting the application                  |

---

## 🎯 Project Goals
### Context
With over **250,000 titles**, Tubi offers incredible variety, but users often struggle with **choice overload**. Traditional recommendation engines focus solely on content matching — but users also want to know **why** something was recommended.

### Objective
This project addresses these gaps by:
- Providing **taste-based recommendations** using both **content similarity** and **persona-based clustering**.
- Offering a **clear, natural-language explanation** that connects each recommendation back to the user’s preferences.

---

## 🔗 Data Processing Workflow

### Step 1: Raw Dataset (Tubi-Data.csv)
- Initial dataset included key metadata:  
    - Titles  
    - Genres  
    - Ratings  
    - Length  
    - Description  
    - URLs

---

### Step 2: Data Cleaning (Tubi_Cleaned.csv)
- Processed in the **EDA.ipynb notebook**.
- Key steps:
    - Removed duplicates.
    - Standardized genres and ratings.
    - Generated new fields like content length categories.
- Result: A **cleaned, structured dataset** ready for clustering.

---

### Step 3: Persona Assignment & Clustering (Tubi_with_Personas_and_Clusters.csv)
- Combined genres, ratings, and lengths into a **combined features string**.
- Applied **TF-IDF vectorization** followed by **clustering** into 5 personas:

| Persona              | Description |
|---------------------|-------------------------------------------------------|
| Family Friendly     | Wholesome, lighthearted, suitable for all ages |
| Action Junkies      | High-energy, fast-paced thrillers & action films |
| Drama Lovers        | Emotionally charged, character-driven stories |
| Nostalgia Fans      | Retro classics & beloved throwbacks |
| Documentary Seekers | Informative, real-world content across topics |

---

## 🛠️ Recommendation System Architecture

### Input
- User selects a movie from the dropdown.

### Processing
- Identify the selected movie’s **persona**.
- Recommend 5 movies with a hybrid approach:
    - **TF-IDF similarity** (content-level match).
    - **Persona bonus** (extra weight for movies in the same persona).

### Output
- Top 5 recommendations with clickable links.
- AI-generated explanation describing how these picks fit the user’s tastes.

---

## 💬 Explanation Logic
Explanations are generated via **OpenAI GPT-3.5-Turbo**, using a structured prompt that combines:
- The selected movie.
- The user’s identified persona.
- The 5 recommended movies.

This results in **personalized, easy-to-understand text** that enhances trust and transparency.

---

## 📊 Results
✅ Intuitive, clean Gradio interface.  
✅ Recommendations feel **relevant** (content-based) and **aligned to taste** (persona-based).  
✅ Clear, user-friendly explanations enhance transparency.  
✅ Data pipeline ensures high-quality inputs, improving recommendation accuracy.

---
