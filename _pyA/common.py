import logging


def configur_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='[%(asctime)s.%(msecs)03d] %(module)-5s : %(lineno)-3d %(levelname)-7s - %(message)s'
    )

    


    