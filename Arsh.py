import streamlit as st
import time

# Page setup
st.set_page_config(page_title="Arsh's Spooky Birthday Hunt", page_icon="🎂", layout="centered")

# Introduction with a section from the book, Friday the 13th context, and a joke
st.title("🔮 Arsh's Spooky Birthday Treasure Hunt 🎂")
st.write("""
Welcome, Buddhie! 🌙 In just 2 days, you'll be celebrating your 20th birthday. 🎂 Now, 20 might not sound that old, but for someone who's already called "Buddhie," it sure sounds like you're getting up there! 😜👵 But don't worry, because age is just a number — unless it's **Friday the 13th**, of course. 😱🖤 

Did you know that Friday the 13th is so rare that it only happens once or twice a year? 🌌 The day is shrouded in superstition, where shadows grow longer and whispers become louder. But don’t be afraid, dear old Buddhie, because amidst the darkness, there's a treasure waiting for you — a treasure that reveals how much you mean to me and how much I love you. 💕 Let's begin this mystical journey... if you dare! 👻
""")

st.write("---")

# Book Section Introduction (Spooky Version)
st.write("""
**A Tale of Two Strangers Who Became Soulmates**  
Once upon a time, under the blazing sun at a wedding far away, two strangers met. One, a shy Greeky Buddha 🧘‍♂️, who had never imagined he'd find a friend, a confidant, and a soulmate in the same moment. The other, a charming Ms. Unstoppable Radio 🎙️, whose smile was enough to melt any heart. They crossed paths, and little did they know, a bond was forming — a bond strong enough to withstand even the darkest nights and the most haunted of Fridays. 🌌

But the story didn't end there. A year later, at another wedding, under the moonlit sky, we met again. And this time, nothing could keep us apart... 💫🖤
""")

# Updated Instructions with Emojis
st.subheader("🕵️‍♂️ Uncover the Secrets to Reveal Your Special Message! 🔍")
st.write("""
Each clue below is a key that unlocks a piece of a hidden message crafted just for you, Buddhie. 💌✨ Solve them carefully and put all the pieces together to unveil a surprise that comes straight from my heart. 💖🖤 If you get stuck or need a hint, remember you can always call your favorite Greeky Buddha for help! 📞😉 Let's dive in! 🚀
""")

# Define clues and answers with emojis
clues = [
    {"question": "🕵️‍♀️ On a bright sunny day, amidst the crowd of unknown faces at a wedding far away, I saw someone who took my breath away... Your smile, your eyes, your warmth — it was like a spell. 🕸️ Who was that enchanting soul? (4 letters)", 
     "answer": "arsh"},
    {"question": "🎬 A year passed, and under a different sky, at Amarjit’s wedding, the air was filled with excitement and mystery. 🌕 I knew I had to see you again. But I was nervous, my heart raced. What was the one thing that gave me the courage to sit next to you during the movie? 🎥 (5 letters)", 
     "answer": "hands"},
    {"question": "🔥 Time went on, and with every shared secret, every laugh, every tear, my trust in you grew. 💕 But one day, a small spark of jealousy flickered. Instead of fear, it brought us closer. 🖤 What did that feeling teach me about us? 💖 (5 letters)", 
     "answer": "trust"},
]

# Initialize session state for answers
if 'answers' not in st.session_state:
    st.session_state['answers'] = [""] * len(clues)

# Function to check all answers and identify incorrect ones
def check_answers():
    incorrect_indices = [i for i, answer in enumerate(st.session_state['answers']) if answer.strip().lower() != clues[i]['answer']]
    return incorrect_indices

# Display all clues with more emojis
st.subheader("📝 Answer the Clues Below to Unlock the Special Message! 💡")
for i, clue in enumerate(clues):
    st.write(f"**Clue {i + 1}**: {clue['question']}")
    st.session_state['answers'][i] = st.text_input(f"🔑 Your answer for Clue {i + 1}:", value=st.session_state['answers'][i], key=f"answer_{i}")

# Check answers and reveal the final message if all are correct
if st.button("🎯 Submit All Answers"):
    incorrect_indices = check_answers()
    if not incorrect_indices:
        st.balloons()  # Show balloons if all answers are correct
        st.success("🎉 Amazing job, Buddhie! You've unlocked the secret message! 🎉 Get ready for the BIG surprise coming on Sunday, September 15th, on your birthday! 🥳🎂 Keep this excitement up, it's just the beginning! 💫")

        # Display warning message with a heartfelt note
        st.warning("""
        **🖤 My Dearest Arsh (Buddhie), 🖤**

        On this mystical night, when the world is draped in the rare shadows of Friday the 13th, I find myself lost in thoughts of you. They say this day is cursed, filled with superstitions and fears, but I believe it’s just another way to show how much light you bring into my life. ✨

        From the moment we met, like a flicker of light in the darkness, I knew you were someone extraordinary. I never imagined that at a random wedding, I would find not just a cousin, but the one who would become my **Best Friend for Life**. 💞 The one whose laughter feels like a spell, whose voice is my favorite melody, and whose presence calms the wildest storms in my heart.

        As we met again under the moonlit sky at Amarjit's wedding, I was filled with both excitement and nerves. But holding your hand, I knew I was where I belonged. ❤️ You, Buddhie, make even the scariest nights feel safe, even the stormiest paths feel like a dance. You are my guiding star, the light in my shadows, and my companion on this wild journey called life. 🌙

        I want you to know, especially as your 20th birthday draws near, that my love for you is boundless, fierce, and eternal. No ghost, no shadow, no unlucky day could ever dim the brightness of what we share. 💖 You are my soulmate, my adventurer, my Ms. Unstoppable Radio. 🎤

        So, let's continue to walk hand in hand, through every misty path and moonlit night. 🌌 Because with you, I know I am home, no matter how dark the world gets. I can't wait to celebrate every moment with you, to share all our joys, secrets, and dreams. 🖤

        Forever and always,  
        **Greeky Buddha** 🖤
        """)

        # Add a delay for the spooky video reveal
        time.sleep(15)
        
        # Display spooky MP4 video
        st.video("Arsh.mp4", start_time=0) 
        
        # Banner with a message
        st.markdown("""
        ---
        ## 🎉 This is just the beginning, Buddhie! 🎉
        **Get ready for the grand finale — the big treasure awaits you: a personalized book that tells our story in every shade and every emotion.** Can't wait to see you soon!  
        **- Greeky Buddha** 🌟
        """)
    else:
        # Display which answers are incorrect
        st.error("🚫 Some answers are incorrect. Please check the following clues again: ❗")
        for i in incorrect_indices:
            st.write(f"- 🔍 Clue {i + 1}: {clues[i]['question']}")

# Footer
st.write("---")
st.write("🖤 Thanks for joining this spooky adventure. Can't wait to celebrate your special day! 🎉")
