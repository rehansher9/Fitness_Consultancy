import os
import streamlit as st
from groq import Groq

# Set up the Groq API key
api_key = os.getenv("GROQ_API_KEY", "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")

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit app layout with emojis and colors
st.title("🏋️‍♂️ Personal Fitness & Meal Plan Generator 💪")

# Sidebar for navigation with emojis
with st.sidebar:
    st.header("🌟 Modules")
    module = st.selectbox(
        "Choose a module:",
        ["🍽️ Meal Plan Generator", "🏃 Exercise Routine", "📖 Guidelines"]
    )

# Function to interact with Groq's API
def get_response_from_model(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Meal Plan Generator with daily meal variation
if module == "🍽️ Meal Plan Generator":
    st.subheader("🍽️ Meal Plan Generator")
    
    # Body type, meal preference, and dietary needs input with emojis
    st.write("Customize your meal plan:")
    body_type = st.selectbox("Select your body type:", ["Skinny 🤏", "Average 👍", "Overweight 💪"])
    dietary_restrictions = st.multiselect(
        "Dietary restrictions (if any):",
        ["Lactose intolerant 🥛🚫", "Vegan 🌱", "Gluten-free 🌾🚫", "No meat 🍗🚫"]
    )
    goal = st.selectbox("Select your dietary goal:", ["Gain muscle 🏋️‍♂️", "Lose weight 🏃‍♀️", "Maintain weight ⚖️"])
    meal_preference = st.radio("Meal preference:", ["Meaty 🍖", "Vegetarian 🥦"])
    
    # Day selector for meal variation with slider emoji
    day = st.slider("Select the day for your meal plan 📅", 1, 7, 1)
    
    # Memo callout
    st.info("💡 Meal variety is key to staying consistent. Your meal plan will change daily to keep things fresh!")

    # Constructing prompt for a daily-changing meal plan
    meal_plan_prompt = f"""
    User has a {body_type.split()[0].lower()} body type with a goal to {goal.lower().split()[0]}.
    They have the following dietary restrictions: {', '.join(dietary_restrictions)}.
    They prefer a {meal_preference.lower()} diet.
    Generate a personalized meal plan for day {day}, including the number of meals recommended.
    Ensure that meals vary each day to prevent monotony.
    """

    # Display generated prompt for debugging
    with st.expander("📜 Show Generated Prompt"):
        st.code(meal_plan_prompt)

    # Button for meal plan generation with an emoji
    if st.button("🍽️ Generate Meal Plan"):
        response = get_response_from_model(meal_plan_prompt)
        st.success(response)

# Exercise Routine Module with color accents and tips
elif module == "🏃 Exercise Routine":
    st.subheader("🏃 Exercise Routine")
    st.write("Customize your workout routine:")

    # Fitness goals and schedule with emojis
    goal = st.selectbox("Your fitness goal:", ["Build muscle 💪", "Lose fat 🔥", "Maintain fitness 🧘‍♂️"])
    days_per_week = st.slider("Workout days per week 🗓️:", min_value=3, max_value=6)
    target_areas = st.multiselect("Target areas:", ["Full body 🏋️", "Upper body 💪", "Lower body 🦵", "Core 🧘‍♂️"])

    # Memo callout with tips
    st.info("💪 Pro Tip: Consistency is key! Stick to your routine to see the best results.")

    # Constructing prompt for exercise routine
    exercise_prompt = f"""
    User has a goal to {goal.split()[0].lower()}. They plan to work out {days_per_week} days per week, 
    focusing on {', '.join(target_areas)}.
    Generate a personalized exercise routine.
    """

    # Display generated prompt for debugging
    with st.expander("📜 Show Generated Prompt"):
        st.code(exercise_prompt)

    # Button for exercise routine generation with emoji
    if st.button("🏃 Generate Exercise Routine"):
        response = get_response_from_model(exercise_prompt)
        st.success(response)

# Guidelines Module with a memo and sections for clarity
elif module == "📖 Guidelines":
    st.subheader("📖 General Fitness & Nutrition Guidelines")

    # Select specific guideline type with emoji
    guideline_type = st.selectbox("Choose guideline type:", ["Nutrition 🍎", "Exercise 🏋️", "Both 🏃‍♂️🍽️"])

    # Memo with motivational message
    st.info("✨ Remember, small daily improvements lead to big results! ✨")

    # Constructing prompt for guidelines
    guidelines_prompt = f"""
    Provide concise and effective {guideline_type.lower()} guidelines for a general user interested in fitness.
    """

    # Display generated prompt for debugging
    with st.expander("📜 Show Generated Prompt"):
        st.code(guidelines_prompt)

    # Button for generating guidelines
    if st.button("📖 Generate Guidelines"):
        response = get_response_from_model(guidelines_prompt)
        st.success(response)
