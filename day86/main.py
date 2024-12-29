import tkinter as tk
from tkinter import ttk, messagebox
import random
import time


class TypingTestModel:
    """
    타이핑 테스트에 필요한 데이터(단어 리스트, 시간, 진행 상황)를 관리하고,
    통계 계산(WPM, CPM) 등 기본 로직을 담당.
    """

    def __init__(self):
        self.words_list = [
            "love", "life", "work", "hand", "over", "more", "back", "long", "home", "this",
            "that", "with", "from", "they", "people", "child", "world", "three", "under", "thing",
            "would", "could", "there", "after", "before", "night", "light", "early", "water", "great",
            "really", "small", "start", "right", "place", "again", "think", "every", "never", "other",
            "group", "about", "score", "point", "power", "sound", "music", "board", "heart", "voice",
            "ready", "mount", "phone", "field", "house", "video", "thank", "write", "learn", "teach",
            "still", "study", "money", "broad", "space", "trace", "frame", "brave", "truth", "front",
            "range", "river", "month", "forty", "fifty", "sixty", "smart", "green", "brown", "apple",
            "north", "south", "grain", "wheat", "bread", "lunch", "pizza", "white", "black", "floor",
            "chair", "table", "knife", "spoon", "fork", "ruler", "paper", "stone", "metal", "linen"
        ]

        self.time_limit = 60
        self.time_left = self.time_limit
        self.is_testing = False

        self.current_word_index = 0
        self.correct_words = 0
        self.correct_letters = 0
        self.start_time = 0.0

        self.highest_wpm = 0
        self.highest_cpm = 0

    def reset_test(self, time_limit: int):
        """새로운 테스트를 시작하기 위한 상태 초기화."""
        self.time_limit = time_limit
        self.time_left = time_limit
        self.is_testing = True

        self.current_word_index = 0
        self.correct_words = 0
        self.correct_letters = 0

        self.start_time = time.time()
        random.shuffle(self.words_list)

    def end_test(self):
        """테스트 종료 상태로 전환."""
        self.is_testing = False

    def compute_stats(self) -> tuple:
        """
        (cpm, wpm)을 계산해 반환한다.
        종료 시점 혹은 테스트 진행 중이라도 현재 상태를 바탕으로 계산 가능.
        """
        elapsed_time = time.time() - self.start_time
        if elapsed_time <= 0:
            return 0, 0
        cpm = int(self.correct_letters * 60 / elapsed_time)
        wpm = int(self.correct_words * 60 / elapsed_time)
        return cpm, wpm

    def update_highscore(self, cpm: int, wpm: int):
        """최고 기록 갱신 여부 확인 후 갱신."""
        if cpm > self.highest_cpm:
            self.highest_cpm = cpm
        if wpm > self.highest_wpm:
            self.highest_wpm = wpm


