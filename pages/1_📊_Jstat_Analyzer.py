import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Streamlit 페이지 설정
st.set_page_config(
    page_title="Jstat Analyzer",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    """
    # Jstat Analyzer
    #### jstat log collection commands
    ```
    # jstat -gc -t {PID} {interval}
    
    Example) jstat -gc -t 384746 10000ms
    ```
    """
)
# st.sidebar.header("Jstat Data Visualization")

# Streamlit 사이드바 설정
st.sidebar.title("Support Us")
#st.sidebar.markdown("""
#If you find this app helpful, consider supporting us by buying us a coffee. Your support is greatly appreciated!
#""")
st.sidebar.markdown(
    '<a href="https://www.buymeacoffee.com/call518"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=call518&button_colour=9AD9FF&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff" /></a>',
    unsafe_allow_html=True
)

# 도움말 섹션
with st.expander("Help"):
    st.markdown("""
- **Timestamp**: Time elapsed since command execution (seconds)
- **S0C**: Current size of the first survivor space (KB)
- **S1C**: Current size of the second survivor space (KB)
- **S0U**: Used space of the first survivor space (KB)
- **S1U**: Used space of the second survivor space (KB)
- **EC**: Current size of the Eden space (KB)
- **EU**: Used space of the Eden space (KB)
- **OC**: Current size of the Old generation space (KB)
- **OU**: Used space of the Old generation space (KB)
- **MC**: Current size of the Metaspace (KB)
- **MU**: Used space of the Metaspace (KB)
- **CCSC**: Current size of the Compressed Class Space (KB)
- **CCSU**: Used space of the Compressed Class Space (KB)
- **YGC**: Count of Young Generation Garbage Collections
- **YGCT**: Total time spent in Young Generation GC (seconds)
- **FGC**: Count of Full Garbage Collections
- **FGCT**: Total time spent in Full GC (seconds)
- **GCT**: Total time spent in GC (seconds)
- **YGC Bar Color**: <span style='display: inline-block; width: 12px; height: 12px; background-color: rgba(255, 215, 0, 0.2);'></span>
- **FGC Bar Color**: <span style='display: inline-block; width: 12px; height: 12px; background-color: rgba(255, 28, 37, 0.2);'></span>
    """, unsafe_allow_html=True)

# 입력 형식 선택 (텍스트 또는 파일 업로드)
input_type = st.radio("Choose your input method:", ('Text Input', 'File Upload'))

