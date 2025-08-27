class StandardPageFooter:
    base_locator = '//vsk-footer/footer'

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

