import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VisualGC",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Google AdSense 코드
adsense_code = '''
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4969032818064598"
     crossorigin="anonymous"></script>
<!-- 광고 단위 코드 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-XXXXXX"
     data-ad-slot="XXXXXX"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
'''

# Streamlit 앱에 광고 삽입
components.html(adsense_code, height=100)

# Streamlit 사이드바 설정
st.sidebar.title("Support Us")
st.sidebar.markdown("""
If you find this app helpful, consider supporting us by buying us a coffee. Your support is greatly appreciated!
""")
st.sidebar.markdown(
    '<a href="https://www.buymeacoffee.com/call518"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=call518&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff" /></a>',
    unsafe_allow_html=True
)

st.write("# Welcome to VisualGC! 👋")

st.markdown("""
## Simplifying JVM Garbage Collection Analysis

At VisualGC.io, we offer a streamlined solution to visualize JVM garbage collection and heap size changes with ease. Our platform is designed to make the complex world of JVM memory management more accessible and understandable.

**How does VisualGC.io work?**
- **Simple Process:** Just copy and paste your jstat result logs into our site.
- **Instant Visualization:** Hit the 'Confirm' button and immediately see the changes in GC and heap sizes.
- **User-Friendly Interface:** Our Streamlit-powered dashboard is intuitive and easy to navigate, making GC log analysis straightforward.
- **Clear Insights:** Understand the impact of garbage collection on your JVM’s performance at a glance.
- **Optimize Your Application:** Use these visual insights to identify potential performance bottlenecks and optimize your application.

Get started with VisualGC.io today and experience the easiest way to visualize and understand your JVM’s garbage collection activities!

😎Contact to Admin: [JungJungIn](mailto:call518+visualgc@gmail.com)
""",
unsafe_allow_html=True
)
