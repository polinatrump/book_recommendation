from src.entrypoints.app import ApplicationEntryPoint
from warnings import simplefilter

if __name__ == '__main__':
    simplefilter('ignore', RuntimeWarning)
    ApplicationEntryPoint.start()



# Result without threads/ processes: 1300
# Result 10 Processes: 200
# Result 5 Processes: 287, 500, 263
# Database + process pool: 74 sec
