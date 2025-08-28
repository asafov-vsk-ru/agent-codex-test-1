from core.ui.pages.base_page import BasePage


class VskMainPage(BasePage):

    _url: str = "https://www.stage.vsk.ru/klientam"
    _title: str = "ВСК"

    # Accept cookie panel (Header)
    vsk_cookie_panel: str = "//vsk-cookie-panel[@class='ng-star-inserted']"
    vsk_cookie_span: str = "//span[@class='text']/text='Чтобы улучшить работу сайта, мы используем файлы cookie.'"
    vsk_cookie_button: str = "//div[@class='accept-button']/text='Принимаю'"
    vsk_cookie_link: str = "//a[@class='link-text ng-star-inserted']/text='Подробнее тут.'"
    vsk_cookie_img: str = "/img[@alt='Картинка для панели принятия cookies']"

    # Logo main page (Header)
    vsk_logo: str = "//img[@alt='Header VSK logo']"

    # Left header menu (Header)
    vsk_header_top_nav: str = "//nav[@class='header-top-nav']"
    vsk_header_menu_client_item: str = "//ui/li[@routerlinkactive='header-nav-item-active']/a/text='Клиентам' href='/klientam'"
    vsk_header_menu_vip_item: str = "//ui/li[@routerlinkactive='header-nav-item-active']/a/text='VIP' href='/vip'"
    vsk_header_menu_business_item: str = "//ui/li[@routerlinkactive='header-nav-item-active']/a/text='Бизнесу' href='/biznesu'"
    vsk_header_menu_career_item: str = "//ui/li[@routerlinkactive='header-nav-item-active']/a/text='Карьера' href='/klientam/karyera'"
    vsk_header_menu_offices_item: str = "//ui/li[@routerlinkactive='header-nav-item-active']/a/text='Офисы' href='/klientam/offices'"

    # Right header menu (Header)
    vsk_header_top_buttons: str = "//div[@class='header-top-buttons']"
    vsk_agents_button: str = "//a[@id='header-agents-button']"
    vsk_defer_offscreen_load: str = "//vsk-defer-offscreen-load/div/span[@class='ng-star-inserted']/path"
    vsk_authorization_dropdown_menu: str = "//vsk-authorization-dropdown-menu/a[@id='login-header-button']/text=' Войти '"

    # Navigation header menu (Header)
    vsk_header_bottom_nav: str = "//nav[@class='header-bottom-nav']"
    vsk_nav_menu_health_item: str = "//nav/li[@id='health']/a/text='Здоровье'"
    vsk_nav_menu_auto_item: str = "//nav/li[@id='auto']/a/text='Авто'"
    vsk_nav_menu_travels_item: str = "//nav/li[@id='travels']/a/text='Путешествия'"
    vsk_nav_menu_property_item: str = "//nav/li[@id='property']/a/text='Имущество'"
    vsk_nav_menu_mortgage_item: str = "//nav/li[@id='mortgage']/a/text='Ипотека'"
    vsk_insurance_btn_dialog: str = "//vsk-insurance-btn-dialog[@class='ng-star-inserted']/button[@id='header-insurance-button']"
    vsk_insurance_btn_dialog_text: str = "//vsk-insurance-btn-dialog[@class='ng-star-inserted']/button[@id='header-insurance-button']/span/text='Страховой случай'"

    # Call back widgets (Header)
    vsk_insurance_btn_dialog: str = "//vsk-insurance-btn-dialog/button[@id='header-insurance-button']/span/text='Страховой случай'"
    vsk_call_back_panel: str = "//vsk-call-back-panel/div/vsk-call-back/button/span/text='Заказать звонок'"

    # Banner (Body)
    vsk_carousel_container: str = "//section[@class='container block-banner custom-background ng-star-inserted']/div/vsk-carousel-container-arrow"
    vsk_carousel_left_button: str = "//button[@class='arrow-button arrow-button-left']"
    vsk_carousel_content: str = "//tui-carousel[@class='carousel _transitioned']/div/div/div"
    vsk_carousel_content_button: str = "//a[@class='vsk-text-22-bold banner-link ng-star-inserted']"
    vsk_carousel_content_label: str = "//div[@class='title-text']/text='Приложение ГТО'"
    vsk_carousel_content_text: str = "//div[@class='banner-price ng-star-inserted']/text='Тренируйся и побеждай'"
    vsk_carousel_content_img: str = "//div[@class='banner-data ng-star-inserted']/img"
    vsk_carousel_right_button: str = "//button[@class='arrow-button']"

    # Main (Body)
    vsk_block_main: str = "//vsk-block-main/div[@class='personal ng-star-inserted']"
    vsk_block_main_title: str = "//vsk-block-main/div[@class='personal ng-star-inserted']/h1/text='Главное'"
    vsk_tui_button_buy: str = "//button[@id='main_tab_buy']"
    vsk_tui_button_prolong: str = "//button[@id='main_tab_prolong']"
    vsk_tui_button_pay: str = "//button[@id='main_tab_pay']"
    vsk_tui_button_claim: str = "//button[@id='main_tab_claim']"
    vsk_tui_button_request_status: str = "//button[@id='main_tab_request_status']"
    vsk_product_line_card: str = "//vsk-product-line-card[@class='product-line-card ng-star-inserted']/div"
    vsk_product_line_card_link: str = "//a[@class='title ng-star-inserted']"
    vsk_product_line_card_title: str = "//a[@class='title ng-star-inserted']/h2/text='Здоровье'"
    vsk_product_line_card_item: str = "//vsk-product-line-item[@class='list-item ng-star-inserted']/div"
    vsk_product_line_card_item_link: str = "//a[@class='product-link ng-star-inserted']"
    vsk_product_line_card_item_name: str = "//span[@class='name-container ng-star-inserted']/span[@class='product-name']/text='Медицина без границ'"
    vsk_product_line_card_item_value: str = "//span[@class='product-price ng-star-inserted']/span/text='от 12 661 ₽'"

    # Happens (Body)
    vsk_insurance_case_block: str = "//vsk-insurance-case-block/div[@class='insurance-case']"
    vsk_insurance_case_block_title: str = "//vsk-insurance-case-block/div[@class='insurance-case']/h2/text='Случилось!'"
    vsk_insurance_case_big_card: str = "//vsk-insurance-case-big-card"
    vsk_insurance_case_big_card_link: str = "//a[@class='accident_block_main']"
    vsk_insurance_case_big_card_link_text: str = "//a[@class='accident_block_main']/h3/text='Произошёл страховой случай'"
    vsk_insurance_case_big_card_link_button: str = "//a[@class='accident_block_main']/div/text='Заявить'"
    vsk_insurance_case_small_card: str = "//vsk-insurance-case-small-card"
    vsk_insurance_case_small_card_link: str = "//vsk-insurance-case-small-card/a"
    vsk_insurance_case_small_card_link_text: str = "//vsk-insurance-case-small-card/a/h3/text='Хочу узнать порядок действий при страховом случае'"
    vsk_insurance_case_small_card_link_button: str = "//vsk-insurance-case-small-card/a/div/span/text='Перейти'"

    # Nearest office (Body)
    vsk_block_nearest_office: str = "//vsk-block-nearest-office"
    vsk_block_nearest_office_title: str = "//vsk-block-nearest-office/div/h2/text=' Ближайший офис '"
    vsk_city_info_container: str = "//vsk-city-info/div[@class='city-info-container']"
    vsk_city_info_current_city: str = "//span[@class='city-info']/span/span/text='Москва'"
    vsk_city_info_count_offices: str = "//span[@class='city-info']/span/text=' 56 офисов в городе '"
    vsk_city_info_geolocation_button: str = "//span[@id='geolocation-button']/span/text='Определить моё местоположение'"
    vsk_city_info_all_office_link: str = "//a[@id='all-officies-link']/text=' Все офисы '"
    vsk_office_info_name: str = "//vsk-office-info/div/div/div/div/text='ул. Новый Арбат д. 21'"
    vsk_office_info_map: str = "//div[@class='map']/ya-map/div"
    vsk_office_info_schedule: str = "//vsk-office-schedule/div"
    vsk_office_info_schedule_day_indicators: str = "//div[@class='day-indicators']"
    vsk_office_info_schedule_weekdays: str = "//div[@class='weekdays']"
    vsk_office_info_schedule_weekends: str = "//div[@class='weekends ng-star-inserted']"
    vsk_office_info_schedule_phones: str = "//div[@class='phones ng-star-inserted']"

    # Mobile banner (Body)
    vsk_main_mobile_app_block: str = "//vsk-main-mobile-app-block"

    # Media centre (Body)
    vsk_block_media_center: str = "//vsk-block-media-center/div"
    vsk_block_media_center_title: str = "//vsk-block-media-center/div/h2/text=' Медиацентр '"
    vsk_tui_button_publication: str = "//button[@id='media_tab_publications']"
    vsk_tui_button_search: str = "//button[@id='media_tab_vskali']"
    vsk_tui_button_press: str = "//button[@id='media_tab_presscenter']"
    vsk_tui_button_blog: str = "//button[@id='media_tab_blog']"
    vsk_block_media_center_card: str = "//fieldset[@class='t-item ng-star-inserted']/div/div/div"

    # Survey (Footer)
    vsk_footer: str = "//vsk-footer/footer"
    vsk_oprosso_widget: str = "//vsk-oprosso-widget/div/div/div/text=' Информация на этой странице была для вас полезной? '"
    vsk_oprosso_link: str = "//vsk-oprosso-widget/div/div/a[@class='oprosso-widget oprosso-widgetPollChannel']/text='Пройти опрос '"

    # Footer navigation menu (Footer) vsk-footer footer section vsk-footer-links-columns-section
    vsk_footer_information_section: str = "//vsk-footer-links-columns-section/div/div[@class='section-title h6-bold']/text=' Информация '"
    vsk_footer_links_column: str = "//vsk-footer-links-column[@class='links-list-column-item']"
    vsk_footer_about_link: str = "//vsk-footer-link/div/a[@href='/o-kompanii']/text=' О компании '"
    vsk_footer_career_link: str = "//vsk-footer-link/div/a[@href='/klientam/karyera']/text=' Карьера '"
    vsk_footer_provider_link: str = "//vsk-footer-link/div/a[@href='/o-kompanii/postavshchikam']/text=' Поставщикам '"
    vsk_footer_smi_link: str = "//vsk-footer-link/div/a[@href='/o-kompanii/dlya-smi']/text=' Для СМИ '"
    vsk_external_loyalty_link: str = "//vsk-external-link/div/a[@href='https://svoi.club/']/span/text=' Программа лояльности СВОИ '"
    vsk_footer_client_link: str = "//vsk-footer-link/div/a[@href='/klientam/offices']/text=' Офисы '"
    vsk_external_franchise_link: str = "//vsk-external-link/div/a[@href='https://fr.vsk.ru/']/span/text=' Франшиза '"
    vsk_footer_sitemap_link: str = "//vsk-footer-link/div/a[@href='/site-map']/text=' Карта сайта '"

    vsk_footer_design_section: str = "//vsk-footer-links-columns-section/div/div[@class='section-title h6-bold']/text=' Оформить '"
    vsk_footer_auto_link: str = "//vsk-footer-link/div/a[@href='/klientam/avto']/text=' Авто '"
    vsk_footer_travel_link: str = "//vsk-footer-link/div/a[@href='/klientam/puteshestviya']/text=' Путешествия '"
    vsk_footer_health_link: str = "//vsk-footer-link/div/a[@href='/klientam/zdorove']/text=' Здоровье '"
    vsk_footer_property_link: str = "//vsk-footer-link/div/a[@href='/klientam/imuschestvo']/text=' Имущество '"
    vsk_footer_mortgage_link: str = "//vsk-footer-link/div/a[@href='/klientam/ipoteka']/text=' Ипотека '"
    vsk_external_investments_link: str = "//vsk-external-link/div/a[@href='https://vsklife.ru/']/span/text=' Инвестиции '"

    vsk_footer_declare_section: str = "//vsk-footer-links-columns-section/div/div[@class='section-title h6-bold']/text=' Заявить '"
    vsk_footer_happening_link: str = "//vsk-footer-link/div/a[@href='/klientam/strahovoy-sluchay']/text=' Страховой случай '"
    vsk_footer_for_client_link: str = "//vsk-footer-link/div/a[@href='/o-kompanii/dlya-kliyentov']/text=' Для клиентов '"
    vsk_footer_contact_link: str = "//vsk-footer-link/div/a[@href='/klientam/svyazatsya-s-nami']/text=' Связаться с нами '"

    vsk_footer_more_section: str = "//vsk-footer-links-columns-section/div/div[@class='section-title h6-bold']/text=' Ещё '"
    vsk_footer_disclosure_information_link: str = "//vsk-footer-link/div/a[@href='/o-kompanii/raskrytie-informacii']/text=' Раскрытие информации '"
    vsk_footer_personal_information_link: str = "//vsk-footer-link/div/a[@href='/o-kompanii/dlya-kliyentov?t=personalpolicy&case=personalpolicy']/text=' Политика персональных данных '"
    vsk_footer_pretrial_link: str = "//vsk-footer-link/div/a[@href='/klientam/pre-trial']/text=' Информация о взыскании '"

    vsk_footer_media_section: str = "//vsk-footer-links-columns-section/div/div[@class='section-title h6-bold']/text=' Медиацентр '"
    vsk_footer_news_link: str = "//vsk-footer-link/div/a[@href='/o-kompanii/novosti']/text=' Пресс-центр '"
    vsk_external_yousearch_link: str = "//vsk-external-link/div/a[@href='https://vskali.ru/']/span/text=' ВыИскали '"
    vsk_footer_blog_link: str = "//vsk-footer-link/div/a[@href='/o-kompanii/blog']/text=' Блог '"

    vsk_footer_social_section: str = "//vsk-footer-links-columns-section/div/div[@class='section-title h6-bold']/text=' Социальные сети '"
    vsk_external_icon_vk_link: str = "//vsk-external-icon-link/a[@href='https://vk.com/vsk.insurance']"
    vsk_external_icon_dzen_link: str = "//vsk-external-icon-link/a[@href='https://zen.yandex.ru/vsk']"
    vsk_external_icon_ok_link: str = "//vsk-external-icon-link/a[@href='https://ok.ru/vskinsurance']"
    vsk_external_icon_youtube_link: str = "//vsk-external-icon-link/a[@href='https://www.youtube.com/user/vsktv']"
    vsk_external_icon_telegram_link: str = "//vsk-external-icon-link/a[@href='https://t.me/vskinsur']"
    vsk_external_icon_whatsapp_link: str = "//vsk-external-icon-link/a[@href='https://api.whatsapp.com/send/?phone=79175204537&text&type=phone_number&app_absent=0']"

    # Phone section (Footer)
    vsk_local_phone: str = "//a[@id='local-phone-button']/span/text='8 800 775-15-75'"
    vsk_local_phone_comment: str = "//div[@class='address']/span/text='Круглосуточно'"
    vsk_international_phone: str = "//a[@id='international-phone-button']/span/text='+7 (495) 009-15-75'"
    vsk_international_phone_comment: str = "//div[@class='address ng-star-inserted']/span/text='Для звонков из-за рубежа'"
    vsk_language_button: str = "//div[@class='tui-autofill']/input"
    vsk_language_button_label: str = "//div[@class='language-value ng-star-inserted']/div/text='Русский'"
    vsk_version_visually_impaired_button: str = "//div[@class='t-wrapper']/span/text=' Для слабовидящих '"
    vsk_apple_app_link: str = "//a[@id='app_store_link' @href='https://apps.apple.com/ru/app/вск-страхование/id1241282589']"
    vsk_google_app_link: str = "//a[@id='google_play_link' @href='https://play.google.com/store/apps/details?id=ru.vsk.insurance&hl=ru']"
    vsk_gallery_app_link: str = "//a[@id='app_gallery_link' @href='https://appgallery.cloud.huawei.com/ag/n/app/C105817713?locale=ru_RU&source=shop.vsk.ru&subsource=C105817713&shareFrom=appmarket']"

    # Copyright section (Footer)
    vsk_copyright_footer_section: str = "//section[@class='copyright-section ng-star-inserted']/div/p/text='© 1992–2024 Страховое акционерное общество «ВСК» Россия, Москва, 121552, ул. Островная, 4'"
