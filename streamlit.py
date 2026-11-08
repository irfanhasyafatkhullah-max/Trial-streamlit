import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



st.write ("Hello world 123456")
st.write({"key" : "Value"})
st.write(123)
3*4
"Hello World" if False else "Bye"
"Hello World" if True else "Bye"
pressed = st.button("Tekan")
print ("first :", pressed)
pressed2 = st.button("Tekan kedua")
print("second:", pressed2)
st.title("Simple Title")
st.header("This is a header")
st.subheader('This is a subheader')
st.markdown("this is a **Markdown** also _Miring_")
st.caption("small text")
code_example = """
def greet(name):
    print("Hello", name)
"""
st.code(code_example,language="python")

st.divider()


st.image(os.path.join(os.getcwd(),"BG.jpg"),width=500)

#Data frame 
st.title("Streamlit elements demo")
st.subheader ("Data Frame")
df = pd.DataFrame({
    'Name' : ['irfan','hilal','azkal','nata'],
    'Umur' :[22,22,23,23],
    'Konsentrasi':['elektrik','medis','energi','medis']
})
st.dataframe(df)
#Data editor Section(Editable dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)

#static table section
st.subheader("Static table")
st.table(df)

st.subheader("Metrics")
st.metric(label="Total rows", value=len(df))
st.metric(label="Average Age", value=round(df['Umur'].mean(),1))

#JSON and Disct Section
st.subheader("JSON and Dict")
sample_dict ={
    'name' : 'Alice',
    'age' : 25,
    'skill' :['python','Data Sciece', 'machine learning'] 
    }

st.json(sample_dict)
st.write("Dictionary view", sample_dict)

#Streamlit Chart


st.title("Streamlit Chart")

# 1. Data random (3 kolom)
chart_data = pd.DataFrame({
    "X": range(1, 51),
    "Y": np.random.randint(1, 100, 50),
    "Z": np.random.randint(1, 100, 50)
})

# 2. Tampilkan data
st.subheader("Data")
st.dataframe(chart_data)

# 3. Line Chart
st.subheader("Line Chart")
st.line_chart(chart_data, x="X", y=["Y", "Z"])

# 4. Bar Chart
st.subheader("Bar Chart")
st.bar_chart(chart_data, x="X", y=["Y", "Z"])

# 5. Area Chart
st.subheader("Area Chart")
st.area_chart(chart_data, x="X", y=["Y", "Z"])

# 6. Scatter Chart
st.subheader("Scatter Chart")
st.scatter_chart(chart_data, x="Y", y="Z")

# 7. Pie Chart
#st.subheader("Pie Chart")
#fig = px.pie(chart_data, names="X", values="Y")
#st.plotly_chart(fig)

# 8. Box Plot
#st.subheader("Box Plot")
#fig = px.box(chart_data, y=["Y", "Z"])
#st.plotly_chart(fig)

# 9. Histogram
#st.subheader("Histogram")
#fig = px.histogram(chart_data, x="Y")
#st.plotly_chart(fig)



st.title("Streamlit Map")

# Data lokasi random di sekitar Yogyakarta
map = pd.DataFrame({
    "latitude": -7.80 + np.random.uniform(-0.05, 0.05, 50),
    "longitude": 110.37 + np.random.uniform(-0.05, 0.05, 50)
})

# Tampilkan data
st.subheader("Data Koordinat")
st.dataframe(map)

# Tampilkan Map
st.subheader("Peta Lokasi")
st.map(map)

#Pyplot Section
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
# Membuat chart
fig, ax = plt.subplots()

ax.plot(chart_data["X"], label = 'X')
ax.plot(chart_data["Y"], label = 'Y')
ax.plot(chart_data["Z"], label = 'Z')
ax.set_title("pyplot line chart")
ax.legend()
# Menampilkan chart
st.pyplot(fig)

#form element 

# Page Configuration
st.set_page_config(
    page_title="Form Demo",
    page_icon="📝",
    layout="centered"
)

# Header
st.title("📝 Form Demo")
st.write("Belajar membuat formulir menggunakan Streamlit")
st.divider()