# 텍스트 입력
if input_type == 'Text Input':
    txt_jstat = st.text_area(
        "Enter your jstat results here:",
        value = """================= (This is sample data. Replace it with your own data.) ================= 
        Timestamp        S0C    S1C    S0U    S1U      EC       EU        OC         OU       MC     MU    CCSC   CCSU   YGC     YGCT    FGC    FGCT     GCT
            21.7 16896.0 21504.0 15657.1  0.0   122880.0 96107.2   899584.0   742457.8  4864.0 2952.7 512.0  277.6       6    0.078   3      0.068    0.146
            22.7 20480.0 19968.0  0.0    0.0   120320.0 17950.7  1128448.0   859646.8  4864.0 2954.9 512.0  277.6       7    0.090   4      0.088    0.178
            23.7 20480.0 19968.0  0.0    0.0   120320.0 57013.4  1128448.0   859646.8  4864.0 2954.9 512.0  277.6       7    0.090   4      0.088    0.178
            24.7 20480.0 19968.0  0.0    0.0   120320.0 96076.0  1128448.0   859646.8  4864.0 2954.9 512.0  277.6       7    0.090   4      0.088    0.178
            25.7 19968.0 21504.0  0.0    0.0   117760.0 13979.6  1262080.0   976836.2  4864.0 2954.9 512.0  277.6       8    0.107   5      0.099    0.205
            26.7 19968.0 21504.0  0.0    0.0   117760.0 53042.3  1262080.0   976836.2  4864.0 2954.9 512.0  277.6       8    0.107   5      0.099    0.205
            27.7 19968.0 21504.0  0.0    0.0   117760.0 92105.0  1262080.0   976836.2  4864.0 2954.9 512.0  277.6       8    0.107   5      0.099    0.205
            28.7 18432.0 19968.0  0.0   19531.3 115200.0 17826.0  1262080.0  1070586.6  4864.0 2954.9 512.0  277.6       9    0.115   5      0.099    0.214
            29.6 18432.0 19968.0  0.0   19531.3 115200.0 56888.7  1262080.0  1070586.6  4864.0 2954.9 512.0  277.6       9    0.115   5      0.099    0.214
            30.6 18432.0 19968.0  0.0   19531.3 115200.0 95951.3  1262080.0  1070586.6  4864.0 2954.9 512.0  277.6       9    0.115   5      0.099    0.214
            31.7 15872.0 21504.0  0.0    0.0   112640.0 21703.1  1480704.0  1199491.7  4864.0 2954.9 512.0  277.6      10    0.127   6      0.139    0.266
            32.7 15872.0 21504.0  0.0    0.0   112640.0 60765.7  1480704.0  1199491.7  4864.0 2954.9 512.0  277.6      10    0.127   6      0.139    0.266
            33.7 15872.0 21504.0  0.0    0.0   112640.0 99828.4  1480704.0  1199491.7  4864.0 2954.9 512.0  277.6      10    0.127   6      0.139    0.266
            34.7 20480.0 19968.0  0.0   19531.3 110080.0 29452.0  1480704.0  1289335.8  4864.0 2954.9 512.0  277.6      11    0.137   6      0.139    0.276
            35.7 20480.0 19968.0  0.0   19531.3 110080.0 68514.6  1480704.0  1289335.8  4864.0 2954.9 512.0  277.6      11    0.137   6      0.139    0.276
            36.7 20480.0 19968.0  0.0   19531.3 110080.0 107577.3 1480704.0  1289335.8  4864.0 2954.9 512.0  277.6      11    0.137   6      0.139    0.276
            37.7 19968.0 21504.0  0.0    0.0   107520.0 41139.0  1691648.0  1414336.3  4864.0 2954.9 512.0  277.6      12    0.149   7      0.151    0.300
            38.7 19968.0 21504.0  0.0    0.0   107520.0 80201.6  1691648.0  1414336.3  4864.0 2954.9 512.0  277.6      12    0.149   7      0.151    0.300
            39.7 18432.0 19968.0  0.0   19563.3 104960.0 17634.8  1691648.0  1511993.0  4864.0 2954.9 512.0  277.6      13    0.160   7      0.151    0.310
            40.7 18432.0 19968.0  0.0   19563.3 104960.0 56697.5  1691648.0  1511993.0  4864.0 2954.9 512.0  277.6      13    0.160   7      0.151    0.310
            41.7 18432.0 19968.0  0.0   19563.3 104960.0 95760.1  1691648.0  1511993.0  4864.0 2954.9 512.0  277.6      13    0.160   7      0.151    0.310
            42.7 17408.0 22016.0  0.0    0.0   102912.0 29331.1  1888768.0  1617464.3  4864.0 2954.9 512.0  277.6      14    0.173   8      0.171    0.343
            43.7 17408.0 22016.0  0.0    0.0   102912.0 68393.8  1888768.0  1617464.3  4864.0 2954.9 512.0  277.6      14    0.173   8      0.171    0.343
            44.7 22016.0 19968.0  0.0   19531.3 100864.0  9742.8  1888768.0  1695589.6  4864.0 2954.9 512.0  277.6      15    0.181   8      0.171    0.352
            45.7 22016.0 19968.0  0.0   19531.3 100864.0 48805.5  1888768.0  1695589.6  4864.0 2954.9 512.0  277.6      15    0.181   8      0.171    0.352
            46.7 22016.0 19968.0  0.0   19531.3 100864.0 87868.2  1888768.0  1695589.6  4864.0 2954.9 512.0  277.6      15    0.181   8      0.171    0.352
            47.7 19968.0 22016.0  0.0    0.0   98816.0  25345.1  2081280.0  1812776.1  4864.0 2954.9 512.0  277.6      16    0.193   9      0.228    0.421
            48.7 19968.0 22016.0  0.0    0.0   98816.0  64407.8  2081280.0  1812776.1  4864.0 2954.9 512.0  277.6      16    0.193   9      0.228    0.421
            49.7 22016.0 19968.0  0.0   19531.3 96768.0   9662.9  2081280.0  1886995.2  4864.0 2954.9 512.0  277.6      17    0.202   9      0.228    0.430
            50.7 22016.0 19968.0  0.0   19531.3 96768.0  48725.6  2081280.0  1886995.2  4864.0 2954.9 512.0  277.6      17    0.202   9      0.228    0.430
            51.7 22016.0 19968.0  0.0   19531.3 96768.0  87788.2  2081280.0  1886995.2  4864.0 2954.9 512.0  277.6      17    0.202   9      0.228    0.430
            52.7 19968.0 22016.0  0.0    0.0   94720.0  33077.6  2264576.0  2000276.9  4864.0 2954.9 512.0  277.6      18    0.212  10      0.239    0.451
            53.7 19968.0 22016.0  0.0    0.0   94720.0  72140.3  2264576.0  2000276.9  4864.0 2954.9 512.0  277.6      18    0.212  10      0.239    0.451
            54.7 22016.0 19968.0  0.0   19531.3 92672.0  17395.4  2264576.0  2070589.7  4864.0 2954.9 512.0  277.6      19    0.221  10      0.239    0.460
            55.7 22016.0 19968.0  0.0   19531.3 92672.0  56458.0  2264576.0  2070589.7  4864.0 2954.9 512.0  277.6      19    0.221  10      0.239    0.460
            56.7 19968.0 21504.0  0.0    0.0   90624.0   3906.3  2454016.0  2179968.3  4864.0 2954.9 512.0  277.6      20    0.236  11      0.253    0.489
            57.7 19968.0 21504.0  0.0    0.0   90624.0  44716.3  2454016.0  2179968.3  4864.0 2954.9 512.0  277.6      20    0.236  11      0.253    0.489
            58.7 19968.0 21504.0  0.0    0.0   90624.0  83779.0  2454016.0  2179968.3  4864.0 2954.9 512.0  277.6      20    0.236  11      0.253    0.489
            59.7 19968.0 19968.0  0.0   19531.3 88576.0  36846.6  2454016.0  2246374.9  4864.0 2954.9 512.0  277.6      21    0.245  11      0.253    0.497
            60.7 19968.0 19968.0  0.0   19531.3 88576.0  72003.0  2454016.0  2246374.9  4864.0 2954.9 512.0  277.6      21    0.245  11      0.253    0.497
            61.7 19968.0 21504.0  0.0    0.0   87040.0  25114.7  2635776.0  2351841.9  4864.0 2954.9 512.0  277.6      22    0.255  12      0.304    0.559
            62.7 19968.0 21504.0  0.0    0.0   87040.0  64177.4  2635776.0  2351841.9  4864.0 2954.9 512.0  277.6      22    0.255  12      0.304    0.559
            63.7 21504.0 21504.0  0.0   19531.3 88576.0  21219.4  2635776.0  2414342.1  4864.0 2954.9 512.0  277.6      23    0.264  12      0.304    0.568
            64.7 21504.0 21504.0  0.0   19531.3 88576.0  60282.0  2635776.0  2414342.1  4864.0 2954.9 512.0  277.6      23    0.264  12      0.304    0.568
            65.7 21504.0 21504.0  0.0    0.0   101888.0 13680.4  2795520.0  2519811.3  4864.0 2954.9 512.0  277.6      24    0.275  13      0.316    0.591
            66.7 21504.0 21504.0  0.0    0.0   101888.0 48836.8  2795520.0  2519811.3  4864.0 2954.9 512.0  277.6      24    0.275  13      0.316    0.591
            67.7 21504.0 21504.0  0.0    0.0   101888.0 87899.4  2795520.0  2519811.3  4864.0 2954.9 512.0  277.6      24    0.275  13      0.316    0.591
            68.7 20992.0 19968.0  0.0   19531.3 99840.0  29251.0  2795520.0  2597936.6  4864.0 2954.9 512.0  277.6      25    0.284  13      0.316    0.600
            69.7 20992.0 19968.0  0.0   19531.3 99840.0  68313.6  2795520.0  2597936.6  4864.0 2954.9 512.0  277.6      25    0.284  13      0.316    0.600
            70.7 19968.0 20992.0  0.0    0.0   97792.0   9698.2  2979328.0  2715124.6  4864.0 2954.9 512.0  277.6      26    0.296  14      0.328    0.624
            71.7 19968.0 20992.0  0.0    0.0   97792.0  48760.8  2979328.0  2715124.6  4864.0 2954.9 512.0  277.6      26    0.296  14      0.328    0.624
            72.7 19968.0 20992.0  0.0    0.0   97792.0  87823.5  2979328.0  2715124.6  4864.0 2954.9 512.0  277.6      26    0.296  14      0.328    0.624
            73.7 17920.0 19968.0  0.0   19531.3 95744.0  29173.5  2979328.0  2789343.6  4864.0 2954.9 512.0  277.6      27    0.305  14      0.328    0.633
            74.7 17920.0 19968.0  0.0   19531.3 95744.0  68236.1  2979328.0  2789343.6  4864.0 2954.9 512.0  277.6      27    0.305  14      0.328    0.633
            75.7 16896.0 21504.0  0.0    0.0   93696.0  13525.9  3158016.0  2902625.3  4864.0 2954.9 512.0  277.6      28    0.317  15      0.341    0.657
            76.7 16896.0 21504.0  0.0    0.0   93696.0  52588.6  3158016.0  2902625.3  4864.0 2954.9 512.0  277.6      28    0.317  15      0.341    0.657
            77.7 16896.0 21504.0  0.0    0.0   93696.0  91651.2  3158016.0  2902625.3  4864.0 2954.9 512.0  277.6      28    0.317  15      0.341    0.657
            78.7 20992.0 19968.0  0.0   19531.3 91648.0  40813.2  3158016.0  2972938.1  4864.0 2954.9 512.0  277.6      29    0.325  15      0.341    0.666
            79.7 20992.0 19968.0  0.0   19531.3 91648.0  79875.8  3158016.0  2972938.1  4864.0 2954.9 512.0  277.6      29    0.325  15      0.341    0.666
            80.7 19968.0 21504.0  0.0    0.0   89600.0  29071.5  3328512.0  3082313.5  4864.0 2954.9 512.0  277.6      30    0.336  16      0.353    0.689
            81.7 19968.0 21504.0  0.0    0.0   89600.0  68134.1  3328512.0  3082313.5  4864.0 2954.9 512.0  277.6      30    0.336  16      0.353    0.689
            82.7 19968.0 19968.0  0.0   19531.3 87552.0  21202.1  3328512.0  3148720.0  4864.0 2954.9 512.0  277.6      31    0.345  16      0.353    0.698
            83.7 19968.0 19968.0  0.0   19531.3 87552.0  60264.7  3328512.0  3148720.0  4864.0 2954.9 512.0  277.6      31    0.345  16      0.353    0.698
            84.7 19968.0 21504.0  0.0    0.0   86016.0  13375.8  3508736.0  3250287.8  4864.0 2954.9 512.0  277.6      32    0.360  17      0.369    0.730
            85.7 19968.0 21504.0  0.0    0.0   86016.0  52438.5  3508736.0  3250287.8  4864.0 2954.9 512.0  277.6      32    0.360  17      0.369    0.730
            86.7 19968.0 19968.0  0.0   19531.3 84480.0   9422.4  3508736.0  3312788.0  4864.0 2954.9 512.0  277.6      33    0.367  17      0.369    0.736
        """,
        height=300
    )
    data_input_provided = bool(txt_jstat.strip())

