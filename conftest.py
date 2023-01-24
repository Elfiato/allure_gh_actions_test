import shutil
import logging
import os

import allure

from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')
    # parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')
    parser.addoption('--url', default=f'https://ya.ru/')


@pytest.fixture(scope='function')
def temp_dir(request):
    test_name = '_'.join(request._pyfuncitem.nodeid.split(':'))
    test_dir = os.path.join('/tmp/tests', test_name)
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    # debug_log = request.config.getoption('--debug_log')
    headless = request.config.getoption('--headless')
    allure_dir = request.config.getoption('--alluredir')
    if request.config.getoption('--selenoid'):
        vnc = request.config.getoption('--vnc')
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False
    return {
        'url': url,
        # 'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
        'headless': headless,
        'alluredir': allure_dir
    }


@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    # log_level = logging.DEBUG if config['debug_log'] else logging.INFO
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


@pytest.fixture(scope='function', autouse=True)
def report(request, temp_dir):
    failed_test_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_test_count:
        test_log = os.path.join(temp_dir, 'test.log')
        with open(test_log, 'r') as f:
            allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)
