import time
import sys
sys.path.append('C:\\Users\\mateu\Desktop\\Proyecto\\Proyecto_VLC_Alberto_Y_Mateu\\src')
from main import main


def benchmark(func, args):
    start_time = time.perf_counter()
    func(args)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    return print(run_time)


if __name__ == "__main__":
    benchmark(main, "C:\\Users\\mateu\Desktop\\Proyecto\\Proyecto_VLC_Alberto_Y_Mateu\\lib\\xml_vlc.xml")
