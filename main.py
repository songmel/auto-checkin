import gspread
import datetime
import sys
from PyQt5 import QtWidgets, uic, QtCore

class UserForm(QtWidgets.QDialog):
    def __init__(self, sheet):
        super().__init__()

        self.sheet = sheet # sheet 클래스 의존성 추가가

        uic.loadUi("main_ui.ui", self)  # Qt Designer UI 불러오기

        # User 정보
        self.name = "Unknown"
        self.studentid = "00000000"
        self.department = "Unknown"
        self.contact = "000-0000-0000"
        self.printnum = "0"
        self.printtime = "0시간 0분"

        # 창 팝업 위치 설정
        self.move(300, 300)

        # 창의 테두리 제거
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 테두리 없는 창 만들기

        # OK 및 Cancel 버튼 이벤트 연결
        self.buttonBox.accepted.connect(self.ok_clicked)   # OK 버튼
        self.buttonBox.rejected.connect(self.cancel_clicked)  # Cancel 버튼

        # placeholder text 설정
        self.name_input.setPlaceholderText("홍길동")  # 이름 입력 필드
        self.studentid_input.setPlaceholderText("20250000")  # 학번번 입력 필드
        self.department_input.setPlaceholderText("기계공학부")  # 학과 입력 필드
        self.contact_input.setPlaceholderText("010-1234-5678")  # 전화번호 입력 필드
        self.printnum_input.setPlaceholderText("0")  # 프린터번호 입력 필드
        self.h_input.setPlaceholderText("0")  # 출력 시 입력 필드
        self.m_input.setPlaceholderText("0")  # 출력 분분 입력 필드

    def ok_clicked(self):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d")
        self.name = self.name_input.text()
        self.studentid = self.studentid_input.text()
        self.department = self.department_input.text()
        self.contact = self.contact_input.text()
        self.printnum = self.printnum_input.text()
        self.printtime = self.h_input.text() + "시간 " + self.m_input.text() + "분"

        self.sheet.write_item(formatted_time, self.name, self.studentid, self.department, self.contact, self.printnum, self.printtime)

        QtWidgets.QMessageBox.information(self, "전송완료", "전송을 완료했습니다.")
        self.accept()  # 다이얼로그 닫기

    def cancel_clicked(self):
        QtWidgets.QMessageBox.warning(self, "취소", "입력을 취소했습니다.")
        self.reject()  # 다이얼로그 닫기


class sheet_manager():
    def __init__(self):
        super().__init__()

        self.gc = gspread.service_account(filename='service_account.json') # !!!사용계정 api json으로 설정할 것 !!!
        self.sh = self.gc.open("checkin test") # !!!스프레드시트 제목으로 설정할 것!!!
        self.wsh = self.sh.worksheet("sheet_test") # !!!작업시트 이름으로 설정할 것!!!

    def get_item(self):
        print(self.wsh.get('A1'))

    def write_item(self, current_time, name, studentid, department, contact, printnum, printttime):
        # 특정 열에서 마지막 값이 있는 행 찾기 (예: A열)
        column_values = self.wsh.col_values(1)  # A열(1번 열)의 모든 값 가져오기
        last_filled_row = len(column_values)  # 마지막 값이 있는 행 번호

        # 새로운 데이터 추가 (마지막 행 아래)
        next_row = last_filled_row + 1  # 다음 빈 행
        self.wsh.update(f"A{next_row}:G{next_row}", [[current_time, name, studentid, department, contact, printnum, printttime]])  # A열에 값 추가


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    sheet = sheet_manager()
    window = UserForm(sheet)
    window.show()
    sys.exit(app.exec_())
