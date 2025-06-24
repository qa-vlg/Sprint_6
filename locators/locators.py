from selenium.webdriver.common.by import By

class Locators:
    # домашняя страница
    YANDEX_HOME_BUTTON = (By.XPATH, ".//img[@src='/assets/ya.svg' and @alt='Yandex']")
    DZEN_LOGO = (By.XPATH, ".//*[@class='dzen-layout--desktop-base-header__logoLink-2h']")
    SCOOTER_HOME_BUTTON = (By.XPATH, ".//img[@src='/assets/scooter.svg' and @alt='Scooter']")
    HOME_HEADER_TEXT = (By.XPATH, ".//div[@class='Home_Header__iJKdX' and text()='Самокат ']")
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    MID_ORDER_BUTTON = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[contains(@class, 'Button_')]")
    CKOOKIES_BUTTON = (By.XPATH, ".//button[text()='да все привыкли']")
    HOW_IT_WORKS_ELEMENTS = (By.XPATH, ".//*[@class='Home_StatusBrick__1PsW9']")

    # Заказ самоката: диалог часть 1
    FIRST_NAME_INPUT = (By.XPATH, ".//*[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and contains(@placeholder, 'Имя')]")
    LAST_NAME_INPUT = (By.XPATH, ".//*[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and contains(@placeholder, 'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, ".//*[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and contains(@placeholder, 'Адрес')]")
    SUBWAY_STATION_INPUT = (By.XPATH, ".//*[@class='select-search__input' and contains(@placeholder, 'Станция')]")
    SUBWAY_STATION_CONFIRM = (By.XPATH, ".//*[@class='select-search__row' and @data-index='0']")
    PHONE_NUMBER_INPUT = (By.XPATH, ".//*[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and contains(@placeholder, 'Телефон')]")
    BUTTON_NEXT = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")

    # Заказ самоката: диалог часть 2
    EXPECTED_DATE_INPUT = (By.XPATH, ".//*[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and contains(@placeholder, 'Когда')]")
    RENT_DURATION_OPEN_DROPDOWN = (By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    RENT_DURATION_OPTIONS = (By.XPATH, ".//div[@class='Dropdown-menu']")
    RENT_DURATION_ONE_DAY = (By.XPATH, ".//div[@class='Dropdown-option'][1]")
    COLOR_PICKER_BLACK = (By.XPATH, ".//div[@class='Order_Checkboxes__3lWSI']/label[@for='black']")
    COLOR_PICKER_GREY = (By.XPATH, ".//div[@class='Order_Checkboxes__3lWSI']/label[@for='grey']")
    COMMENTS_INPUT = (By.XPATH, ".//*[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and contains(@placeholder, 'Комментарий')]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    # Заказ самоката: подтверждение оформления заказа
    ORDER_CONFIRMATION_DIALOG = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']")
    ORDER_CONFIRMATION_DECLINE_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Нет']")
    ORDER_CONFIRMATION_ACCEPT_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")

    # Заказ самоката: заказ оформлен
    ORDER_CONFIRMED_WINDOW = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']")
    ORDER_CONFIRMATION_TEXT = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    VEW_ORDER_STATUS_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")

    # Выпадающий список в разделе Вопросы о важном
    FAQ_SECTION = (By.XPATH, ".//div[@class='Home_FourPart__1uthg'")
    FAQ_ELEMENTS_TABLE = (By.XPATH, ".//div[@class='accordion'")

    ANSWER_0_DROPDOWN = (By.XPATH, ".//div[@id='accordion__heading-0']")
    ANSWER_0_TEXT = (By.XPATH, ".//div[@id='accordion__panel-0']/p")

    ANSWER_1_DROPDOWN = (By.XPATH, ".//div[@id='accordion__heading-1']")
    ANSWER_1_TEXT = (By.XPATH, ".//div[@id='accordion__panel-1']/p")

    ANSWER_2_DROPDOWN = (By.XPATH, ".//div[@id='accordion__heading-2']")
    ANSWER_2_TEXT = (By.XPATH, ".//div[@id='accordion__panel-2']/p")

    ANSWER_3_DROPDOWN = (By.XPATH, ".//div[@id='accordion__heading-3']")
    ANSWER_3_TEXT = (By.XPATH, ".//div[@id='accordion__panel-3']/p")

    ANSWER_4_DROPDOWN = (By.XPATH, ".//div[@id='accordion__heading-4']")
    ANSWER_4_TEXT = (By.XPATH, ".//div[@id='accordion__panel-4']/p")

    ANSWER_5_DROPDOWN = (By.XPATH, ".//div[@id='accordion__heading-5']")
    ANSWER_5_TEXT = (By.XPATH, ".//div[@id='accordion__panel-5']/p")

    ANSWER_6_DROPDOWN = (By.XPATH, ".//div[@id='accordion__heading-6']")
    ANSWER_6_TEXT = (By.XPATH, ".//div[@id='accordion__panel-6']/p")

    ANSWER_7_DROPDOWN = (By.XPATH, ".//div[@id='accordion__heading-7']")
    ANSWER_7_TEXT = (By.XPATH, ".//div[@id='accordion__panel-7']/p")