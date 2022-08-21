import streamlit as st
import pickle
import numpy as np

pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))



st.title("Book Recommendation")

book_name = st.text_input('Enter Book name')

if st.button("Recommend"):
    def recommend(book_name):
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
        data = []
        
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title']==pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            
            data.append(item)
        return data
    
    val = recommend(book_name)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader(val[0][0])
        st.text(val[0][1])
        st.image(val[0][2])

    with col2:
        st.subheader(val[1][0])
        st.text(val[1][1])
        st.image(val[1][2])
            
    with col3:
        st.subheader(val[2][0])
        st.text(val[2][1])
        st.image(val[2][2])
    
    with col4:
        st.subheader(val[3][0])
        st.text(val[3][1])
        st.image(val[3][2])