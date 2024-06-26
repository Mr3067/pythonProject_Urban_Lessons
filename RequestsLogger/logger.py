"""


"""
import logging

log_info = logging.getLogger(f'Log_INFO')
log_info.setLevel(logging.INFO)
fh_info = logging.FileHandler(
    filename='success_responses.log',
    mode='w',
    encoding='utf-8')
formatter = logging.Formatter(f'%(levelname)s:%(message)s')
fh_info.setFormatter(formatter)
log_info.addHandler(fh_info)


log_warning = logging.getLogger('Log_WARNING')
log_warning.setLevel(logging.WARNING)
fh_warning = logging.FileHandler(
    filename='bad_responses.log',
    mode='w',
    encoding='utf-8')
formatter = logging.Formatter(f'%(levelname)s:%(message)s')
fh_warning.setFormatter(formatter)
log_warning.addHandler(fh_warning)


log_error = logging.getLogger('Log_ERROR')
log_error.setLevel(logging.ERROR)
fh_error = logging.FileHandler(
    filename='blocked_responses.log',
    mode='w',
    encoding='utf-8')
formatter = logging.Formatter(f'%(levelname)s:%(message)s')
fh_error.setFormatter(formatter)
log_error.addHandler(fh_error)

