import qrcode
from PIL import Image
import streamlit as st
import io

st.title("QR Code Generator")

# This replaces input()
data = st.text_input("Enter a website or URL")

if st.button("Generate QR Code") and data.strip():

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color='red',
        back_color='white'
    )

    # Show the QR code on the webpage
    st.image(img)

    # Convert to PNG so user can download
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")

    st.download_button(
        label="Download QR Code",
        data=buffer.getvalue(),
        file_name="MyQRCode.png",
        mime="image/png"
    )
