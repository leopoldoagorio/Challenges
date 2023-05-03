from mydatalib import DataCapture

if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)

    stats = capture.build_stats()
    print(stats.less(4))
    print(stats.between(3,6))
    print(stats.greater(4))
#     print('Hi Montevideo')
#     capture = DataCapture()
#     capture.add(1)
#     capture.add(1)
#     capture.add(1)
#     capture.add(2)
#     capture.add(3)
#     capture.add(3)
#     capture.add(9)
#     capture.add(9)
#     capture.add(9)
#     capture.add(9)
#     capture.add(9)
#     print(capture.time_series)
#     stats = capture.build_stats()
#     print(stats.freqs)
#     print(stats.csum)
#     print_hi('PyCharm')