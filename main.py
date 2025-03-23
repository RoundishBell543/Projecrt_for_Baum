import sys
import numpy as np
from PyQt6 import uic 
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, 
    QWidget, QVBoxLayout, QLabel, 
    QLineEdit, QPushButton, QMessageBox,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run_analytical_window)
        self.pushButton_2.clicked.connect(self.closeEvent)

    def run_analytical_window(self):
        self.analytical_window = Analytical_ChartWindow()
        self.analytical_window.show()
        
    def closeEvent(self):
        self.analytical_window = Geometric_ChartWindow()
        self.analytical_window.show()
        
        
class Analytical_ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('analytical_chart_window.ui', self) 
        
        self.pushButton_Bar.clicked.connect(self.run_bar_graph_window)
        self.pushButton_Pie.clicked.connect(self.run_pie_graph_window)
        
    def run_bar_graph_window(self):
        self.bar_graph = Bar_Graph_Window()
        self.bar_graph.show()
    def run_pie_graph_window(self):   
        self.pie_graph = Pie_Graph_Window()
        self.pie_graph.show()
        
        
class Geometric_ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('geometric_chart_window.ui', self)
        
        self.pushButton_Line.clicked.connect(self.run_line_graph_window)
        self.pushButton_Parabola.clicked.connect(self.run_parabola_graph_window)
        self.pushButton_Giperbola.clicked.connect(self.run_giperbola_graph_window)
        self.pushButton_Trigeometry.clicked.connect(self.run_trigeometry_graph_window)
        
    def run_line_graph_window(self):
        self.line_graph = Line_Graph_Window()
        self.line_graph.show()

    def run_parabola_graph_window(self):
        self.parabola_graph = Parabola_Graph_Window()
        self.parabola_graph.show()
    
    def run_giperbola_graph_window(self):
        self.giperbola_graph = Giperbola_Graph_Window()
        self.giperbola_graph.show()
        
    def run_trigeometry_graph_window(self):
        self.trigeometry_graph = Trigeometry_Graph_Window()
        self.trigeometry_graph.show()

class Bar_Graph_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Столбчатая диаграмма")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)

        # Поле для названия диаграммы
        self.title_label = QLabel("Введите название диаграммы:", self)
        layout.addWidget(self.title_label)
        self.title_input = QLineEdit(self)
        layout.addWidget(self.title_input)

        # Поле для ввода значений столбцов
        self.label = QLabel("Введите значения столбцов (например, 10, 20, 15):", self)
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Поле для ввода названий столбцов
        self.names_label = QLabel("Введите названия столбцов через запятую (например, A, B, C):", self)
        layout.addWidget(self.names_label)

        self.names_input = QLineEdit(self)
        layout.addWidget(self.names_input)

        # Кнопка построения графика
        self.plot_button = QPushButton("Построить диаграмму", self)
        self.plot_button.clicked.connect(self.plot_bar_chart)
        layout.addWidget(self.plot_button)

        # Полотно для диаграммы
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def plot_bar_chart(self):
        title = self.title_input.text()
        input_text = self.input_field.text()
        names_text = self.names_input.text()

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        try:
            # Разбиваем вводимые данные
            data = list(map(float, input_text.split(",")))
            bar_names = [name.strip() for name in names_text.split(",")]

            # Проверяем совпадение количества значений и названий
            if len(bar_names) != len(data):
                raise ValueError("Количество названий столбцов должно совпадать с количеством значений!")

            # Строим диаграмму
            ax.bar(bar_names, data, color="skyblue")
            ax.set_xlabel("Категории")
            ax.set_ylabel("Значения")
            ax.set_title(title if title else "Столбчатая диаграмма")

            self.canvas.draw()

        except ValueError as e:
            # Выводим сообщение об ошибке
            QMessageBox.critical(self, "Ошибка", str(e))
            ax.text(0.5, 0.5, "Ошибка ввода", fontsize=12, ha='center', transform=ax.transAxes)
            self.canvas.draw()

