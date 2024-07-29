from PySide6.QtWidgets import QTextEdit
class myTextEdit(QTextEdit):
    def __init__(self, parent):
        super(myTextEdit, self).__init__(parent)
        self.setAcceptDrops(True)

        self.input_path_file = ""

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.xlsx') or e.mimeData().text().endswith('.xls'):  # 目前只处理两种excel文件
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):  # 读取拖放文件的文件路径
        self.input_path_file = e.mimeData().text().replace('file:///', '')
        self.input_path_file = self.input_path_file.replace('/', '\\\\')
        print(self.input_path_file)