# streamlit_rune_app.py

import streamlit as st

# --- Rune Emotion Profiles ---
rune_profiles = {
    'Fehu':     ['desire', 'motivation', 'ambition', 'satisfaction', 'abundance'],
    'Uruz':     ['vitality', 'strength', 'courage', 'resilience', 'readiness'],
    'Thurisaz': ['anger', 'defensiveness', 'urgency', 'pressure', 'fear'],
    'Ansuz':    ['clarity', 'insight', 'communication', 'inspiration', 'inner knowing'],
    'Raidho':   ['purpose', 'movement', 'vision', 'alignment', 'forward focus'],
    'Kenaz':    ['creativity', 'transformation', 'illumination', 'inspiration', 'breakthrough'],
    'Gebo':     ['gratitude', 'connection', 'mutuality', 'love', 'harmony'],
    'Wunjo':    ['joy', 'happiness', 'contentment', 'peace', 'celebration'],
    'Hagalaz':  ['chaos', 'stress', 'pressure', 'breakthrough', 'disruption'],
    'Nauthiz':  ['frustration', 'urgency', 'pressure', 'unmet needs', 'inner resistance'],
    'Isa':      ['stillness', 'numbness', 'frozen', 'detachment', 'pause'],
    'Jera':     ['patience', 'growth', 'natural rhythm', 'acceptance', 'perseverance'],
    'Eihwaz':   ['endurance', 'transformation', 'inner strength', 'shadow work', 'resilience'],
    'Perthro':  ['mystery', 'uncertainty', 'fate', 'intuition', 'surrender'],
    'Algiz':    ['protection', 'awareness', 'spiritual connection', 'boundaries', 'defense'],
    'Sowilo':   ['confidence', 'clarity', 'triumph', 'motivation', 'radiance'],
    'Tiwaz':    ['discipline', 'justice', 'courage', 'focus', 'alignment to truth'],
    'Berkano':  ['nurture', 'healing', 'compassion', 'gentle strength', 'renewal'],
    'Ehwaz':    ['trust', 'momentum', 'movement', 'partnership', 'emotional rhythm'],
    'Mannaz':   ['self-awareness', 'identity', 'belonging', 'social reflection', 'humanity'],
    'Laguz':    ['flow', 'emotion', 'intuition', 'empathy', 'dreaming'],
    'Ingwaz':   ['peace', 'potential', 'inner preparation', 'patience', 'gestation'],
    'Dagaz':    ['awakening', 'breakthrough', 'clarity', 'change', 'light after shadow'],
    'Othala':   ['heritage', 'ancestral pull', 'belonging', 'rootedness', 'legacy'],
}

# --- Rituals and Meditations ---
rune_actions = {
    'Nauthiz': {
        'ritual': "Clasp hands tightly, then slowly release. Focus on unmet needs.",
        'meditation': "Breathe into tension, exhale slowly. Feel where pressure lives in the body."
    },
    'Isa': {
        'ritual': "Sit in silence for 5 minutes. Embrace stillness.",
        'meditation': "Visualize a frozen lake. Trust what rests beneath the ice."
    },
    'Wunjo': {
        'ritual': "Smile at your reflection and speak one joyful thing.",
        'meditation': "Inhale with a smile, exhale with a sigh of contentment."
    },
    'Fehu': {
        'ritual': "Hold a coin or object of value. Focus on your relationship with receiving.",
        'meditation': "Visualize energy flowing in and out like breath or light."
    },
}

# --- Rune Matching Engine ---
def match_runes_by_emotion(user_emotions, rune_profiles):
    rune_scores = {}
    for rune, emotions in rune_profiles.items():
        score = 0
        for emotion in emotions:
            if emotion in user_emotions:
                score += user_emotions[emotion]  # weight by input intensity
        rune_scores[rune] = score
    return sorted(rune_scores.items(), key=lambda x: x[1], reverse=True)

# --- Streamlit App Interface ---
st.title("Rune Signal AI")
st.markdown("Enter your emotional state and receive a rune-based ritual and meditation.")

# Emotion input form
emotion_input = st.text_area("Describe how you feel in a few words (e.g. frustrated, joyful, stuck, inspired):")

if st.button("Analyze") and emotion_input:
    # Parse emotions
    words = [word.strip().lower() for word in emotion_input.split(',') if word.strip()]
    user_emotions = {word: 1.0 for word in words}  # Default weight = 1.0

    results = match_runes_by_emotion(user_emotions, rune_profiles)
    top_rune = results[0][0]

    st.subheader(f"Top Rune Match: {top_rune}")
    st.write(f"**Score:** {results[0][1]:.2f}")

    if top_rune in rune_actions:
        st.markdown("**Suggested Ritual:**")
        st.write(rune_actions[top_rune]['ritual'])

        st.markdown("**Suggested Meditation:**")
        st.write(rune_actions[top_rune]['meditation'])
    else:
        st.info("No ritual/meditation defined for this rune yet.")

    st.markdown("---")
    st.markdown("**Other Rune Matches:**")
    for rune, score in results[1:4]:
        st.write(f"{rune}: {score:.2f}")
