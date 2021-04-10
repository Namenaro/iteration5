class MultiKernelDevice:
    def __init__(self, max_distance, ker_size):
        self.ker_size = ker_size
        self.max_distance = max_distance

        self.kernels = []

    def _try_recognize(self, input_patch):
        # возвращаем бинарный результат распознавания: если входные
        # данные оказались достаточно похожи хоть на одно ядро, то
        # возвращаем истину. Иначе ложь.
        if len(self.kernels) == 0:
            return False
        for kernel in self.kernels:
            diff = self._compare_kenel_and_patch(kernel, input_patch)
            if diff < self.max_distance:
               return True
        return False

    def _compare_kenel_and_patch(self, kernel, patch):
        # здесь реализуем какой-то способ померить непохожесть данных (патч) и эталона (кернел)
        # функция возвращает какой-то неотрицательное число "непохожесть". Чем оно больше,
        # тем хуже. Ноль значит полное совпадение (идеальное).
        pass

    def try_recognize_region(self, region):
        # прикладываем каждое из ядер к каждому из возможных патчей в регионе до
        # тех пор, пока не случится хорошего попадания. Если хорошего попадания
        # не случается, то возвращаем отрицательное число. Если попаданий несколько,
        # то возвращаем управление, приводящее к наилучшему попаданию в образец.

        for i in range(0, len(region) - self.ker_size):
            region_patch = region[i:i+self.ker_size]
            if self._try_recognize(region_patch):
                return i
        return -1

    def add_new_kernel(self, region):
        pass