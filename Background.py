import streamlit as st

st.set_page_config(page_title="Background",layout="wide")


page_bg = """
<style>
.stApp{
background-image: url("https://wallpapers.com/images/featured/luffy-smile-os5fogrcl2bylfkf.jpg");
 background-size: cover; 
 backgrpund-position: center;
 centre background-attachment: fixed ;
 opacity:0.9;
 }
</style>
"""
st.markdown(page_bg,unsafe_allow_html=True)

st.markdown("""
<style>
.box{
    width:300px;
    background: rgba(255,255,255,0.2);  
    padding:20px;
    border-radius:10px;
    backdrop-filter: blur(10px); 
    text-align:center;
    color:black;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="box">Hello!!! Click an option to view image</div>', unsafe_allow_html=True)


st.markdown(
"""
<style>
.Desc_box{
width=300px;
padding=50px;
border:2px solid black;
boarder-radius=10px;
background-color:rgba(255,255,255,0.2);
text-align:centre;
backdrop-filter: blur(50px);
color:black;
""",unsafe_allow_html=True
    )

st.markdown("""
<style>
h1:hover{
    color:white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    text-shadow:0px 0px 20px white;
}
</style>
""", unsafe_allow_html=True)

st.title("Image Viewer")

image1=("https://4kwallpapers.com/images/wallpapers/mount-everest-3440x1440-11019.jpg")
image2=("https://wallpapercat.com/w/full/9/4/c/777151-3840x2160-desktop-4k-the-taj-mahal-wallpaper-photo.jpg")
image3=("https://hips.hearstapps.com/autoweek/assets/s3fs-public/10-classic-recreations-1969-boss-429-mustang.jpg")
image4=("https://images.pexels.com/photos/20408462/pexels-photo-20408462.jpeg?cs=srgb&dl=pexels-jack-baghel-2199968-20408462.jpg&fm=jpg")



col1,col2,col3,col4=st.columns(4)

image_selected=None
about=""
with col1:
 
    if st.button("Mountain",use_container_width=True):
        image_selected=image1
        about="World's Tallest Mountain - The Mount Everest"
with col2:
    if st.button("7-Wonders",use_container_width=True):
        image_selected=image2
        about="One of the 7 Wonders in India - Taj Mahal"
        
with col3:
    if st.button("Vehicle",use_container_width=True):
        image_selected=image3
        about="The most classiest car - Ford Mustang"
with col4:
    if st.button("Food",use_container_width=True):
        image_selected=image4
        about="Food with low calories - Chapati"


if image_selected:
    st.markdown(f"<div class=Desc_box>{about}</div>",unsafe_allow_html=True)
    st.image(image_selected,use_container_width=True)
    
