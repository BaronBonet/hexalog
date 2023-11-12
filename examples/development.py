from examples.service import Service
from hexalog.adapters.cli_logger import ColorfulCLILogger


def main():
    logger = ColorfulCLILogger()
    service = Service(logger)
    service.do_something()


if __name__ == "__main__":
    main()