# Membuat form
with st.form("my_form"):

    st.subheader("Personal Information")

    nama = st.text_input("Nama Lengkap", placeholder="Masukkan nama")
    email = st.text_input("Email", placeholder="nama@email.com")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Jenis Kelamin",
            ["Laki-laki", "Perempuan"]
        )

        pendidikan = st.selectbox(
            "Pendidikan",
            ["SMA/SMK", "Diploma", "S1", "S2", "S3"]
        )

    with col2:
        umur = st.number_input(
            "Umur",
            min_value=1,
            max_value=100,
            value=20
        )

        tanggal = st.date_input("Tanggal Lahir")

    st.divider()

    st.subheader("Additional Information")

    pekerjaan = st.radio(
        "Status",
        ["Pelajar", "Mahasiswa", "Bekerja", "Lainnya"],
        horizontal=True
    )

    minat = st.multiselect(
        "Bidang Minat",
        ["Programming", "Data Science", "AI",
         "Electronics", "IoT", "Engineering"]
    )

    pengalaman = st.slider(
        "Pengalaman Coding (Tahun)",
        min_value=0,
        max_value=20,
        value=1
    )

    setuju = st.checkbox("Saya menyetujui pengisian formulir")

    pesan = st.text_area(
        "Pesan",
        placeholder="Tuliskan pesan atau keterangan..."
    )

    file = st.file_uploader(
        "Upload Dokumen",
        type=["pdf", "docx", "xlsx"]
    )

    # Tombol submit
    submit = st.form_submit_button(
        "Submit Form",
        type="primary",
        use_container_width=True
    )


# Menampilkan hasil
if submit:

    if nama and email and setuju:

        st.success("Form berhasil dikirim!")

        st.subheader("Hasil Form")

        # Membuat DataFrame
        data = {
            "Nama": [nama],
            "Email": [email],
            "Gender": [gender],
            "Pendidikan": [pendidikan],
            "Umur": [umur],
            "Tanggal Lahir": [tanggal],
            "Status": [pekerjaan],
            "Minat": [", ".join(minat)],
            "Pengalaman Coding": [pengalaman],
            "Pesan": [pesan]
        }

        df = pd.DataFrame(data)
        
        col1, col2, col3 = st.columns(3)

        col1.metric("Umur", f"{umur} Tahun")
        col2.metric("Pengalaman", f"{pengalaman} Tahun")
        col3.metric("Minat", len(minat))

        st.write("**Nama:**", nama)
        st.write("**Email:**", email)
        st.write("**Jenis Kelamin:**", gender)
        st.write("**Pendidikan:**", pendidikan)
        st.write("**Tanggal Lahir:**", tanggal)
        st.write("**Status:**", pekerjaan)
        st.write("**Bidang Minat:**", ", ".join(minat) if minat else "-")
        st.write("**Pesan:**", pesan if pesan else "-")

        if file:
            st.write("**File:**", file.name)

        st.balloons()

    else:
        st.error("Nama, email, dan persetujuan wajib diisi!")

st.sidebar.title("this is sidebar")
st.sidebar.write("Bisa menulis pesan atau button")
sidebar_input = st.sidebar.text_input("Isi", placeholder="HAI")

#tabs layout
tab1, tab2,tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Berada di tab 1")

with tab2:
    st.write("Berada di tab 2")

with tab3:
    st.write("Berada di tab 3")

st.divider()

#coloumns
col1,col2,col3 = st.columns(3)
with col1 :
    st.header("kolom 1")
    st.write("Konten untuk kolom 1")

with col2 :
    st.header("kolom 2")
    st.write("Konten untuk kolom 2")
with col3 :
    st.header("kolom 3")
    st.write("Konten untuk kolom 3")

with st.container(border=True):
    st.write("Container")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Kolom 1")
        st.write("Konten untuk kolom 1")

    with col2:
        st.header("Kolom 2")
        st.write("Konten untuk kolom 2")

placeholder = st.empty()
placeholder.write("UPDATE UNTUK MEMBACA")
if st.button("Update Placeholder") :
    st.write("kccndcdcdsckNSCDJsdvjbdsvSDJVV")
    st.write("zLKDknkandsnvsNVDNJDVJNVNSNVsdjvNJDJDJSJN")

with st.expander("Expand for more details"):
    st.write("Tambahan info1")
    st.write("Tambahan info 2")
 
 #popover(tooltip)
st.write("arahkan ke tombol untuk info")
st.button("Tombol dengan info",help="SCROLL SAMPAI BAWAHH JOS")
 
if sidebar_input:
    st.write(f"you enter in the sidebar: {sidebar_input}")

 
#streamlit run .\streamlit.py