# 파일 업로드
elif input_type == 'File Upload':
    uploaded_file = st.file_uploader("Choose a file")
    data_input_provided = uploaded_file is not None
    if data_input_provided:
        # 파일 내용 읽기
        txt_jstat = uploaded_file.getvalue().decode("utf-8")
        # 업로드된 파일명 표시
        st.success(f"Uploaded file: {uploaded_file.name}")
    else:
        txt_jstat = ""

# 입력 받은 데이터 처리
def process_data(txt_jstat):
    lines = txt_jstat.split('\n')
    data = []
    header = None

    for line in lines:
        if line.strip():
            if 'Timestamp' in line:
                header = line.split()
                continue
            if header:
                data.append(line.split())

    df = pd.DataFrame(data, columns=header)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

### 입력 데이터가 1만 라인 이상일 경우, 인접 2라인을 평균처리하여 1라인으로 만듬(라인수 50%로 줄임)
### 한번 50%화 하였으나, 여전히 1만 라인 이상일 경우, 1만 라인 이하가 될때까지 반복
### 이 로직은 테스트해보지 못했음
# def process_data(txt_jstat):
#     lines = txt_jstat.split('\n')
#     header = None

#     # 헤더 추출
#     for line in lines:
#         if 'Timestamp' in line:
#             header = line.split()
#             break

