import streamlit as st
import json
import altair as alt
# from altair_saver import save
import pandas as pd
import streamlit.components.v1 as components


questions_dict = json.load(open('./questions.json', 'r'))
party_scores = json.load(open('./party_scores.json'))

st.set_page_config(
    page_title="app",
    page_icon="👋",
)


with st.form("my_form"):

    responses = dict()  # question-response pair

    for q in questions_dict:

        # show question and choices
        st.write(questions_dict[q]["question"])
        for choice_triplet in questions_dict[q]["choices"]:
            responses[choice_triplet["choice"]] = st.checkbox(choice_triplet["choice"])

            # assign score
            if responses[choice_triplet["choice"]]:
                for party in choice_triplet["parties"]:
                    for tag in choice_triplet["tags"]:
                        party_scores[party][tag] += 1
        st.markdown("---")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(party_scores)

df = pd.DataFrame(party_scores, columns=list(party_scores.keys()))
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'tag'})
df_melt = pd.melt(df, id_vars="tag", value_vars=party_scores.keys(), var_name="party", value_name="score", )
df_melt = df_melt[["party", "tag", "score"]].sort_values(["party", "tag"])
st.write(df_melt)

# alt.Chart(df).mark_bar().encode()
chart = alt.Chart(df_melt).mark_bar().encode(
    x="party",
    y="score"
)
st.altair_chart(chart)

# chart.save("chart.png")
# save(chart, 'chart.png')

# HtmlFile = open("chart.html", 'r', encoding='utf-8')
# source_code = HtmlFile.read()
# print(source_code)
# components.html(source_code)

# components.html(
#     """
#         <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button"
#         data-text="Check my cool Streamlit Web-App🎈"
#         data-url="https://streamlit.io"
#         data-show-count="false">
#         data-size="Large"
#         data-hashtags="streamlit,python"
#         Tweet
#         </a>
#         <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
#     """
# )


components.html(
    """
    <html>
    <head>
    <title>Your Website Title</title>
    <!-- You can use Open Graph tags to customize link previews.
    Learn more: https://developers.facebook.com/docs/sharing/webmasters -->
    <meta property="og:url"           content="https://www.somesite.com/your-page.html" />
    <meta property="og:type"          content="website" />
    <meta property="og:title"         content="Oh My Title" />
    <meta property="og:description"   content="Your description" />
    <meta property="og:image"         content="https://ibb.co/yfR99LJ" />
    </head>
    <body>
    
    <!-- Load Facebook SDK for JavaScript -->
    <div id="fb-root"></div>
    <script>(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
    fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));</script>
    
    <!-- Your share button code -->
    <div class="fb-share-button" 
    data-href="https://www.somesite.com/your-page.html" 
    data-layout="button_count">
    </div>
    """
)

st.write("Outside the form")
