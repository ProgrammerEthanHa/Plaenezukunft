import streamlit as st
import pandas as pd
import altair as alt

st.header("Jugendliche - Was die junge Generation nach der Schule machen will in Deutschland 2015")
st.subheader("Wenn Du noch zur Schule gehst, welche Pläne hast Du für die Zeit nach der Schule?")

source = pd.DataFrame({
        'Anteil(%)': [33, 27, 6, 6, 5, 2, 2, 1, 7],
        'Pläne': ['Studieren', 'Ausbildung machen', 'Freiwilliges soziales Jahr machen', 'Reisen', 'Arbeiten', 'Bundeswehr', 'Gap year machen', 'Nichts, erst mal chillen', 'Weiß ich noch nicht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Pläne:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=4109; ab 12 Jahre; 2015
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Statista")