#     # 데이터 병합 함수
#     def merge_data(lines):
#         merged_data = []
#         for i in range(0, len(lines), 2):
#             if i + 1 < len(lines):
#                 line1 = lines[i].split()
#                 line2 = lines[i + 1].split()
#                 averaged_line = [(float(a) + float(b)) / 2 for a, b in zip(line1, line2)]
#                 merged_data.append(averaged_line)
#             else:
#                 # 마지막 라인 처리 (홀수 라인일 경우)
#                 merged_data.append([float(x) for x in lines[i].split()])
#         return merged_data

#     # 데이터 병합 반복
#     while len(lines) > 10000:
#         lines = merge_data(lines)

#     # 최종 데이터 프레임 생성
#     data = [line.split() for line in lines if line.strip() and 'Timestamp' not in line]
#     df = pd.DataFrame(data, columns=header)
#     df = df.apply(pd.to_numeric, errors='coerce')
#     return df

# 입력 받은 데이터 처리
if st.button('Create Plot'):
    if not data_input_provided:
        st.error("Please provide jstat data through Text Input or upload a file before creating the plot.")
    else:
        with st.spinner('Generating plot...'):
            # 데이터를 줄 단위로 분리하고 DataFrame 생성
            lines = txt_jstat.split('\n')
            data = []
            header = None

            for line in lines:
                if line.strip():
                    # 헤더인 경우
                    if 'Timestamp' in line:
                        header = line.split()
                        continue
                    # 데이터 추가
                    if header:
                        data.append(line.split())

            df = pd.DataFrame(data, columns=header)
            
            # 데이터 타입 변환
            for col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

            # 함수: GC 이벤트를 표시하는 막대 생성
            def create_gc_bars(df, gc_column, color):
                bars = []
                for i in df.index[df[gc_column].diff() > 0]:
                    bars.append(
                        go.layout.Shape(
                            type="rect",
                            x0=df['Timestamp'][i-1],
                            x1=df['Timestamp'][i],
                            y0=0,
                            y1=1,
                            xref="x",
                            yref="paper",
                            opacity=0.5,
                            fillcolor=f'rgba({color},0.2)',  # 20% 투명도 적용
                            layer="below",
                            line_width=0  # 테두리 없애기
                        )
                    )
                return bars

            # 차트 생성 함수
            def create_chart(title, columns, y_label, colors):
                fig = go.Figure()
                for col, color in zip(columns, colors):
                    fig.add_trace(go.Scatter(
                        x=df['Timestamp'], y=df[col], 
                        mode='lines', 
                        name=col, 
                        # stackgroup='one',
                        # fill='tonexty', # 라인 아래 채움 불투명도 활성/비활성
                        line=dict(color=f'rgba({color},1)'),  # 완전 불투명
                        fillcolor=f'rgba({color},0.2)',  # 20% 투명도
                        showlegend=True,
                        legendgroup=col
                    ))
                
                fig.update_layout(
                    # title=title,
                    xaxis_title="Timestamp",
                    yaxis_title=y_label,
                    legend_title="Legend",
                    hovermode="x unified"
                )
                
                fig.update_yaxes(tickformat=',')

                fig.update_layout(shapes=create_gc_bars(df, 'YGC', '255, 215, 0') + create_gc_bars(df, 'FGC', '255, 28, 37'))
                st.plotly_chart(fig, use_container_width=True)

            # Heap Utilization 차트 생성
            st.markdown("## Heap Utilization")
            create_chart("Heap Utilization", ['S0U', 'S1U', 'EU', 'MU', 'CCSU', 'OU'], "Used (KB)", ['255, 155, 0', '255, 24, 0', '0, 204, 150', '3, 61, 179', '128, 255, 0', '151, 0, 255'])

            # Heap Capacity 차트 생성
            st.markdown("## Heap Capacity")
            create_chart("Heap Capacity", ['S0C', 'S1C', 'EC', 'MC', 'CCSC', 'OC'], "Capacity (KB)", ['255, 155, 0', '255, 24, 0', '0, 204, 150', '3, 61, 179', '128, 255, 0', '151, 0, 255'])

            # Total Garbage Collection Events 차트 생성
            st.markdown("## Total Garbage Collection Events")
            create_chart("Garbage Collection Events", ['YGC', 'FGC'], "Events", ['0, 204, 150', '255, 28, 37'])

            # Total Garbage Collection Time 차트 생성
            st.markdown("## Total Garbage Collection Time")
            create_chart("Garbage Collection Time", ['YGCT', 'FGCT', 'GCT'], "Time (Sec)", ['0, 204, 150', '255, 28, 37', '99, 102, 250'])
