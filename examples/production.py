from examples.service import Service
from hexalog.adapters.struct_logger import StructLogger


def main():
    logger = StructLogger()
    service = Service(logger)
    service.do_something()


if __name__ == "__main__":
    main()
