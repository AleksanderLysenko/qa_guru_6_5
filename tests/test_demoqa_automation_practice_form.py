import os

from selene import be, have
from selene.support.shared import browser


def test_hard(browser_size):
    # fill form
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Lys')
    browser.element('#userEmail').type('example@yandex.ru')
    browser.element('.custom-radio [for=gender-radio-1]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__year-select"]').click().type("1992").click()
    browser.element('[class="react-datepicker__month-select"]').click().type("January").click()
    browser.element('[aria-label="Choose Sunday, January 5th, 1992"]').click()
    browser.element('#subjectsInput').type('economics').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath("images/Skrik.jpg"))
    browser.element('#currentAddress').type('godovikova 9')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').should(be.visible).press_enter()

    # check form
    browser.element('[class="modal-title h4"]').should(have.text('Thanks for submitting the form'))
    browser.all('.modal-body tr th')[0].should(have.exact_text('Label'))
    browser.all('.modal-body tr th')[1].should(have.text('Values'))
    browser.all('.modal-body tr td')[1].should(have.text('Alex Lys'))
    browser.all('.modal-body tr td')[3].should(have.text('example@yandex.ru'))
    browser.all('.modal-body tr td')[5].should(have.exact_text('Male'))
    browser.all('.modal-body tr td')[7].should(have.text('1234567890'))
    browser.all('.modal-body tr td')[9].should(have.text('05 January,1992'))
    browser.all('.modal-body tr td')[11].should(have.text('Economics'))
    browser.all('.modal-body tr td')[13].should(have.text('Sports, Music'))
    browser.all('.modal-body tr td')[15].should(have.text('Skrik.jpg'))
    browser.all('.modal-body tr td')[17].should(have.text('godovikova 9'))
    browser.all('.modal-body tr td')[19].should(have.text('NCR Delhi'))
    