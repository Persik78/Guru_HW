from selene import browser, be, have
from selene.core.query import screenshot
from selenium.webdriver.common.bidi.cdp import devtools


def testHw5():
    browser.open('/automation-practice-form')
    #browser.all('div.userName-wrapper>div').should(have.size(3))

    browser.element('#firstName').type('Diana')
    browser.element('#lastName').type('Degtyareva')
    browser.element('#userEmail').type('swertyxadadw@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').type('1234567890')
    browser.element('[id="subjectsInput"]').type('1234')
    browser.element('[id="hobbies-checkbox-3"]').press()
    browser.element('[id="hobbies-checkbox-1"]').press()
    browser.element('[id="hobbies-checkbox-2"]').press()
    browser.element('[id="hobbies-checkbox-1"]').press()
    browser.element('[id="hobbies-checkbox-2"]').press()
    browser.element('[id="currentAddress"]').type('Volzsky, olomoytczkaya')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="1"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="2004"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--019"]').click()
    browser.element('[id="submit"]').click()
    browser.element()
    browser.element('[id="closeLargeModal"]').press()