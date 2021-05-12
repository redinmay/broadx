import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

#plt.rc("font", family="Malgun Gothic")


st.title(":musical_score: BROADCAST DATA REPORT")


"""
#### 2020년 2분기 방송업무 시스템 처리 결과보고입니다. 청구기간: 2020.4~6, 분배년월: 2020.12
"""
st.write("")


# 파일 데이터 로딩
#
df1 = pd.read_excel('방송자료금액2020Q2.xlsx')
df2 = pd.read_csv('f2_repo.csv')
df3 = pd.read_csv('result_final_2_VAT_for_check.csv')
repo1 = pd.read_csv('ffinal.csv')
repo2 = pd.read_csv('repo2.csv')

df1 = df1[['방송사','2019년 방송사용료', '분기별 사용료', '청구금액', '실청구금액', '보류금4%', '분배금', 'TV분배금', 'RADIO분배금','전체사용회수', '지분율합', '관리비율']]
df1 = df1.set_index('방송사')

# 데이터 수정
#repo1 = repo1.remane(columns={'업체명':'방송사'})

PW = "1239@6i0o3Z$2j0j"
#login
userpw = st.sidebar.text_input("Enter Password!!", type="password")

if userpw != PW:
    # sidebar area
    st.error("Invalided Password! Try again")
    
