#this file is use when think fixtuue can be use to across the multiple pages)
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        #"--cmdopt", action="store", default="type1", help="my option: type1 or type2" (syntax :cmdopt is keyname default is value)
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        #driver=webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver-win64\\chromedriver.exe')  (deprecated this code)
        driver=webdriver.Chrome(service=Service(r"C:\Users\prerna.jain\Downloads\MyDrivers\chromedriver-win64\chromedriver.exe"))
        print(driver," Invoke the Chrome Browser")
    elif browser_name == "firefox":
        #driver=webdriver.Edge(service=Service('C:\\Users\\prerna.jain\\Downloads\\MyDrivers\\edgedriver_win64\\msedgedriver.exe'))
        driver = webdriver.Edge(service=Service("C:\\Users\\prerna.jain\\Downloads\\MyDrivers\\edgedriver_win64\\msedgedriver.exe"))
        print(driver ," Invoke the Edge Browser")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed a screenshot in the HTML report whenever a test fails.
#     :param item:
#     """

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
    report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)







# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#         """
#             Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#             :param item:
#             """
#         pytest_html=item.config.pluginmanager.getplugin('html')
#         outcome = yield
#         report = outcome.get_result()
#         extra=getattr(report, 'extra', [])
#
#         if report.when == 'call' or report.when == "setup":
#             xfail = hasattr(report, 'wasxfail')
#             if (report.skipped and xfail) or (report.failed and not xfail):
#                 file_name=report.nodeid.replace("::", "_") + ".png"
#                 _capture_screenshot(file_name)
#                 if file_name:
#                     html='<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                          'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                     extra.append(pytest_html.extras.html(html))
#       report.extra=extra
#
#  def _capture_screenshot(name):
#  driver.get_screenshot_as_file(name)



