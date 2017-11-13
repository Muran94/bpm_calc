import math
import re
from termcolor import colored

class BPMCalc:
    def __init__(self, original_bpm):
        self.original_bpm = original_bpm
        self.bpm_list = []

    def calc(self):
        for mul_num in [0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]:
            self.bpm_list.append(math.floor(self.original_bpm * mul_num))

    def get_result(self):
        result = """
        0.50倍速: {0:>3d}BPM
        0.75倍速: {1:>3d}BPM
        1.00倍速: {2:>3d}BPM
        1.25倍速: {3:>3d}BPM
        1.50倍速: {4:>3d}BPM
        1.75倍速: {5:>3d}BPM
        2.00倍速: {6:>3d}BPM
        """.format(
            self.bpm_list[0],
            self.bpm_list[1],
            self.bpm_list[2],
            self.bpm_list[3],
            self.bpm_list[4],
            self.bpm_list[5],
            self.bpm_list[6]
            )
        print(result)

while True:
    bpm_value = input(colored("通常速のBPMを入力してください(0 < bpm <= 300) => ", "cyan"))
    if re.match("^[1-9][0-9]{1,2}$", bpm_value):
        original_bpm = int(bpm_value)
        break
    else:
        print(colored("0 < bpm <= 300の範囲で入力してください。", "red"))

bpm_calc = BPMCalc(original_bpm)
bpm_calc.calc()
bpm_calc.get_result()