class Pie_Graph_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Круговая диаграмма")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)

        # Поле для названия диаграммы
        self.title_label = QLabel("Введите название диаграммы:", self)
        layout.addWidget(self.title_label)
        self.title_input = QLineEdit(self)
        layout.addWidget(self.title_input)

        # Поле для ввода значений сегментов
        self.label = QLabel(
            "Введите значения сегментов (например, 30, 40, 30):",
            self,
        )
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Поле для ввода названий сегментов
        self.names_label = QLabel(
            "Введите названия сегментов через запятую (например, A, B, C):",
            self,
        )
        layout.addWidget(self.names_label)

        self.names_input = QLineEdit(self)
        layout.addWidget(self.names_input)

        # Кнопка построения графика
        self.plot_button = QPushButton("Построить диаграмму", self)
        self.plot_button.clicked.connect(self.plot_pie_chart)
        layout.addWidget(self.plot_button)

        # Полотно для диаграммы
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def plot_pie_chart(self):
        title = self.title_input.text()
        input_text = self.input_field.text()
        names_text = self.names_input.text()

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        try:
            # Разбиваем вводимые данные
            data = list(map(float, input_text.split(",")))
            segment_names = [name.strip() for name in names_text.split(",")]

            # Проверяем совпадение количества значений и названий сегментов
            if len(segment_names) != len(data):
                raise ValueError("Количество названий сегментов должно совпадать с количеством значений!")

            # Строим диаграмму
            ax.pie(data, labels=segment_names, autopct='%1.1f%%', startangle=90)
            ax.set_title(title if title else "Круговая диаграмма")

            self.canvas.draw()
        
        except ValueError as e:
            # Выводим сообщение об ошибке
            QMessageBox.critical(self, "Ошибка", str(e))
            ax.text(0.5, 0.5, "Ошибка ввода", fontsize=12, ha='center', transform=ax.transAxes)
            self.canvas.draw()

class Line_Graph_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Построение линейных функций")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)

        # Поле для ввода функций
        self.label = QLabel("Введите функции через запятую (например, x**2, 2*x + 3):", self)
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Поле для ввода диапазона x
        self.range_label = QLabel("Введите диапазон для x (например, -10, 10):", self)
        layout.addWidget(self.range_label)

        self.range_input = QLineEdit(self)
        self.range_input.setText("-10, 10")
        layout.addWidget(self.range_input)

        # Кнопка построения графика
        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        # Полотно для графика
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Начальный диапазон x
        self.x_min, self.x_max = -10, 10

        # Подключение события прокрутки мыши
        self.canvas.mpl_connect("scroll_event", self.on_scroll)

    def plot_graph(self):
        function_texts = self.input_field.text().split(",")
        range_text = self.range_input.text()

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        try:
            # Получаем диапазон x
            self.x_min, self.x_max = map(float, range_text.split(","))
            x = np.linspace(self.x_min, self.x_max, 500)

            # Построение графиков для каждой функции
            for function_text in function_texts:
                function_text = function_text.strip()
                if function_text:
                    y = [eval(function_text, {"x": val, "np": np}) for val in x]
                    ax.plot(x, y, label=f"y = {function_text}")

            ax.set_title("График функции")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.legend()
            ax.grid()

            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            ax.text(0.5, 0.5, "Ошибка ввода", fontsize=12, ha='center', transform=ax.transAxes)
            self.canvas.draw()

    def on_scroll(self, event):
        #Обрабатывает прокрутку колесика мыши для изменения диапазона x.
        scale_factor = 1.1 if event.step > 0 else 0.9  # Увеличение или уменьшение диапазона
        range_size = (self.x_max - self.x_min) * scale_factor

        center = (self.x_max + self.x_min) / 2
        self.x_min = center - range_size / 2
        self.x_max = center + range_size / 2

        self.range_input.setText(f"{self.x_min:.2f}, {self.x_max:.2f}")
        self.plot_graph()  # Перерисовка графика
        
class Parabola_Graph_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Построение графиков функций")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)

        self.label = QLabel("Введите функции через запятую (например, x**2 + 2*x + 1, x**2 - 4*x):", self)
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        self.range_label = QLabel("Введите диапазон для x (например, -10, 10):", self)
        layout.addWidget(self.range_label)

        self.range_input = QLineEdit(self)
        self.range_input.setText("-10, 10")
        layout.addWidget(self.range_input)

        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.x_min, self.x_max = -10, 10
        self.canvas.mpl_connect("scroll_event", self.on_scroll)

    def plot_graph(self):
        functions = self.input_field.text().split(",")
        range_text = self.range_input.text()

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        try:
            self.x_min, self.x_max = map(float, range_text.split(","))
            x = np.linspace(self.x_min, self.x_max, 1000)

            for func in functions:
                func = func.strip()
                if func:
                    y = [eval(func, {"x": val, "np": np}) for val in x]
                    ax.plot(x, y, label=f"y = {func}")

            ax.set_title("График функции")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.legend()
            ax.grid()
            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            ax.text(0.5, 0.5, "Ошибка ввода", fontsize=12, ha='center', transform=ax.transAxes)
            self.canvas.draw()

    def on_scroll(self, event):
        scale_factor = 1.1 if event.step > 0 else 0.9
        range_size = (self.x_max - self.x_min) * scale_factor

        center = (self.x_max + self.x_min) / 2
        self.x_min = center - range_size / 2
        self.x_max = center + range_size / 2

        self.range_input.setText(f"{self.x_min:.2f}, {self.x_max:.2f}")
        self.plot_graph()