else:
    # Load main report page

    menu = ["종합개요","분배자료","분배데이터"]
    choice = st.sidebar.selectbox("메인메뉴를 선택하세요",menu)

    if choice == '종합개요':
        # 방송사 선택 사이드바 생성
        sec = ['KBS', 'SBS', 'MBC', 'Total']
        board = st.sidebar.radio("방송사를 선택하세요", sec)
        
        if board == 'KBS':

            # 종합개요 리포팅
            st.subheader(':notes:  방송사별 종합 개요')
            st.write('')

            # 컬럼 레이아웃 첫번째 파트
            col1, col2 = st.beta_columns([2, 1])
            
            with col1:
                dkbs = df1[df1.index =='KBS']
                dkbs1 = dkbs[['실청구금액', '보류금4%', '분배금']]
                dkbs2 = dkbs[['전체사용회수', '지분율합', '관리비율']]
                dkbs3 = dkbs[['2019년 방송사용료', '분기별 사용료']]
                st.table(dkbs1.style.format({'실청구금액': '{:,.0f}','보류금4%': '{:,.0f}','분배금': '{:,.0f}' }))
                st.table(dkbs2.style.format({'전체사용회수': '{:,.0f}','지분율합': '{:,.2f}','관리비율': '{:,.2f}' }))
                st.table(dkbs3.style.format({'2019년 방송사용료': '{:,.0f}','분기별 사용료': '{:,.0f}'}))
                
            with col2:
                dc = dkbs1[['보류금4%', '분배금']]
                st.bar_chart(dc)

            
            # 히트수 리포팅
            st.subheader(':sunglasses:  히트수 개요')
            st.write('')

            # 컬럼 레이아웃 두번째 파트
            col1, col2 = st.beta_columns([1, 1])
            
            with col1:
                hk = df2[df2['방송사']=='KBS']
                hitkbs = pd.pivot_table(hk, values="관리코드", index=["구분1"], columns=["사용형태"], aggfunc=np.size, margins=True, margins_name="합계")
                st.table(hitkbs)

            with col2:
                hk = df2[df2['방송사']=='KBS']
                hitkbs = pd.pivot_table(hk, values="관리코드", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.size, margins=True, margins_name="합계")
                st.table(hitkbs)

            # 분배점수 리포팅
            st.subheader(':pushpin:  분배점수 개요')
            st.write('')

            # 컬럼 레이아웃 세번째 파트
            col1, col2 = st.beta_columns([1, 1])
            
            with col1:
                hk = df2[df2['방송사']=='KBS']
                hitkbs = pd.pivot_table(hk, values="분배점수", index=["구분1"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
                st.table(hitkbs)

            with col2:
                hk = df2[df2['방송사']=='KBS']
                hitkbs = pd.pivot_table(hk, values="분배점수", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
                st.table(hitkbs)


            # 지분점수 리포팅
            st.subheader(':avocado:  지분점수(지분율*분배점수) 개요')
            st.write('')

            # 컬럼 레이아웃 세번째 파트
            #col1, col2 = st.beta_columns([3, 1])
            
            st.write('음악유형별')
            hk = df2[df2['방송사']=='KBS']
            hitkbs = pd.pivot_table(hk, values="지분점수", index=["구분1"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
            st.table(hitkbs)
            st.write('모니터링업체별')
            hk = df2[df2['방송사']=='KBS']
            hitkbs = pd.pivot_table(hk, values="지분점수", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
            st.table(hitkbs)


        elif board == 'MBC':
            # 종합개요 리포팅
            st.subheader(':notes:  방송사별 종합 개요')
            st.write('')

            # 컬럼 레이아웃 첫번째 파트
            col1, col2 = st.beta_columns([2, 1])
            
            with col1:
                dmbc = df1[df1.index =='MBC']
                dmbc1 = dmbc[['실청구금액', '보류금4%', '분배금']]
                dmbc2 = dmbc[['전체사용회수', '지분율합', '관리비율']]
                dmbc3 = dmbc[['2019년 방송사용료', '분기별 사용료']]
                st.table(dmbc1.style.format({'실청구금액': '{:,.0f}','보류금4%': '{:,.0f}','분배금': '{:,.0f}' }))
                st.table(dmbc2.style.format({'전체사용회수': '{:,.0f}','지분율합': '{:,.2f}','관리비율': '{:,.2f}' }))
                st.table(dmbc3.style.format({'2019년 방송사용료': '{:,.0f}','분기별 사용료': '{:,.0f}'}))
                
            with col2:
                dc = dmbc1[['보류금4%', '분배금']]
                st.bar_chart(dc)

            
            # 히트수 리포팅
            st.subheader(':sunglasses:  히트수 개요')
            st.write('')

            # 컬럼 레이아웃 두번째 파트
            col1, col2 = st.beta_columns([1, 1])
            
            with col1:
                hm = df2[df2['방송사']=='MBC']
                hitm = pd.pivot_table(hm, values="관리코드", index=["구분1"], columns=["사용형태"], aggfunc=np.size, margins=True, margins_name="합계")
                st.table(hitm)

            with col2:
                hm = df2[df2['방송사']=='MBC']
                hitm = pd.pivot_table(hm, values="관리코드", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.size, margins=True, margins_name="합계")
                st.table(hitm)

            # 분배점수 리포팅
            st.subheader(':pushpin:  분배점수 개요')
            st.write('')

            # 컬럼 레이아웃 세번째 파트
            col1, col2 = st.beta_columns([1, 1])
            
            with col1:
                hm = df2[df2['방송사']=='MBC']
                hitm = pd.pivot_table(hm, values="분배점수", index=["구분1"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
                st.table(hitm)

            with col2:
                hm = df2[df2['방송사']=='MBC']
                hitm = pd.pivot_table(hm, values="분배점수", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
                st.table(hitm)


            # 지분점수 리포팅
            st.subheader(':avocado:  지분점수(지분율*분배점수) 개요')
            st.write('')

            # 컬럼 레이아웃 세번째 파트
            #col1, col2 = st.beta_columns([3, 1])
            
            st.write('음악유형별')
            hm = df2[df2['방송사']=='MBC']
            hitm = pd.pivot_table(hm, values="지분점수", index=["구분1"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
            st.table(hitm)
            st.write('모니터링업체별')
            hm = df2[df2['방송사']=='MBC']
            hitm = pd.pivot_table(hm, values="지분점수", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
            st.table(hitm)



        elif board == 'SBS':
            # 종합개요 리포팅
            st.subheader(':notes:  방송사별 종합 개요')
            st.write('')

            # 컬럼 레이아웃 첫번째 파트
            col1, col2 = st.beta_columns([2, 1])
            
            with col1:
                dmbc = df1[df1.index =='SBS']
                dmbc1 = dmbc[['실청구금액', '보류금4%', '분배금']]
                dmbc2 = dmbc[['전체사용회수', '지분율합', '관리비율']]
                dmbc3 = dmbc[['2019년 방송사용료', '분기별 사용료']]
                st.table(dmbc1.style.format({'실청구금액': '{:,.0f}','보류금4%': '{:,.0f}','분배금': '{:,.0f}' }))
                st.table(dmbc2.style.format({'전체사용회수': '{:,.0f}','지분율합': '{:,.2f}','관리비율': '{:,.2f}' }))
                st.table(dmbc3.style.format({'2019년 방송사용료': '{:,.0f}','분기별 사용료': '{:,.0f}'}))
                
            with col2:
                dc = dmbc1[['보류금4%', '분배금']]
                st.bar_chart(dc)

            
            # 히트수 리포팅
            st.subheader(':sunglasses:  히트수 개요')
            st.write('')

            # 컬럼 레이아웃 두번째 파트
            col1, col2 = st.beta_columns([1, 1])
            
            with col1:
                hm = df2[df2['방송사']=='SBS']
                hitm = pd.pivot_table(hm, values="관리코드", index=["구분1"], columns=["사용형태"], aggfunc=np.size, margins=True, margins_name="합계")
                st.table(hitm)

            with col2:
                hm = df2[df2['방송사']=='SBS']
                hitm = pd.pivot_table(hm, values="관리코드", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.size, margins=True, margins_name="합계")
                st.table(hitm)

            # 분배점수 리포팅
            st.subheader(':pushpin:  분배점수 개요')
            st.write('')

            # 컬럼 레이아웃 세번째 파트
            col1, col2 = st.beta_columns([1, 1])
            
            with col1:
                hm = df2[df2['방송사']=='SBS']
                hitm = pd.pivot_table(hm, values="분배점수", index=["구분1"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
                st.table(hitm)

            with col2:
                hm = df2[df2['방송사']=='SBS']
                hitm = pd.pivot_table(hm, values="분배점수", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
                st.table(hitm)


            # 지분점수 리포팅
            st.subheader(':avocado:  지분점수(지분율*분배점수) 개요')
            st.write('')

            # 컬럼 레이아웃 세번째 파트
            #col1, col2 = st.beta_columns([3, 1])
            
            st.write('음악유형별')
            hm = df2[df2['방송사']=='SBS']
            hitm = pd.pivot_table(hm, values="지분점수", index=["구분1"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
            st.table(hitm)
            st.write('모니터링업체별')
            hm = df2[df2['방송사']=='SBS']
            hitm = pd.pivot_table(hm, values="지분점수", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
            st.table(hitm)

        elif board == 'Total':
            # 종합개요 리포팅
            st.subheader(':notes:  방송사별 종합 개요')
            st.write('')

            # 컬럼 레이아웃 첫번째 파트
            col1, col2 = st.beta_columns([2, 1])
            
            with col1:
                dmbc = df1
                dmbc1 = dmbc[['실청구금액', '보류금4%', '분배금']]
                dmbc2 = dmbc[['전체사용회수', '지분율합', '관리비율']]
                dmbc3 = dmbc[['2019년 방송사용료', '분기별 사용료']]
                st.table(dmbc1.style.format({'실청구금액': '{:,.0f}','보류금4%': '{:,.0f}','분배금': '{:,.0f}' }))
                st.table(dmbc2.style.format({'전체사용회수': '{:,.0f}','지분율합': '{:,.2f}','관리비율': '{:,.2f}' }))
                st.table(dmbc3.style.format({'2019년 방송사용료': '{:,.0f}','분기별 사용료': '{:,.0f}'}))
                
            with col2:
                dc = dmbc1[['보류금4%', '분배금']]
                st.bar_chart(dc)

            
            # 히트수 리포팅
            st.subheader(':sunglasses:  히트수 개요')
            st.write('')

            # 컬럼 레이아웃 두번째 파트
            col1, col2 = st.beta_columns([1, 1])
            
            with col1:
                hm = df2
                hitm = pd.pivot_table(hm, values="관리코드", index=["구분1"], columns=["사용형태"], aggfunc=np.size, margins=True, margins_name="합계")
                st.table(hitm)

            with col2:
                hm = df2
                hitm = pd.pivot_table(hm, values="관리코드", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.size, margins=True, margins_name="합계")
                st.table(hitm)

            # 분배점수 리포팅
            st.subheader(':pushpin:  분배점수 개요')
            st.write('')

            # 컬럼 레이아웃 세번째 파트
            col1, col2 = st.beta_columns([1, 1])
            
            with col1:
                hm = df2
                hitm = pd.pivot_table(hm, values="분배점수", index=["구분1"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
                st.table(hitm)

            with col2:
                hm = df2
                hitm = pd.pivot_table(hm, values="분배점수", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
                st.table(hitm)


            # 지분점수 리포팅
            st.subheader(':avocado:  지분점수(지분율*분배점수) 개요')
            st.write('')

            # 컬럼 레이아웃 세번째 파트
            #col1, col2 = st.beta_columns([3, 1])
            
            st.write('음악유형별')
            hm = df2
            hitm = pd.pivot_table(hm, values="지분점수", index=["구분1"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
            st.table(hitm)
            st.write('모니터링업체별')
            hm = df2
            hitm = pd.pivot_table(hm, values="지분점수", index=["모니터링업체"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name="합계")
            st.table(hitm)

        
    elif choice == '분배자료':

        #방송사 선택 사이트바 생성
        sec = ['KBS', 'SBS', 'MBC', 'Total']
        broad = st.sidebar.radio("방송사를 선택하세요", sec)

        # 서브 타이틀
        st.subheader(':bus:  분배자료 분석')

        if broad == 'KBS':
            fk = df2[df2['방송사']=='KBS']
            fk1 = pd.pivot_table(fk, values="곡당분배금", index=["음악유형","구분2"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name='합계')
            st.table(fk1)
            # 서브 타이틀
            st.subheader(':joystick:  항목별 분석')
            gg = fk.groupby(['방송사', '구분1', '사용형태'], as_index=False).agg(히트수=('관리코드', np.size), 지분율=('songrate', sum), 분배점수=('분배점수', sum), 지분점수=('지분점수', sum), 분배금=('곡당분배금', sum))
            st.table(gg.style.format({'히트수': '{:,.0f}','지분율': '{:,.2f}','분배점수': '{:,.0f}','지분점수': '{:,.2f}','분배금': '{:,.0f}'}))
            st.bar_chart(gg)

        elif broad == 'MBC':
            fk = df2[df2['방송사']=='MBC']
            fk1 = pd.pivot_table(fk, values="곡당분배금", index=["음악유형","구분2"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name='합계')
            st.table(fk1)
            # 서브 타이틀
            st.subheader(':joystick:  항목별 분석')
            gg = fk.groupby(['방송사', '구분1', '사용형태'], as_index=False).agg(히트수=('관리코드', np.size), 지분율=('songrate', sum), 분배점수=('분배점수', sum), 지분점수=('지분점수', sum), 분배금=('곡당분배금', sum))
            st.table(gg.style.format({'히트수': '{:,.0f}','지분율': '{:,.2f}','분배점수': '{:,.0f}','지분점수': '{:,.2f}','분배금': '{:,.0f}'}))

        elif broad == 'SBS':
            fk = df2[df2['방송사']=='SBS']
            fk1 = pd.pivot_table(fk, values="곡당분배금", index=["음악유형","구분2"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name='합계')
            st.table(fk1)
            # 서브 타이틀
            st.subheader(':joystick:  항목별 분석')
            gg = fk.groupby(['방송사', '구분1', '사용형태'], as_index=False).agg(히트수=('관리코드', np.size), 지분율=('songrate', sum), 분배점수=('분배점수', sum), 지분점수=('지분점수', sum), 분배금=('곡당분배금', sum))
            st.table(gg.style.format({'히트수': '{:,.0f}','지분율': '{:,.2f}','분배점수': '{:,.0f}','지분점수': '{:,.2f}','분배금': '{:,.0f}'}))
        else:
            fk = df2
            fk1 = pd.pivot_table(fk, values="곡당분배금", index=["방송사","음악유형","구분2"], columns=["사용형태"], aggfunc=np.sum, margins=True, margins_name='합계')
            st.table(fk1)
            # 서브 타이틀
            st.subheader(':joystick:  항목별 분석')
            gg = fk.groupby(['방송사', '구분1', '사용형태'], as_index=False).agg(히트수=('관리코드', np.size), 지분율=('songrate', sum), 분배점수=('분배점수', sum), 지분점수=('지분점수', sum), 분배금=('곡당분배금', sum))
            st.table(gg.style.format({'히트수': '{:,.0f}','지분율': '{:,.2f}','분배점수': '{:,.0f}','지분점수': '{:,.2f}','분배금': '{:,.0f}'}))
            #st.bar_chart(gg)




    elif choice == '분배데이터':
        #방송사 선택 사이트바 생성
        sec = ['KBS', 'SBS', 'MBC', 'Total']
        broad = st.sidebar.radio("방송사를 선택하세요", sec)

        # 서브 타이틀
        st.subheader(':card_file_box:  분배데이터 분석')

        if broad == 'KBS':
            fk = repo1[repo1['업체명']=='KBS']
            fk = fk[['구분', '분배대상금', '일반회원분배금', '일반미확인', '출판사국내', '출판사해외', '출판사국내해외']]
            st.table(fk.style.format({'분배대상금': '{:,.0f}','일반회원분배금': '{:,.0f}', '출판사국내': '{:,.0f}', '출판사해외': '{:,.0f}', '출판사국내해외': '{:,.0f}','출판사미확인국내분': '{:,.0f}'}))

            # 서브 타이틀
            st.subheader(':bulb:  면세/과세 분석')
            tx = repo2[repo2['업체명']=='KBS']
            tx = tx.set_index('업체명')
            tx1 = tx[['면세대상', '과세대상', '부가세','청구금액', '청구금액(VAT포함)']]
            tx2 = tx[['실면세대상', '과세대상', '부가세', '실청구금액','실청구금액(VAT포함)']]
            st.table(tx1.style.format({'면세대상': '{:,.0f}','과세대상': '{:,.0f}','부가세': '{:,.0f}','청구금액': '{:,.0f}','청구금액(VAT포함)': '{:,.0f}'}))
            tc1 = tx1[['면세대상', '과세대상', '부가세']]
            st.bar_chart(tc1)
            st.table(tx2.style.format({'실면세대상': '{:,.0f}','과세대상': '{:,.0f}','부가세': '{:,.0f}','실청구금액': '{:,.0f}','실청구금액(VAT포함)': '{:,.0f}'}))
            tc2 = tx2[['실면세대상', '과세대상', '부가세']]
            st.bar_chart(tc2)

        elif broad == 'MBC':
            fk = repo1[repo1['업체명']=='MBC']
            fk = fk[['구분', '분배대상금', '일반회원분배금', '일반미확인', '출판사국내', '출판사해외', '출판사국내해외']]
            st.table(fk.style.format({'분배대상금': '{:,.0f}','일반회원분배금': '{:,.0f}', '출판사국내': '{:,.0f}', '출판사해외': '{:,.0f}', '출판사국내해외': '{:,.0f}','출판사미확인국내분': '{:,.0f}'}))

            # 서브 타이틀
            st.subheader(':bulb:  면세/과세 분석')
            tx = repo2[repo2['업체명']=='MBC']
            tx1 = tx[['면세대상', '과세대상', '부가세','청구금액', '청구금액(VAT포함)']]
            tx2 = tx[['실면세대상', '과세대상', '부가세', '실청구금액','실청구금액(VAT포함)']]
            st.table(tx1.style.format({'면세대상': '{:,.0f}','과세대상': '{:,.0f}','부가세': '{:,.0f}','청구금액': '{:,.0f}','청구금액(VAT포함)': '{:,.0f}'}))
            st.table(tx2.style.format({'실면세대상': '{:,.0f}','과세대상': '{:,.0f}','부가세': '{:,.0f}','실청구금액': '{:,.0f}','실청구금액(VAT포함)': '{:,.0f}'}))


        elif broad == 'SBS':
            fk = repo1[repo1['업체명']=='SBS']
            fk = fk[['구분', '분배대상금', '일반회원분배금', '일반미확인', '출판사국내', '출판사해외', '출판사국내해외']]
            st.table(fk.style.format({'분배대상금': '{:,.0f}','일반회원분배금': '{:,.0f}', '출판사국내': '{:,.0f}', '출판사해외': '{:,.0f}', '출판사국내해외': '{:,.0f}','출판사미확인국내분': '{:,.0f}'}))
            
            # 서브 타이틀
            st.subheader(':bulb:  면세/과세 분석')
            tx = repo2[repo2['업체명']=='SBS']
            tx1 = tx[['면세대상', '과세대상', '부가세','청구금액', '청구금액(VAT포함)']]
            tx2 = tx[['실면세대상', '과세대상', '부가세', '실청구금액','실청구금액(VAT포함)']]
            st.table(tx1.style.format({'면세대상': '{:,.0f}','과세대상': '{:,.0f}','부가세': '{:,.0f}','청구금액': '{:,.0f}','청구금액(VAT포함)': '{:,.0f}'}))
            st.table(tx2.style.format({'실면세대상': '{:,.0f}','과세대상': '{:,.0f}','부가세': '{:,.0f}','실청구금액': '{:,.0f}','실청구금액(VAT포함)': '{:,.0f}'}))


        else:
            fk = repo1
            st.dataframe(fk.style.format({'분배대상금': '{:,.0f}','일반회원분배금': '{:,.0f}', '출판사국내': '{:,.0f}', '출판사해외': '{:,.0f}', '출판사국내해외': '{:,.0f}','출판사미확인국내분': '{:,.0f}'}))
            # 서브 타이틀
            st.subheader(':bulb:  면세/과세 분석')
            tx = repo2.set_index('업체명')
            tx1 = tx[['면세대상', '과세대상', '부가세','청구금액', '청구금액(VAT포함)']]
            tx2 = tx[['실면세대상', '과세대상', '부가세', '실청구금액','실청구금액(VAT포함)']]
            st.table(tx1.style.format({'면세대상': '{:,.0f}','과세대상': '{:,.0f}','부가세': '{:,.0f}','청구금액': '{:,.0f}','청구금액(VAT포함)': '{:,.0f}'}))
            cdata1 = tx1[['면세대상', '과세대상', '부가세']]
            st.bar_chart(cdata1)
            st.table(tx2.style.format({'실면세대상': '{:,.0f}','과세대상': '{:,.0f}','부가세': '{:,.0f}','실청구금액': '{:,.0f}','실청구금액(VAT포함)': '{:,.0f}'}))
            cdata2 = tx2[['실면세대상', '과세대상', '부가세']]
            st.bar_chart(cdata2)
        



