import streamlit as st  #[cite: 1]

st.title(
    " แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%"
)  #[cite: 1]

price = st.number_input(
    "กรอกราคาสินค้า (บาท):", value=0.0
)  #[cite: 1]

vat = price * 0.07  #[cite: 1]
net_price = price - vat  #[cite: 1]

st.header(
    f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท"
)  #[cite: 1]
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")  #[cite: 1]

st.divider()  #[cite: 1]

st.write("นิธินาถ พัฒนบุญแสน เลขที่ 30 ม.4/3")  #[cite: 1]