class Giperbola_Graph_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики гиперболических функций")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)

        self.label = QLabel(
            "Введите гиперболические функции через запятую (например, 1/x, (x-2)/(x+1)):", self
        )
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        self.range_label = QLabel("Введите диапазон для x (например, -10, 10):", self)
        layout.addWidget(self.range_label)

        self.range_input = QLineEdit(self)
        self.range_input.setText("-10, 10")
        layout.addWidget(self.range_input)

        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.ax = self.figure.add_subplot(111)

        # Подключаем обработчик масштабирования
        self.canvas.mpl_connect("scroll_event", self.on_scroll)

        self.plot_graph()  # Строим начальный график

    def plot_graph(self):
        functions = self.input_field.text().split(",")
        range_text = self.range_input.text()

        self.ax.clear()

        try:
            x_min, x_max = map(float, range_text.split(","))
            x = np.linspace(x_min, x_max, 1000)

            for func in functions:
                func = func.strip()
                if func:
                    y = np.full_like(x, np.nan)  # Заполняем NaN, чтобы избежать разрывов

                    for i, val in enumerate(x):
                        try:
                            y[i] = eval(func, {"x": val, "np": np})
                        except ZeroDivisionError:
                            y[i] = np.nan  # Пропускаем разрывы

                    self.ax.plot(x, y, label=f"y = {func}")

            self.ax.set_title("График гиперболической функции")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
            self.ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
            self.ax.legend()
            self.ax.grid()

            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            self.ax.text(0.5, 0.5, "Ошибка ввода", fontsize=12, ha='center', transform=self.ax.transAxes)
            self.canvas.draw()

    def on_scroll(self, event):
        """Масштабирование изображения при прокрутке колесика мыши."""
        scale_factor = 1.2 if event.step > 0 else 0.8

        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        x_center = (xlim[0] + xlim[1]) / 2
        y_center = (ylim[0] + ylim[1]) / 2

        new_xlim = [(x - x_center) * scale_factor + x_center for x in xlim]
        new_ylim = [(y - y_center) * scale_factor + y_center for y in ylim]

        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)

        self.canvas.draw()
        
        
class Trigeometry_Graph_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики тригонометрических функций")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)

        self.label = QLabel(
            "Введите функции через запятую (например, np.sin(x), np.cos(x), np.tan(x)):", self
        )
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        self.range_label = QLabel("Введите диапазон для x (например, -2*pi, 2*pi):", self)
        layout.addWidget(self.range_label)

        self.range_input = QLineEdit(self)
        self.range_input.setText("-6.28, 6.28")
        layout.addWidget(self.range_input)

        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.x_min, self.x_max = -6.28, 6.28
        self.canvas.mpl_connect("scroll_event", self.on_scroll)

    def plot_graph(self):
        functions = self.input_field.text().split(",")
        range_text = self.range_input.text()

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        try:
            self.x_min, self.x_max = map(float, range_text.split(","))
            x = np.linspace(self.x_min, self.x_max, 1000)

            for func in functions:
                func = func.strip()
                if func:
                    y = [eval(func, {"x": val, "np": np}) for val in x]
                    ax.plot(x, y, label=f"y = {func}")

            ax.set_title("График тригонометрической функции")
            ax.set_xlabel("x (радианы)")
            ax.set_ylabel("y")
            ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
            ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
            ax.legend()
            ax.grid()
            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            ax.text(0.5, 0.5, "Ошибка ввода", fontsize=12, ha='center', transform=ax.transAxes)
            self.canvas.draw()

    def on_scroll(self, event):
        scale_factor = 1.1 if event.step > 0 else 0.9
        range_size = (self.x_max - self.x_min) * scale_factor

        center = (self.x_max + self.x_min) / 2
        self.x_min = center - range_size / 2
        self.x_max = center + range_size / 2

        self.range_input.setText(f"{self.x_min:.2f}, {self.x_max:.2f}")
        self.plot_graph()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())