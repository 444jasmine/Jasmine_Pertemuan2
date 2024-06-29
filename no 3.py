class py_solution:
    def reverse_word(self, s):
        return ' '.join(reversed(s.split()))

x = input("Masukkan kalimat: ")
print(py_solution().reverse_word(x))
