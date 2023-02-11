from src.entrypoints.app import ApplicationEntryPoint
from warnings import simplefilter

if __name__ == '__main__':
    simplefilter('ignore', RuntimeWarning)
    ApplicationEntryPoint.start()

