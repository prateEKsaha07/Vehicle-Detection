import streamlit as st
from ultralytics import YOLO
import cv2
import os

st.title("Sentinel.v8")

# loading model
model = YOLO("models/v2_979data.pt")


