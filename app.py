import streamlit as st
from ultralytics import YOLO
import cv2
import os
from PIL import Image
import base64

# st.markdown("""
# <style>
# .stApp {
#     background-color: #1e1e1e;
# }
# </style>
# """, unsafe_allow_html=True)


def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64("assets/eye.png")

# st.markdown(f"""
# <h1 style='display:flex; align-items:center; justify-content: center; gap:10px;'>
#     Sentinel.v8
#     <img src="data:image/png;base64,{img_base64}" width="40">
# </h1>
# """, unsafe_allow_html=True)


st.markdown(f"""
<h1 style='display:flex; align-items:center; gap:10px; margin-bottom:10px;'>
    Sentinel.v8 <img src="data:image/png;base64,{img_base64}" width="50" style="margin-top:-5px; vertical-align:middle;">
</h1>
""", unsafe_allow_html=True)


# col1,col2 = st.columns([1,8])

# with col1:
#     icon = Image.open("assets/security-camera.png")
#     st.image(icon, width=50)

# with col2:
#     st.title("Sentinel.v8")


st.markdown("""
<span style='color:#ff4b4b; font-size:18px; font-weight:600;'>Sentinel.v8</span> is a custom-trained object detection system built using YOLOv8.
It can detect and classify common road vehicles in real-world scenarios.

It is primarily trained on the IDD dataset along with a mix of custom-collected data from Bhilai, helping it adapt to diverse real-world road conditions.
""", unsafe_allow_html=True)


# st.markdown(""" 
# ### about it     
# <span style="color:red; font-weight:bold;">Sentinel.v8</span> is a custom-trained object detection system built using YOLOv8.
# """, unsafe_allow_html=True)  
# It can detect and classify common road vehicles in real-world scenarios.
# """)


# Load model
model = YOLO("models/v2_979data.pt")

option = st.selectbox("Choose input type", ["Image", "Video"])

def add_watermark(image):
    overlay = image.copy()
    cv2.putText(
        overlay,
        "PrateekSaha | Sentinel.v8",
        (10, image.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        1,
        cv2.LINE_AA
    )
    return overlay

# ---------------- IMAGE ----------------
if option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

    if uploaded_file is not None:
        file_path = os.path.join("inputs", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.image(file_path, caption="Original Image")

        if st.button("Detect"):
            results = model(file_path)

            result_img = results[0].plot()
            watermarked = add_watermark(result_img)
            st.image(watermarked, caption="Image Detected !")

# ---------------- VIDEO ----------------
elif option == "Video":
    uploaded_file = st.file_uploader("Upload a video", type=["mp4"])

    if uploaded_file is not None:
        file_path = os.path.join("input", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.video(file_path)

        if st.button("Detect Video"):
            output_path = os.path.join("output", uploaded_file.name)

            results = model.predict(
                source=file_path,
                save=True,
                conf=0.25,
                project="output",
                name="streamlit"
            )

            st.success("Processing done! Check output folder")


st.markdown(
    "<div style='text-align: center; font-size:12px; color: gray;'>PrateekSaha | Sentinel.v8©2026</div>",
    unsafe_allow_html=True
)

# instructions
st.sidebar.markdown("### Sentinel.v8 | PrateekSaha©2026")
st.sidebar.markdown("""
## Some general Instruction about the model 
### Can Detect
- Car
- Bike (including scooters)
- Truck

### Features
- Works on images and videos  
- Handles different angles and lighting conditions  
- Trained on a mix of real-world and curated dataset  

### Can't do!
- May confuse pedestrians with bikes  
- Performance depends on visibility and distance  
- Limited accuracy on rare vehicle types

""")