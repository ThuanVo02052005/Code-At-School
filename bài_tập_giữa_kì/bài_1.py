from abc import ABC, abstractmethod

# Giao diện tín hiệu
class Signal(ABC):
    @abstractmethod
    def get_amplitude(self):
        pass

    @abstractmethod
    def get_frequency(self):
        pass

    @abstractmethod
    def get_period(self):
        pass

    @abstractmethod
    def get_wavelength(self):
        pass

# Lớp tín hiệu rời rạc
class DiscreteSignal(Signal):
    def __init__(self, amplitude, frequency, period, wavelength):
        self.amplitude = amplitude
        self.frequency = frequency
        self.period = period
        self.wavelength = wavelength

    def get_amplitude(self):
        return self.amplitude

    def get_frequency(self):
        return self.frequency

    def get_period(self):
        return self.period

    def get_wavelength(self):
        return self.wavelength

# Lớp tín hiệu liên tục
class ContinuousSignal(Signal):
    def __init__(self, amplitude, frequency, period, wavelength):
        self.amplitude = amplitude
        self.frequency = frequency
        self.period = period
        self.wavelength = wavelength

    def get_amplitude(self):
        return self.amplitude

    def get_frequency(self):
        return self.frequency

    def get_period(self):
        return self.period

    def get_wavelength(self):
        return self.wavelength
