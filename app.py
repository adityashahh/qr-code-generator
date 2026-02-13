import qrcode
from PIL import Image
import streamlit as st
import io

st.title("QR Code Generator")

data = st.text_input("Enter a website or URL")

if st.button("Generate QR Code") and data.strip():

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Convert to a standard PIL image so Streamlit can display it
    img = qr.make_image(fill_color='red', back_color='white').convert("RGB")

    st.image(img)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    st.download_button(
        label="Download QR Code",
        data=buffer,
        file_name="MyQRCode.png",
        mime="image/png"
    )
