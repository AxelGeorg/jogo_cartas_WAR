import datetime


class GravaLogResultado:

    def __init__(self):
        open(r"resultadoLog.txt", "w")

    @staticmethod
    def GravaLog(linhaLog):
        with open(r"resultadoLog.txt", "a") as file:
            file.write(f"\n[{datetime.datetime.now()}] {linhaLog}")
