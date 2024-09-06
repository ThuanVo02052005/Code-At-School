# Lớp tín hiệu rời rạc với định nghĩa như [1]
from bài_1 import *
class DiscreteSignalWithDefinition(DiscreteSignal):
    def __init__(self, amplitude, frequency, period, wavelength):
        super().__init__(amplitude, frequency, period, wavelength)

    def calculate_discrete_signal(self, n):
        result = 0
        for k in range(n + 1):
            result += self.amplitude * self.delta_function(n - k)
        return result

    def delta_function(self, n):
        return 1 if n == 0 else 0

# Lớp Radar phân tích tín hiệu với mẫu tín hiệu rời rạc như [2]
class Radar:
    def analyze_signal(self, n):
        signal = [0] * 16
        for i in range(16):
            signal[i] = (1 - i / 15) if 0 <= i <= 15 else 0
        return signal

    def print_signal(self, signal):
        print(" ".join(map(str, signal)))

# Sử dụng các đối tượng vừa tạo
if __name__ == "__main__":
    discrete_signal = DiscreteSignalWithDefinition(1.0, 1.0, 1.0, 1.0)
    radar = Radar()
    signal = radar.analyze_signal(4)
    radar.print_signal(signal)
