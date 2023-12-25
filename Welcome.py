import streamlit as st

st.set_page_config(
    page_title="VisualGC",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# st.sidebar.success("")

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
""")
