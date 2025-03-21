import sys
from PyQt5 import QtWidgets, uic, QtCore

class UserForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_ui.ui", self)  # Qt Designer UI 불러오기

        # OK 및 Cancel 버튼 이벤트 연결
        self.buttonBox.accepted.connect(self.ok_clicked)   # OK 버튼
        self.buttonBox.rejected.connect(self.cancel_clicked)  # Cancel 버튼

        # 창 팝업 위치 설정
        self.move(300, 300)

        # 창의 테두리 제거
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 테두리 없는 창 만들기

        # placeholder text 설정
        self.name_input.setPlaceholderText("홍길동")  # 이름 입력 필드
        self.studentid_input.setPlaceholderText("20250000")  # 학번번 입력 필드
        self.department_input.setPlaceholderText("기계공학부")  # 학과 입력 필드
        self.contact_input.setPlaceholderText("010-1234-5678")  # 전화번호 입력 필드
        self.printnum_input.setPlaceholderText("0")  # 프린터번호 입력 필드
        self.h_input.setPlaceholderText("0")  # 출력 시 입력 필드
        self.m_input.setPlaceholderText("0")  # 출력 분분 입력 필드

    def ok_clicked(self):
        # name = self.name_input.text()
        # phone = self.phone_input.text()
        QtWidgets.QMessageBox.information(self, "확인")
        self.accept()  # 다이얼로그 닫기

    def cancel_clicked(self):
        QtWidgets.QMessageBox.warning(self, "취소", "입력을 취소했습니다.")
        self.reject()  # 다이얼로그 닫기

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UserForm()
    window.show()
    sys.exit(app.exec_())
