import numpy as np

class MultiKernelDevice:
    def __init__(self, ker_size):
        self.ker_size = ker_size
        self.kernels = []

    def _find_best_match_for_patch(self, input_patch):
        if len(self.kernels) == 0:
            return False
        best_match_score = None
        best_kernel_id = None
        for i in range(len(self.kernels)):
            kernel = self.kernels[i]
            diff = self._compare_kenel_and_patch(kernel, input_patch)
            if best_match_score is None:
                best_match_score = diff
                best_kernel_id = i
            else:
                if diff < best_match_score:
                    best_match_score = diff
                    best_kernel_id = i
        return best_match_score, best_kernel_id


    def _compare_kenel_and_patch(self, kernel, patch):
        return np.linalg.norm(kernel-patch)

    def find_best_in_vicinity(self, coord, vicinity, signal):
        best_u = None
        best_kernel_id = None
        best_score = None
        for u in range(-vicinity, vicinity):
            start = coord + u
            if start < 0 or start > len(signal) - 1 - self.ker_size:
                continue
            patch = signal[start:start+self.ker_size]
            u_best_match_score, u_best_kernel_id = self._find_best_match_for_patch(patch)
            if best_u is None:
                best_u = u
                best_kernel_id = u_best_kernel_id
                best_score = u_best_match_score
            else:
                if u_best_match_score < best_score:
                    best_u = u
                    best_kernel_id = u_best_kernel_id
                    best_score = u_best_match_score
        return best_u, best_kernel_id, best_score


