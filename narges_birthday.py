import streamlit as st
import random

st.set_page_config(page_title="🎉 تولد نرگس 🐸💚", page_icon="🐸", layout="wide")

# ------------------- CSS شاین و انیمیشن -------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #ffb3e6, #b3e6ff, #d9ffb3);
    animation: bg 12s infinite alternate;
}

@keyframes bg {
    0% { background-position: 0% 50%; }
    100% { background-position: 100% 50%; }
}

h1 {
    text-shadow: 0 0 20px #fff, 0 0 40px #ff66cc;
}

.shiny {
    background: linear-gradient(90deg, #ff66cc, #ff99dd, #ff66cc);
    padding: 20px;
    border-radius: 20px;
    font-size: 40px;
    color: white;
    text-align: center;
    font-weight: bold;
    animation: shine 2s infinite alternate;
}

@keyframes shine {
    from { box-shadow: 0 0 10px #fff; }
    to { box-shadow: 0 0 30px #ff66cc; }
}

.shake {
    animation: shake 0.4s infinite;
}

@keyframes shake {
    0% { transform: translate(1px, 1px) rotate(0deg); }
    25% { transform: translate(-1px, 2px) rotate(-1deg); }
    50% { transform: translate(1px, -1px) rotate(1deg); }
    75% { transform: translate(-1px, -2px) rotate(-1deg); }
    100% { transform: translate(1px, 1px) rotate(0deg); }
}

/* دکمه کیوت */
div.stButton > button {
    background-color: #ff66cc;
    color: white;
    font-size: 22px;
    border-radius: 15px;
    padding: 12px 22px;
    font-weight: bold;
    box-shadow: 0 0 15px #ff99dd;
}

</style>
""", unsafe_allow_html=True)

# ------------------- Confetti -------------------
confetti_js = """
<script>
function fire(){
  for(let i=0;i<5;i++){
    confetti({
      particleCount: 200,
      spread: 150,
      startVelocity: 60,
      origin: { y: 0.3 }
    });
  }
}
fire();
</script>
"""
st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
""", unsafe_allow_html=True)

# ------------------- مراحل -------------------
if "step" not in st.session_state:
    st.session_state.step = 0

# ------------------- صفحه اول -------------------
if st.session_state.step == 0:
    st.markdown(f"""
    <h1 class='shiny'>🎉🐸💚 نرگس جوووون تولدت مبااارک 💚🐸🎉</h1>
    <p style='text-align:center; font-size:27px; font-weight:bold; color:#883377;'>
        امروز روز توئه، پرنسس 🎀  
        یه تست باحال برات ساختیم، آخرش هم یه فسقلی سوپرایزی داری!  
        حتما آخرش اسکرین بگیر بفرست برای فاطمه 😘💋  
    </p>
    """, unsafe_allow_html=True)

    if st.button("بزن بریم نرگسییی! 💚🎀", key="start_button"):
        st.session_state.step = 1
        st.markdown(confetti_js, unsafe_allow_html=True)

# ------------------- مرحله 1 -------------------
elif st.session_state.step == 1:
    q1 = st.radio("نرگس🌸 روزا رو بیشتر دوست داری یا شبا؟ 😍", ["روز 🌞", "شب 🌙"])
    if st.button("بعــدییی 🐸✨"):
        st.session_state.q1 = q1
        st.session_state.step = 2
        st.markdown(confetti_js, unsafe_allow_html=True)

# ------------------- مرحله 2 -------------------
elif st.session_state.step == 2:
    if "روز" in st.session_state.q1:
        q2 = st.radio("خب خانومی 🌞 کجا میریم؟ 💖",
                      ["کافه‌ای که همیشه دوست داشتی ☕💗",
                       "ساحل دریا 🌊✨",
                       "بافت قدیم 🏛️🌿",
                       "یه جای جدید 🤔💞"])
    else:
        q2 = st.radio("اوه اوه نرگسِ شب‌عاشق 🌙✨ مقصد؟",
                      ["کافه مورد علاقه‌ت ☕💗",
                       "ساحل دریا 🌊✨",
                       "بافت قدیم 🏛️🌿",
                       "یه جای جدید و مرموز 🤔💜"])
    if st.button("خب بزن بریم مرحله بعد 😭💗"):
        st.session_state.q2 = q2
        st.session_state.step = 3
        st.markdown(confetti_js, unsafe_allow_html=True)

# ------------------- مرحله 3 -------------------
elif st.session_state.step == 3:
    if "روز" in st.session_state.q1:
        q3 = st.radio("ملکه صبحونه‌ها 😭💗 صبحونه چی بخوریم؟",
                      ["ساندویچ سرد 🥪💚",
                       "کروسان و قهوه ☕🥐✨",
                       "نیمرو و چایی 🍳🍵💛"])
    else:
        q3 = st.radio("شام چی بخوریم خوشگل؟ 😍✨",
                      ["پیتزااا 🍕💖", "لازانیا 🍝💗", "پاستا 🍝✨"])
    if st.button("نتیجه رو بیار قووورباغه 😭🐸"):
        st.session_state.q3 = q3
        st.session_state.step = 4
        st.markdown(confetti_js, unsafe_allow_html=True)

# ------------------- نتیجه -------------------
elif st.session_state.step == 4:

    if "روز" in st.session_state.q1:
        result = f"""
        ### 🌞💚 نرگس جان!

        وای این روز فوق‌العاده‌ت رسید 😭🎀  
        قراره بری **{st.session_state.q2}**  
        و یه صبحونه‌ی خوشگل **{st.session_state.q3}** بخوری 😍✨  

        قورباغه‌ها از ذوق دارن غش می‌کنن برات 🐸💚  
        امروز *کاملاً روز توئه!* 🎉💖
        """
    else:
        result = f"""
        ### 🌙💜 نرگس عزیز!

        چه شب قشنگی قراره بسازی 😭✨  
        مقصدت: **{st.session_state.q2}**  
        شام خوشگل: **{st.session_state.q3}** 🍝💖  

        ماه و ستاره و قورباغه‌ها همه امشب با تو هماهنگن 🐸🌙✨
        """

    st.markdown(f"""
    <div style='background-color:#fff0fa; border-radius:25px; padding:30px;
                font-size:26px; font-weight:bold; color:#cc0066; text-align:center;
                box-shadow:0 0 25px #ff99dd;'>
        {result}

    """, unsafe_allow_html=True)

    st.markdown(confetti_js, unsafe_allow_html=True)