class TypingTestView:
    """
    Tkinter UI를 구성하고, Controller가 요청할 때 UI를 업데이트하는 메서드들을 제공.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test (Refactored)")

        self.label_guide = tk.Label(
            root,
            text="시간(초)을 선택하고 [Start]를 누른 뒤, 밑줄 친 단어 입력 후 스페이스를 누르세요!"
        )
        self.label_guide.pack(pady=5)

        top_frame = tk.Frame(root)
        top_frame.pack(pady=5)

        tk.Label(top_frame, text="Time (sec):").pack(side="left")
        self.combo_time = ttk.Combobox(top_frame, values=[30, 60, 90], width=5)
        self.combo_time.set("60")
        self.combo_time.pack(side="left", padx=5)

        self.label_cpm = tk.Label(top_frame, text="CPM: ?")
        self.label_cpm.pack(side="left", padx=10)

        self.label_wpm = tk.Label(top_frame, text="WPM: ?")
        self.label_wpm.pack(side="left", padx=10)

        self.label_timer = tk.Label(top_frame, text="Time left: 1:00")
        self.label_timer.pack(side="left", padx=10)

        self.btn_start_stop = tk.Button(top_frame, text="Start")
        self.btn_start_stop.pack(side="left", padx=10)

        self.label_highscore = tk.Label(top_frame, text="Best WPM: 0 / CPM: 0")
        self.label_highscore.pack(side="left", padx=10)

        progress_frame = tk.Frame(root)
        progress_frame.pack(pady=5)
        tk.Label(progress_frame, text="Progress: ").pack(side="left")
        self.progress_var = tk.IntVar()
        self.progress_bar = ttk.Progressbar(progress_frame, orient="horizontal",
                                            length=300, mode="determinate",
                                            variable=self.progress_var)
        self.progress_bar.pack(side="left", padx=5)

        text_frame = tk.Frame(root)
        text_frame.pack()

        scrollbar = tk.Scrollbar(text_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.text_box = tk.Text(
            text_frame,
            width=60,
            height=6,
            font=("Consolas", 16),
            wrap="word",
            yscrollcommand=scrollbar.set
        )
        self.text_box.pack(side="left", fill="both", expand=True, pady=5)
        self.text_box.config(state="disabled")
        self.text_box.bind("<1>", lambda e: "break")  # 클릭해서 수정 불가
        scrollbar.config(command=self.text_box.yview)
        self.text_box.tag_configure("current_word", underline=True)

        self.entry_user = tk.Entry(root, font=("Consolas", 16), width=30)
        self.entry_user.pack(pady=10)

        self.label_result = tk.Label(root, text="", font=("Consolas", 12))
        self.label_result.pack(pady=5)

        self.time_options = [30, 60, 90]

    def get_time_limit(self) -> int:
        """콤보박스에서 선택된 시간을 int로 반환(잘못된 값이면 60)."""
        try:
            return int(self.combo_time.get())
        except ValueError:
            return 60

    def bind_start_stop(self, command):
        """Start/Stop 버튼에 대한 command 바인딩."""
        self.btn_start_stop.config(command=command)

    def bind_space(self, command):
        """엔트리에서 스페이스 입력 시 실행할 함수(Controller check_word)에 바인딩."""
        self.entry_user.bind("<space>", command)

    def show_words(self, words_list):
        """Text 위젯에 모든 단어를 출력하고, 단어별 (start, end) 인덱스를 반환."""
        self.text_box.config(state="normal")
        self.text_box.delete("1.0", tk.END)
        word_positions = []

        for w in words_list:
            start_index = self.text_box.index(tk.INSERT)
            self.text_box.insert(tk.INSERT, w + " ")
            end_index = self.text_box.index(tk.INSERT)
            word_positions.append((start_index, end_index))

        self.text_box.config(state="disabled")
        return word_positions

    def highlight_current_word(self, start, end):
        """현재 단어 범위를 밑줄 태그로 표시하고, 자동 스크롤."""
        self.text_box.config(state="normal")
        # 기존 밑줄 제거
        self.text_box.tag_remove("current_word", "1.0", tk.END)
        # 새로 밑줄 추가
        self.text_box.tag_add("current_word", start, end)
        self.text_box.see(start)
        self.text_box.config(state="disabled")

    def clear_entry(self):
        self.entry_user.delete(0, tk.END)

    def focus_entry(self):
        self.entry_user.focus_set()

    def set_progressbar_max(self, maximum: int):
        """Progressbar의 최대값 설정."""
        self.progress_bar.config(maximum=maximum)
        self.progress_var.set(0)

    def update_progress(self, value: int):
        """Progressbar 값 갱신."""
        self.progress_var.set(value)

    def update_timer_label(self, time_left: int):
        """남은 시간을 mm:ss 형태로 표시."""
        mm = time_left // 60
        ss = time_left % 60
        time_str = f"{mm}:{ss:02d}"
        self.label_timer.config(text=f"Time left: {time_str}")

    def update_cpm_wpm_labels(self, cpm: int, wpm: int):
        """CPM, WPM 라벨 업데이트."""
        self.label_cpm.config(text=f"CPM: {cpm}")
        self.label_wpm.config(text=f"WPM: {wpm}")

    def update_highscore_label(self, cpm: int, wpm: int):
        """최고 기록 라벨 업데이트."""
        self.label_highscore.config(text=f"Best WPM: {wpm} / CPM: {cpm}")

    def update_result_label(self, text: str):
        self.label_result.config(text=text)

    def set_button_text(self, text: str):
        self.btn_start_stop.config(text=text)

    def disable_entry(self):
        self.entry_user.config(state="disabled")

    def enable_entry(self):
        self.entry_user.config(state="normal")

    def show_result_popup(self, message: str):
        messagebox.showinfo("결과", message)


class TypingTestController:
    """
    Model과 View를 연결하고, 이벤트(시작/중단/스페이스 등)를 처리.
    """

    def __init__(self, model: TypingTestModel, view: TypingTestView):
        self.model = model
        self.view = view

        self.word_positions = []

        self.view.bind_start_stop(self.toggle_test)
        self.view.bind_space(self.check_word)

        self.timer_job = None

    def toggle_test(self):
        """시작 / 중단 버튼을 누르면 실행"""
        if self.model.is_testing:
            self.end_test()
        else:
            self.start_test()

    def start_test(self):
        """테스트를 시작"""
        time_limit = self.view.get_time_limit()
        self.model.reset_test(time_limit)

        self.view.set_button_text("Stop")
        self.view.enable_entry()
        self.view.clear_entry()
        self.view.focus_entry()

        self.word_positions = self.view.show_words(self.model.words_list)

        if self.word_positions:
            start, end = self.word_positions[self.model.current_word_index]
            self.view.highlight_current_word(start, end)

        self.view.set_progressbar_max(len(self.model.words_list))

        self.view.update_result_label("")
        self.update_timer()

    def end_test(self):
        """테스트 종료 로직"""
        if not self.model.is_testing:
            return

        self.model.end_test()
        self.view.set_button_text("Start")
        if self.timer_job:
            self.view.root.after_cancel(self.timer_job)

        self.view.disable_entry()

        cpm, wpm = self.model.compute_stats()
        self.model.update_highscore(cpm, wpm)
        self.view.update_cpm_wpm_labels(cpm, wpm)
        self.view.update_highscore_label(self.model.highest_cpm, self.model.highest_wpm)

        elapsed_time = int(time.time() - self.model.start_time)
        result_text = (
            f"정확히 입력한 단어 수: {self.model.correct_words}\n"
            f"정확히 입력한 글자 수: {self.model.correct_letters}\n"
            f"소요 시간: {elapsed_time}초"
        )
        self.view.update_result_label(result_text)

        popup_message = (
            f"테스트 종료!\n\n"
            f"정확히 입력한 단어 수: {self.model.correct_words}\n"
            f"정확히 입력한 글자 수: {self.model.correct_letters}\n"
            f"WPM: {wpm}, CPM: {cpm}\n"
            f"소요 시간: {elapsed_time}초\n\n"
            f"최고 기록 => WPM: {self.model.highest_wpm}, CPM: {self.model.highest_cpm}"
        )
        self.view.show_result_popup(popup_message)

    def check_word(self, event):
        """Entry에서 스페이스를 누르면 현재 단어와 비교"""
        if not self.model.is_testing:
            return "break"

        typed = self.view.entry_user.get().strip()
        current_word = self.model.words_list[self.model.current_word_index]

        if typed == current_word:
            self.model.correct_words += 1
            self.model.correct_letters += len(current_word)

        self.model.current_word_index += 1
        self.view.clear_entry()

        self.view.update_progress(self.model.current_word_index)

        if self.model.current_word_index >= len(self.model.words_list):
            self.end_test()
            return "break"

        start, end = self.word_positions[self.model.current_word_index]
        self.view.highlight_current_word(start, end)

        return "break"

    def update_timer(self):
        """1초마다 남은 시간 갱신"""
        if self.model.is_testing:
            self.model.time_left -= 1
            if self.model.time_left < 0:
                self.end_test()
                return

            self.view.update_timer_label(self.model.time_left)

            cpm, wpm = self.model.compute_stats()
            self.view.update_cpm_wpm_labels(cpm, wpm)

            self.timer_job = self.view.root.after(1000, self.update_timer)


def main():
    root = tk.Tk()

    model = TypingTestModel()
    view = TypingTestView(root)
    controller = TypingTestController(model, view)

    root.mainloop()


if __name__ == "__main__":
    main()
