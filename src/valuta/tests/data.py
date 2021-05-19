__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "CURRENCY_CHOICES",
    "CURRENCY_CHOICES_SORT_BY_KEY",
    "CURRENCY_CHOICES_WITH_CODE",
    "CURRENCY_CHOICES_WITH_CODE_SORT_BY_KEY",
    "LIST_CURRENCIES_OUTPUT",
    "LIST_GENERATED_CURRENCY_MODULES",
)

LIST_CURRENCIES_OUTPUT = """
┌───────────┬──────────────────────────────────────────┐
│ ISO code  │ Currency                                 │
├───────────┼──────────────────────────────────────────┤
│ AED       │ United Arab Emirates Dirham              │
├───────────┼──────────────────────────────────────────┤
│ AFN       │ Afghan Afghani                           │
├───────────┼──────────────────────────────────────────┤
│ ALL       │ Albanian Lek                             │
├───────────┼──────────────────────────────────────────┤
│ AMD       │ Armenian Dram                            │
├───────────┼──────────────────────────────────────────┤
│ ANG       │ Netherlands Antillean Guilder            │
├───────────┼──────────────────────────────────────────┤
│ AOA       │ Angolan Kwanza                           │
├───────────┼──────────────────────────────────────────┤
│ ARS       │ Argentine Peso                           │
├───────────┼──────────────────────────────────────────┤
│ AUD       │ Australian Dollar                        │
├───────────┼──────────────────────────────────────────┤
│ AWG       │ Aruban Florin                            │
├───────────┼──────────────────────────────────────────┤
│ AZN       │ Azerbaijani Manat                        │
├───────────┼──────────────────────────────────────────┤
│ BAM       │ Bosnia-Herzegovina Convertible Mark      │
├───────────┼──────────────────────────────────────────┤
│ BBD       │ Barbadian Dollar                         │
├───────────┼──────────────────────────────────────────┤
│ BDT       │ Bangladeshi Taka                         │
├───────────┼──────────────────────────────────────────┤
│ BGN       │ Bulgarian Lev                            │
├───────────┼──────────────────────────────────────────┤
│ BHD       │ Bahraini Dinar                           │
├───────────┼──────────────────────────────────────────┤
│ BIF       │ Burundian Franc                          │
├───────────┼──────────────────────────────────────────┤
│ BMD       │ Bermudan Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ BND       │ Brunei Dollar                            │
├───────────┼──────────────────────────────────────────┤
│ BOB       │ Bolivian Boliviano                       │
├───────────┼──────────────────────────────────────────┤
│ BRL       │ Brazilian Real                           │
├───────────┼──────────────────────────────────────────┤
│ BSD       │ Bahamian Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ BTC       │ Bitcoin                                  │
├───────────┼──────────────────────────────────────────┤
│ BTN       │ Bhutanese Ngultrum                       │
├───────────┼──────────────────────────────────────────┤
│ BWP       │ Botswanan Pula                           │
├───────────┼──────────────────────────────────────────┤
│ BYN       │ Belarusian Ruble                         │
├───────────┼──────────────────────────────────────────┤
│ BZD       │ Belize Dollar                            │
├───────────┼──────────────────────────────────────────┤
│ CAD       │ Canadian Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ CDF       │ Congolese Franc                          │
├───────────┼──────────────────────────────────────────┤
│ CHF       │ Swiss Franc                              │
├───────────┼──────────────────────────────────────────┤
│ CKD       │ CKD                                      │
├───────────┼──────────────────────────────────────────┤
│ CLP       │ Chilean Peso                             │
├───────────┼──────────────────────────────────────────┤
│ CNY       │ Chinese Yuan                             │
├───────────┼──────────────────────────────────────────┤
│ COP       │ Colombian Peso                           │
├───────────┼──────────────────────────────────────────┤
│ CRC       │ Costa Rican Colón                        │
├───────────┼──────────────────────────────────────────┤
│ CUP       │ Cuban Peso                               │
├───────────┼──────────────────────────────────────────┤
│ CVE       │ Cape Verdean Escudo                      │
├───────────┼──────────────────────────────────────────┤
│ CZK       │ Czech Koruna                             │
├───────────┼──────────────────────────────────────────┤
│ DJF       │ Djiboutian Franc                         │
├───────────┼──────────────────────────────────────────┤
│ DKK       │ Danish Krone                             │
├───────────┼──────────────────────────────────────────┤
│ DOP       │ Dominican Peso                           │
├───────────┼──────────────────────────────────────────┤
│ DZD       │ Algerian Dinar                           │
├───────────┼──────────────────────────────────────────┤
│ EGP       │ Egyptian Pound                           │
├───────────┼──────────────────────────────────────────┤
│ ERN       │ Eritrean Nakfa                           │
├───────────┼──────────────────────────────────────────┤
│ ETB       │ Ethiopian Birr                           │
├───────────┼──────────────────────────────────────────┤
│ EUR       │ Euro                                     │
├───────────┼──────────────────────────────────────────┤
│ FJD       │ Fijian Dollar                            │
├───────────┼──────────────────────────────────────────┤
│ FKP       │ Falkland Islands Pound                   │
├───────────┼──────────────────────────────────────────┤
│ FOK       │ FOK                                      │
├───────────┼──────────────────────────────────────────┤
│ GBP       │ British Pound                            │
├───────────┼──────────────────────────────────────────┤
│ GEL       │ Georgian Lari                            │
├───────────┼──────────────────────────────────────────┤
│ GGP       │ GGP                                      │
├───────────┼──────────────────────────────────────────┤
│ GHS       │ Ghanaian Cedi                            │
├───────────┼──────────────────────────────────────────┤
│ GIP       │ Gibraltar Pound                          │
├───────────┼──────────────────────────────────────────┤
│ GMD       │ Gambian Dalasi                           │
├───────────┼──────────────────────────────────────────┤
│ GNF       │ Guinean Franc                            │
├───────────┼──────────────────────────────────────────┤
│ GTQ       │ Guatemalan Quetzal                       │
├───────────┼──────────────────────────────────────────┤
│ GYD       │ Guyanaese Dollar                         │
├───────────┼──────────────────────────────────────────┤
│ HKD       │ Hong Kong Dollar                         │
├───────────┼──────────────────────────────────────────┤
│ HNL       │ Honduran Lempira                         │
├───────────┼──────────────────────────────────────────┤
│ HRK       │ Croatian Kuna                            │
├───────────┼──────────────────────────────────────────┤
│ HTG       │ Haitian Gourde                           │
├───────────┼──────────────────────────────────────────┤
│ HUF       │ Hungarian Forint                         │
├───────────┼──────────────────────────────────────────┤
│ IDR       │ Indonesian Rupiah                        │
├───────────┼──────────────────────────────────────────┤
│ ILS       │ Israeli New Shekel                       │
├───────────┼──────────────────────────────────────────┤
│ IMP       │ IMP                                      │
├───────────┼──────────────────────────────────────────┤
│ INR       │ Indian Rupee                             │
├───────────┼──────────────────────────────────────────┤
│ IQD       │ Iraqi Dinar                              │
├───────────┼──────────────────────────────────────────┤
│ IRR       │ Iranian Rial                             │
├───────────┼──────────────────────────────────────────┤
│ ISK       │ Icelandic Króna                          │
├───────────┼──────────────────────────────────────────┤
│ JEP       │ JEP                                      │
├───────────┼──────────────────────────────────────────┤
│ JMD       │ Jamaican Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ JOD       │ Jordanian Dinar                          │
├───────────┼──────────────────────────────────────────┤
│ JPY       │ Japanese Yen                             │
├───────────┼──────────────────────────────────────────┤
│ KES       │ Kenyan Shilling                          │
├───────────┼──────────────────────────────────────────┤
│ KGS       │ Kyrgystani Som                           │
├───────────┼──────────────────────────────────────────┤
│ KHR       │ Cambodian Riel                           │
├───────────┼──────────────────────────────────────────┤
│ KID       │ KID                                      │
├───────────┼──────────────────────────────────────────┤
│ KMF       │ Comorian Franc                           │
├───────────┼──────────────────────────────────────────┤
│ KPW       │ North Korean Won                         │
├───────────┼──────────────────────────────────────────┤
│ KRW       │ South Korean Won                         │
├───────────┼──────────────────────────────────────────┤
│ KWD       │ Kuwaiti Dinar                            │
├───────────┼──────────────────────────────────────────┤
│ KYD       │ Cayman Islands Dollar                    │
├───────────┼──────────────────────────────────────────┤
│ KZT       │ Kazakhstani Tenge                        │
├───────────┼──────────────────────────────────────────┤
│ LAK       │ Laotian Kip                              │
├───────────┼──────────────────────────────────────────┤
│ LBP       │ Lebanese Pound                           │
├───────────┼──────────────────────────────────────────┤
│ LKR       │ Sri Lankan Rupee                         │
├───────────┼──────────────────────────────────────────┤
│ LRD       │ Liberian Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ LSL       │ Lesotho Loti                             │
├───────────┼──────────────────────────────────────────┤
│ LYD       │ Libyan Dinar                             │
├───────────┼──────────────────────────────────────────┤
│ MAD       │ Moroccan Dirham                          │
├───────────┼──────────────────────────────────────────┤
│ MDL       │ Moldovan Leu                             │
├───────────┼──────────────────────────────────────────┤
│ MGA       │ Malagasy Ariary                          │
├───────────┼──────────────────────────────────────────┤
│ MKD       │ Macedonian Denar                         │
├───────────┼──────────────────────────────────────────┤
│ MMK       │ Myanmar Kyat                             │
├───────────┼──────────────────────────────────────────┤
│ MNT       │ Mongolian Tugrik                         │
├───────────┼──────────────────────────────────────────┤
│ MOP       │ Macanese Pataca                          │
├───────────┼──────────────────────────────────────────┤
│ MRU       │ Mauritanian Ouguiya                      │
├───────────┼──────────────────────────────────────────┤
│ MUR       │ Mauritian Rupee                          │
├───────────┼──────────────────────────────────────────┤
│ MVR       │ Maldivian Rufiyaa                        │
├───────────┼──────────────────────────────────────────┤
│ MWK       │ Malawian Kwacha                          │
├───────────┼──────────────────────────────────────────┤
│ MXN       │ Mexican Peso                             │
├───────────┼──────────────────────────────────────────┤
│ MYR       │ Malaysian Ringgit                        │
├───────────┼──────────────────────────────────────────┤
│ MZN       │ Mozambican Metical                       │
├───────────┼──────────────────────────────────────────┤
│ NAD       │ Namibian Dollar                          │
├───────────┼──────────────────────────────────────────┤
│ NGN       │ Nigerian Naira                           │
├───────────┼──────────────────────────────────────────┤
│ NIO       │ Nicaraguan Córdoba                       │
├───────────┼──────────────────────────────────────────┤
│ NOK       │ Norwegian Krone                          │
├───────────┼──────────────────────────────────────────┤
│ NPR       │ Nepalese Rupee                           │
├───────────┼──────────────────────────────────────────┤
│ NZD       │ New Zealand Dollar                       │
├───────────┼──────────────────────────────────────────┤
│ OMR       │ Omani Rial                               │
├───────────┼──────────────────────────────────────────┤
│ PAB       │ Panamanian Balboa                        │
├───────────┼──────────────────────────────────────────┤
│ PEN       │ Peruvian Sol                             │
├───────────┼──────────────────────────────────────────┤
│ PGK       │ Papua New Guinean Kina                   │
├───────────┼──────────────────────────────────────────┤
│ PHP       │ Philippine Piso                          │
├───────────┼──────────────────────────────────────────┤
│ PKR       │ Pakistani Rupee                          │
├───────────┼──────────────────────────────────────────┤
│ PLN       │ Polish Zloty                             │
├───────────┼──────────────────────────────────────────┤
│ PND       │ PND                                      │
├───────────┼──────────────────────────────────────────┤
│ PRB       │ PRB                                      │
├───────────┼──────────────────────────────────────────┤
│ PYG       │ Paraguayan Guarani                       │
├───────────┼──────────────────────────────────────────┤
│ QAR       │ Qatari Rial                              │
├───────────┼──────────────────────────────────────────┤
│ RON       │ Romanian Leu                             │
├───────────┼──────────────────────────────────────────┤
│ RSD       │ Serbian Dinar                            │
├───────────┼──────────────────────────────────────────┤
│ RUB       │ Russian Ruble                            │
├───────────┼──────────────────────────────────────────┤
│ RWF       │ Rwandan Franc                            │
├───────────┼──────────────────────────────────────────┤
│ SAR       │ Saudi Riyal                              │
├───────────┼──────────────────────────────────────────┤
│ SBD       │ Solomon Islands Dollar                   │
├───────────┼──────────────────────────────────────────┤
│ SCR       │ Seychellois Rupee                        │
├───────────┼──────────────────────────────────────────┤
│ SDG       │ Sudanese Pound                           │
├───────────┼──────────────────────────────────────────┤
│ SEK       │ Swedish Krona                            │
├───────────┼──────────────────────────────────────────┤
│ SGD       │ Singapore Dollar                         │
├───────────┼──────────────────────────────────────────┤
│ SHP       │ St. Helena Pound                         │
├───────────┼──────────────────────────────────────────┤
│ SLL       │ Sierra Leonean Leone                     │
├───────────┼──────────────────────────────────────────┤
│ SLS       │ SLS                                      │
├───────────┼──────────────────────────────────────────┤
│ SOS       │ Somali Shilling                          │
├───────────┼──────────────────────────────────────────┤
│ SRD       │ Surinamese Dollar                        │
├───────────┼──────────────────────────────────────────┤
│ SSP       │ South Sudanese Pound                     │
├───────────┼──────────────────────────────────────────┤
│ STN       │ São Tomé & Príncipe Dobra                │
├───────────┼──────────────────────────────────────────┤
│ SYP       │ Syrian Pound                             │
├───────────┼──────────────────────────────────────────┤
│ SZL       │ Swazi Lilangeni                          │
├───────────┼──────────────────────────────────────────┤
│ THB       │ Thai Baht                                │
├───────────┼──────────────────────────────────────────┤
│ TJS       │ Tajikistani Somoni                       │
├───────────┼──────────────────────────────────────────┤
│ TMT       │ Turkmenistani Manat                      │
├───────────┼──────────────────────────────────────────┤
│ TND       │ Tunisian Dinar                           │
├───────────┼──────────────────────────────────────────┤
│ TOP       │ Tongan Paʻanga                           │
├───────────┼──────────────────────────────────────────┤
│ TRY       │ Turkish Lira                             │
├───────────┼──────────────────────────────────────────┤
│ TTD       │ Trinidad & Tobago Dollar                 │
├───────────┼──────────────────────────────────────────┤
│ TVD       │ TVD                                      │
├───────────┼──────────────────────────────────────────┤
│ TWD       │ New Taiwan Dollar                        │
├───────────┼──────────────────────────────────────────┤
│ TZS       │ Tanzanian Shilling                       │
├───────────┼──────────────────────────────────────────┤
│ UAH       │ Ukrainian Hryvnia                        │
├───────────┼──────────────────────────────────────────┤
│ UGX       │ Ugandan Shilling                         │
├───────────┼──────────────────────────────────────────┤
│ USD       │ US Dollar                                │
├───────────┼──────────────────────────────────────────┤
│ UYU       │ Uruguayan Peso                           │
├───────────┼──────────────────────────────────────────┤
│ UZS       │ Uzbekistani Som                          │
├───────────┼──────────────────────────────────────────┤
│ VES       │ Venezuelan Bolívar                       │
├───────────┼──────────────────────────────────────────┤
│ VND       │ Vietnamese Dong                          │
├───────────┼──────────────────────────────────────────┤
│ VUV       │ Vanuatu Vatu                             │
├───────────┼──────────────────────────────────────────┤
│ WST       │ Samoan Tala                              │
├───────────┼──────────────────────────────────────────┤
│ XAF       │ Central African CFA Franc                │
├───────────┼──────────────────────────────────────────┤
│ XCD       │ East Caribbean Dollar                    │
├───────────┼──────────────────────────────────────────┤
│ XOF       │ West African CFA Franc                   │
├───────────┼──────────────────────────────────────────┤
│ XPF       │ CFP Franc                                │
├───────────┼──────────────────────────────────────────┤
│ YER       │ Yemeni Rial                              │
├───────────┼──────────────────────────────────────────┤
│ ZAR       │ South African Rand                       │
├───────────┼──────────────────────────────────────────┤
│ ZMW       │ Zambian Kwacha                           │
├───────────┼──────────────────────────────────────────┤
│ ZWB       │ ZWB                                      │
└───────────┴──────────────────────────────────────────┘
""".strip().encode()


CURRENCY_CHOICES = [
    ("AFN", "Afghan Afghani"),
    ("ALL", "Albanian Lek"),
    ("DZD", "Algerian Dinar"),
    ("AOA", "Angolan Kwanza"),
    ("ARS", "Argentine Peso"),
    ("AMD", "Armenian Dram"),
    ("AWG", "Aruban Florin"),
    ("AUD", "Australian Dollar"),
    ("AZN", "Azerbaijani Manat"),
    ("BSD", "Bahamian Dollar"),
    ("BHD", "Bahraini Dinar"),
    ("BDT", "Bangladeshi Taka"),
    ("BBD", "Barbadian Dollar"),
    ("BYN", "Belarusian Ruble"),
    ("BZD", "Belize Dollar"),
    ("BMD", "Bermudan Dollar"),
    ("BTN", "Bhutanese Ngultrum"),
    ("BTC", "Bitcoin"),
    ("BOB", "Bolivian Boliviano"),
    ("BAM", "Bosnia-Herzegovina Convertible Mark"),
    ("BWP", "Botswanan Pula"),
    ("BRL", "Brazilian Real"),
    ("GBP", "British Pound"),
    ("BND", "Brunei Dollar"),
    ("BGN", "Bulgarian Lev"),
    ("BIF", "Burundian Franc"),
    ("XPF", "CFP Franc"),
    ("CKD", "CKD"),
    ("KHR", "Cambodian Riel"),
    ("CAD", "Canadian Dollar"),
    ("CVE", "Cape Verdean Escudo"),
    ("KYD", "Cayman Islands Dollar"),
    ("XAF", "Central African CFA Franc"),
    ("CLP", "Chilean Peso"),
    ("CNY", "Chinese Yuan"),
    ("COP", "Colombian Peso"),
    ("KMF", "Comorian Franc"),
    ("CDF", "Congolese Franc"),
    ("CRC", "Costa Rican Colón"),
    ("HRK", "Croatian Kuna"),
    ("CUP", "Cuban Peso"),
    ("CZK", "Czech Koruna"),
    ("DKK", "Danish Krone"),
    ("DJF", "Djiboutian Franc"),
    ("DOP", "Dominican Peso"),
    ("XCD", "East Caribbean Dollar"),
    ("EGP", "Egyptian Pound"),
    ("ERN", "Eritrean Nakfa"),
    ("ETB", "Ethiopian Birr"),
    ("EUR", "Euro"),
    ("FOK", "FOK"),
    ("FKP", "Falkland Islands Pound"),
    ("FJD", "Fijian Dollar"),
    ("GGP", "GGP"),
    ("GMD", "Gambian Dalasi"),
    ("GEL", "Georgian Lari"),
    ("GHS", "Ghanaian Cedi"),
    ("GIP", "Gibraltar Pound"),
    ("GTQ", "Guatemalan Quetzal"),
    ("GNF", "Guinean Franc"),
    ("GYD", "Guyanaese Dollar"),
    ("HTG", "Haitian Gourde"),
    ("HNL", "Honduran Lempira"),
    ("HKD", "Hong Kong Dollar"),
    ("HUF", "Hungarian Forint"),
    ("IMP", "IMP"),
    ("ISK", "Icelandic Króna"),
    ("INR", "Indian Rupee"),
    ("IDR", "Indonesian Rupiah"),
    ("IRR", "Iranian Rial"),
    ("IQD", "Iraqi Dinar"),
    ("ILS", "Israeli New Shekel"),
    ("JEP", "JEP"),
    ("JMD", "Jamaican Dollar"),
    ("JPY", "Japanese Yen"),
    ("JOD", "Jordanian Dinar"),
    ("KID", "KID"),
    ("KZT", "Kazakhstani Tenge"),
    ("KES", "Kenyan Shilling"),
    ("KWD", "Kuwaiti Dinar"),
    ("KGS", "Kyrgystani Som"),
    ("LAK", "Laotian Kip"),
    ("LBP", "Lebanese Pound"),
    ("LSL", "Lesotho Loti"),
    ("LRD", "Liberian Dollar"),
    ("LYD", "Libyan Dinar"),
    ("MOP", "Macanese Pataca"),
    ("MKD", "Macedonian Denar"),
    ("MGA", "Malagasy Ariary"),
    ("MWK", "Malawian Kwacha"),
    ("MYR", "Malaysian Ringgit"),
    ("MVR", "Maldivian Rufiyaa"),
    ("MRU", "Mauritanian Ouguiya"),
    ("MUR", "Mauritian Rupee"),
    ("MXN", "Mexican Peso"),
    ("MDL", "Moldovan Leu"),
    ("MNT", "Mongolian Tugrik"),
    ("MAD", "Moroccan Dirham"),
    ("MZN", "Mozambican Metical"),
    ("MMK", "Myanmar Kyat"),
    ("NAD", "Namibian Dollar"),
    ("NPR", "Nepalese Rupee"),
    ("ANG", "Netherlands Antillean Guilder"),
    ("TWD", "New Taiwan Dollar"),
    ("NZD", "New Zealand Dollar"),
    ("NIO", "Nicaraguan Córdoba"),
    ("NGN", "Nigerian Naira"),
    ("KPW", "North Korean Won"),
    ("NOK", "Norwegian Krone"),
    ("OMR", "Omani Rial"),
    ("PND", "PND"),
    ("PRB", "PRB"),
    ("PKR", "Pakistani Rupee"),
    ("PAB", "Panamanian Balboa"),
    ("PGK", "Papua New Guinean Kina"),
    ("PYG", "Paraguayan Guarani"),
    ("PEN", "Peruvian Sol"),
    ("PHP", "Philippine Piso"),
    ("PLN", "Polish Zloty"),
    ("QAR", "Qatari Rial"),
    ("RON", "Romanian Leu"),
    ("RUB", "Russian Ruble"),
    ("RWF", "Rwandan Franc"),
    ("SLS", "SLS"),
    ("WST", "Samoan Tala"),
    ("SAR", "Saudi Riyal"),
    ("RSD", "Serbian Dinar"),
    ("SCR", "Seychellois Rupee"),
    ("SLL", "Sierra Leonean Leone"),
    ("SGD", "Singapore Dollar"),
    ("SBD", "Solomon Islands Dollar"),
    ("SOS", "Somali Shilling"),
    ("ZAR", "South African Rand"),
    ("KRW", "South Korean Won"),
    ("SSP", "South Sudanese Pound"),
    ("LKR", "Sri Lankan Rupee"),
    ("SHP", "St. Helena Pound"),
    ("SDG", "Sudanese Pound"),
    ("SRD", "Surinamese Dollar"),
    ("SZL", "Swazi Lilangeni"),
    ("SEK", "Swedish Krona"),
    ("CHF", "Swiss Franc"),
    ("SYP", "Syrian Pound"),
    ("STN", "São Tomé & Príncipe Dobra"),
    ("TVD", "TVD"),
    ("TJS", "Tajikistani Somoni"),
    ("TZS", "Tanzanian Shilling"),
    ("THB", "Thai Baht"),
    ("TOP", "Tongan Paʻanga"),
    ("TTD", "Trinidad & Tobago Dollar"),
    ("TND", "Tunisian Dinar"),
    ("TRY", "Turkish Lira"),
    ("TMT", "Turkmenistani Manat"),
    ("USD", "US Dollar"),
    ("UGX", "Ugandan Shilling"),
    ("UAH", "Ukrainian Hryvnia"),
    ("AED", "United Arab Emirates Dirham"),
    ("UYU", "Uruguayan Peso"),
    ("UZS", "Uzbekistani Som"),
    ("VUV", "Vanuatu Vatu"),
    ("VES", "Venezuelan Bolívar"),
    ("VND", "Vietnamese Dong"),
    ("XOF", "West African CFA Franc"),
    ("YER", "Yemeni Rial"),
    ("ZWB", "ZWB"),
    ("ZMW", "Zambian Kwacha"),
]

CURRENCY_CHOICES_SORT_BY_KEY = [
    ("AED", "United Arab Emirates Dirham"),
    ("AFN", "Afghan Afghani"),
    ("ALL", "Albanian Lek"),
    ("AMD", "Armenian Dram"),
    ("ANG", "Netherlands Antillean Guilder"),
    ("AOA", "Angolan Kwanza"),
    ("ARS", "Argentine Peso"),
    ("AUD", "Australian Dollar"),
    ("AWG", "Aruban Florin"),
    ("AZN", "Azerbaijani Manat"),
    ("BAM", "Bosnia-Herzegovina Convertible Mark"),
    ("BBD", "Barbadian Dollar"),
    ("BDT", "Bangladeshi Taka"),
    ("BGN", "Bulgarian Lev"),
    ("BHD", "Bahraini Dinar"),
    ("BIF", "Burundian Franc"),
    ("BMD", "Bermudan Dollar"),
    ("BND", "Brunei Dollar"),
    ("BOB", "Bolivian Boliviano"),
    ("BRL", "Brazilian Real"),
    ("BSD", "Bahamian Dollar"),
    ("BTC", "Bitcoin"),
    ("BTN", "Bhutanese Ngultrum"),
    ("BWP", "Botswanan Pula"),
    ("BYN", "Belarusian Ruble"),
    ("BZD", "Belize Dollar"),
    ("CAD", "Canadian Dollar"),
    ("CDF", "Congolese Franc"),
    ("CHF", "Swiss Franc"),
    ("CKD", "CKD"),
    ("CLP", "Chilean Peso"),
    ("CNY", "Chinese Yuan"),
    ("COP", "Colombian Peso"),
    ("CRC", "Costa Rican Colón"),
    ("CUP", "Cuban Peso"),
    ("CVE", "Cape Verdean Escudo"),
    ("CZK", "Czech Koruna"),
    ("DJF", "Djiboutian Franc"),
    ("DKK", "Danish Krone"),
    ("DOP", "Dominican Peso"),
    ("DZD", "Algerian Dinar"),
    ("EGP", "Egyptian Pound"),
    ("ERN", "Eritrean Nakfa"),
    ("ETB", "Ethiopian Birr"),
    ("EUR", "Euro"),
    ("FJD", "Fijian Dollar"),
    ("FKP", "Falkland Islands Pound"),
    ("FOK", "FOK"),
    ("GBP", "British Pound"),
    ("GEL", "Georgian Lari"),
    ("GGP", "GGP"),
    ("GHS", "Ghanaian Cedi"),
    ("GIP", "Gibraltar Pound"),
    ("GMD", "Gambian Dalasi"),
    ("GNF", "Guinean Franc"),
    ("GTQ", "Guatemalan Quetzal"),
    ("GYD", "Guyanaese Dollar"),
    ("HKD", "Hong Kong Dollar"),
    ("HNL", "Honduran Lempira"),
    ("HRK", "Croatian Kuna"),
    ("HTG", "Haitian Gourde"),
    ("HUF", "Hungarian Forint"),
    ("IDR", "Indonesian Rupiah"),
    ("ILS", "Israeli New Shekel"),
    ("IMP", "IMP"),
    ("INR", "Indian Rupee"),
    ("IQD", "Iraqi Dinar"),
    ("IRR", "Iranian Rial"),
    ("ISK", "Icelandic Króna"),
    ("JEP", "JEP"),
    ("JMD", "Jamaican Dollar"),
    ("JOD", "Jordanian Dinar"),
    ("JPY", "Japanese Yen"),
    ("KES", "Kenyan Shilling"),
    ("KGS", "Kyrgystani Som"),
    ("KHR", "Cambodian Riel"),
    ("KID", "KID"),
    ("KMF", "Comorian Franc"),
    ("KPW", "North Korean Won"),
    ("KRW", "South Korean Won"),
    ("KWD", "Kuwaiti Dinar"),
    ("KYD", "Cayman Islands Dollar"),
    ("KZT", "Kazakhstani Tenge"),
    ("LAK", "Laotian Kip"),
    ("LBP", "Lebanese Pound"),
    ("LKR", "Sri Lankan Rupee"),
    ("LRD", "Liberian Dollar"),
    ("LSL", "Lesotho Loti"),
    ("LYD", "Libyan Dinar"),
    ("MAD", "Moroccan Dirham"),
    ("MDL", "Moldovan Leu"),
    ("MGA", "Malagasy Ariary"),
    ("MKD", "Macedonian Denar"),
    ("MMK", "Myanmar Kyat"),
    ("MNT", "Mongolian Tugrik"),
    ("MOP", "Macanese Pataca"),
    ("MRU", "Mauritanian Ouguiya"),
    ("MUR", "Mauritian Rupee"),
    ("MVR", "Maldivian Rufiyaa"),
    ("MWK", "Malawian Kwacha"),
    ("MXN", "Mexican Peso"),
    ("MYR", "Malaysian Ringgit"),
    ("MZN", "Mozambican Metical"),
    ("NAD", "Namibian Dollar"),
    ("NGN", "Nigerian Naira"),
    ("NIO", "Nicaraguan Córdoba"),
    ("NOK", "Norwegian Krone"),
    ("NPR", "Nepalese Rupee"),
    ("NZD", "New Zealand Dollar"),
    ("OMR", "Omani Rial"),
    ("PAB", "Panamanian Balboa"),
    ("PEN", "Peruvian Sol"),
    ("PGK", "Papua New Guinean Kina"),
    ("PHP", "Philippine Piso"),
    ("PKR", "Pakistani Rupee"),
    ("PLN", "Polish Zloty"),
    ("PND", "PND"),
    ("PRB", "PRB"),
    ("PYG", "Paraguayan Guarani"),
    ("QAR", "Qatari Rial"),
    ("RON", "Romanian Leu"),
    ("RSD", "Serbian Dinar"),
    ("RUB", "Russian Ruble"),
    ("RWF", "Rwandan Franc"),
    ("SAR", "Saudi Riyal"),
    ("SBD", "Solomon Islands Dollar"),
    ("SCR", "Seychellois Rupee"),
    ("SDG", "Sudanese Pound"),
    ("SEK", "Swedish Krona"),
    ("SGD", "Singapore Dollar"),
    ("SHP", "St. Helena Pound"),
    ("SLL", "Sierra Leonean Leone"),
    ("SLS", "SLS"),
    ("SOS", "Somali Shilling"),
    ("SRD", "Surinamese Dollar"),
    ("SSP", "South Sudanese Pound"),
    ("STN", "São Tomé & Príncipe Dobra"),
    ("SYP", "Syrian Pound"),
    ("SZL", "Swazi Lilangeni"),
    ("THB", "Thai Baht"),
    ("TJS", "Tajikistani Somoni"),
    ("TMT", "Turkmenistani Manat"),
    ("TND", "Tunisian Dinar"),
    ("TOP", "Tongan Paʻanga"),
    ("TRY", "Turkish Lira"),
    ("TTD", "Trinidad & Tobago Dollar"),
    ("TVD", "TVD"),
    ("TWD", "New Taiwan Dollar"),
    ("TZS", "Tanzanian Shilling"),
    ("UAH", "Ukrainian Hryvnia"),
    ("UGX", "Ugandan Shilling"),
    ("USD", "US Dollar"),
    ("UYU", "Uruguayan Peso"),
    ("UZS", "Uzbekistani Som"),
    ("VES", "Venezuelan Bolívar"),
    ("VND", "Vietnamese Dong"),
    ("VUV", "Vanuatu Vatu"),
    ("WST", "Samoan Tala"),
    ("XAF", "Central African CFA Franc"),
    ("XCD", "East Caribbean Dollar"),
    ("XOF", "West African CFA Franc"),
    ("XPF", "CFP Franc"),
    ("YER", "Yemeni Rial"),
    ("ZAR", "South African Rand"),
    ("ZMW", "Zambian Kwacha"),
    ("ZWB", "ZWB"),
]

CURRENCY_CHOICES_WITH_CODE = [
    ("AFN", "Afghan Afghani (AFN)"),
    ("ALL", "Albanian Lek (ALL)"),
    ("DZD", "Algerian Dinar (DZD)"),
    ("AOA", "Angolan Kwanza (AOA)"),
    ("ARS", "Argentine Peso (ARS)"),
    ("AMD", "Armenian Dram (AMD)"),
    ("AWG", "Aruban Florin (AWG)"),
    ("AUD", "Australian Dollar (AUD)"),
    ("AZN", "Azerbaijani Manat (AZN)"),
    ("BSD", "Bahamian Dollar (BSD)"),
    ("BHD", "Bahraini Dinar (BHD)"),
    ("BDT", "Bangladeshi Taka (BDT)"),
    ("BBD", "Barbadian Dollar (BBD)"),
    ("BYN", "Belarusian Ruble (BYN)"),
    ("BZD", "Belize Dollar (BZD)"),
    ("BMD", "Bermudan Dollar (BMD)"),
    ("BTN", "Bhutanese Ngultrum (BTN)"),
    ("BTC", "Bitcoin (BTC)"),
    ("BOB", "Bolivian Boliviano (BOB)"),
    ("BAM", "Bosnia-Herzegovina Convertible Mark (BAM)"),
    ("BWP", "Botswanan Pula (BWP)"),
    ("BRL", "Brazilian Real (BRL)"),
    ("GBP", "British Pound (GBP)"),
    ("BND", "Brunei Dollar (BND)"),
    ("BGN", "Bulgarian Lev (BGN)"),
    ("BIF", "Burundian Franc (BIF)"),
    ("XPF", "CFP Franc (XPF)"),
    ("CKD", "CKD (CKD)"),
    ("KHR", "Cambodian Riel (KHR)"),
    ("CAD", "Canadian Dollar (CAD)"),
    ("CVE", "Cape Verdean Escudo (CVE)"),
    ("KYD", "Cayman Islands Dollar (KYD)"),
    ("XAF", "Central African CFA Franc (XAF)"),
    ("CLP", "Chilean Peso (CLP)"),
    ("CNY", "Chinese Yuan (CNY)"),
    ("COP", "Colombian Peso (COP)"),
    ("KMF", "Comorian Franc (KMF)"),
    ("CDF", "Congolese Franc (CDF)"),
    ("CRC", "Costa Rican Colón (CRC)"),
    ("HRK", "Croatian Kuna (HRK)"),
    ("CUP", "Cuban Peso (CUP)"),
    ("CZK", "Czech Koruna (CZK)"),
    ("DKK", "Danish Krone (DKK)"),
    ("DJF", "Djiboutian Franc (DJF)"),
    ("DOP", "Dominican Peso (DOP)"),
    ("XCD", "East Caribbean Dollar (XCD)"),
    ("EGP", "Egyptian Pound (EGP)"),
    ("ERN", "Eritrean Nakfa (ERN)"),
    ("ETB", "Ethiopian Birr (ETB)"),
    ("EUR", "Euro (EUR)"),
    ("FOK", "FOK (FOK)"),
    ("FKP", "Falkland Islands Pound (FKP)"),
    ("FJD", "Fijian Dollar (FJD)"),
    ("GGP", "GGP (GGP)"),
    ("GMD", "Gambian Dalasi (GMD)"),
    ("GEL", "Georgian Lari (GEL)"),
    ("GHS", "Ghanaian Cedi (GHS)"),
    ("GIP", "Gibraltar Pound (GIP)"),
    ("GTQ", "Guatemalan Quetzal (GTQ)"),
    ("GNF", "Guinean Franc (GNF)"),
    ("GYD", "Guyanaese Dollar (GYD)"),
    ("HTG", "Haitian Gourde (HTG)"),
    ("HNL", "Honduran Lempira (HNL)"),
    ("HKD", "Hong Kong Dollar (HKD)"),
    ("HUF", "Hungarian Forint (HUF)"),
    ("IMP", "IMP (IMP)"),
    ("ISK", "Icelandic Króna (ISK)"),
    ("INR", "Indian Rupee (INR)"),
    ("IDR", "Indonesian Rupiah (IDR)"),
    ("IRR", "Iranian Rial (IRR)"),
    ("IQD", "Iraqi Dinar (IQD)"),
    ("ILS", "Israeli New Shekel (ILS)"),
    ("JEP", "JEP (JEP)"),
    ("JMD", "Jamaican Dollar (JMD)"),
    ("JPY", "Japanese Yen (JPY)"),
    ("JOD", "Jordanian Dinar (JOD)"),
    ("KID", "KID (KID)"),
    ("KZT", "Kazakhstani Tenge (KZT)"),
    ("KES", "Kenyan Shilling (KES)"),
    ("KWD", "Kuwaiti Dinar (KWD)"),
    ("KGS", "Kyrgystani Som (KGS)"),
    ("LAK", "Laotian Kip (LAK)"),
    ("LBP", "Lebanese Pound (LBP)"),
    ("LSL", "Lesotho Loti (LSL)"),
    ("LRD", "Liberian Dollar (LRD)"),
    ("LYD", "Libyan Dinar (LYD)"),
    ("MOP", "Macanese Pataca (MOP)"),
    ("MKD", "Macedonian Denar (MKD)"),
    ("MGA", "Malagasy Ariary (MGA)"),
    ("MWK", "Malawian Kwacha (MWK)"),
    ("MYR", "Malaysian Ringgit (MYR)"),
    ("MVR", "Maldivian Rufiyaa (MVR)"),
    ("MRU", "Mauritanian Ouguiya (MRU)"),
    ("MUR", "Mauritian Rupee (MUR)"),
    ("MXN", "Mexican Peso (MXN)"),
    ("MDL", "Moldovan Leu (MDL)"),
    ("MNT", "Mongolian Tugrik (MNT)"),
    ("MAD", "Moroccan Dirham (MAD)"),
    ("MZN", "Mozambican Metical (MZN)"),
    ("MMK", "Myanmar Kyat (MMK)"),
    ("NAD", "Namibian Dollar (NAD)"),
    ("NPR", "Nepalese Rupee (NPR)"),
    ("ANG", "Netherlands Antillean Guilder (ANG)"),
    ("TWD", "New Taiwan Dollar (TWD)"),
    ("NZD", "New Zealand Dollar (NZD)"),
    ("NIO", "Nicaraguan Córdoba (NIO)"),
    ("NGN", "Nigerian Naira (NGN)"),
    ("KPW", "North Korean Won (KPW)"),
    ("NOK", "Norwegian Krone (NOK)"),
    ("OMR", "Omani Rial (OMR)"),
    ("PND", "PND (PND)"),
    ("PRB", "PRB (PRB)"),
    ("PKR", "Pakistani Rupee (PKR)"),
    ("PAB", "Panamanian Balboa (PAB)"),
    ("PGK", "Papua New Guinean Kina (PGK)"),
    ("PYG", "Paraguayan Guarani (PYG)"),
    ("PEN", "Peruvian Sol (PEN)"),
    ("PHP", "Philippine Piso (PHP)"),
    ("PLN", "Polish Zloty (PLN)"),
    ("QAR", "Qatari Rial (QAR)"),
    ("RON", "Romanian Leu (RON)"),
    ("RUB", "Russian Ruble (RUB)"),
    ("RWF", "Rwandan Franc (RWF)"),
    ("SLS", "SLS (SLS)"),
    ("WST", "Samoan Tala (WST)"),
    ("SAR", "Saudi Riyal (SAR)"),
    ("RSD", "Serbian Dinar (RSD)"),
    ("SCR", "Seychellois Rupee (SCR)"),
    ("SLL", "Sierra Leonean Leone (SLL)"),
    ("SGD", "Singapore Dollar (SGD)"),
    ("SBD", "Solomon Islands Dollar (SBD)"),
    ("SOS", "Somali Shilling (SOS)"),
    ("ZAR", "South African Rand (ZAR)"),
    ("KRW", "South Korean Won (KRW)"),
    ("SSP", "South Sudanese Pound (SSP)"),
    ("LKR", "Sri Lankan Rupee (LKR)"),
    ("SHP", "St. Helena Pound (SHP)"),
    ("SDG", "Sudanese Pound (SDG)"),
    ("SRD", "Surinamese Dollar (SRD)"),
    ("SZL", "Swazi Lilangeni (SZL)"),
    ("SEK", "Swedish Krona (SEK)"),
    ("CHF", "Swiss Franc (CHF)"),
    ("SYP", "Syrian Pound (SYP)"),
    ("STN", "São Tomé & Príncipe Dobra (STN)"),
    ("TVD", "TVD (TVD)"),
    ("TJS", "Tajikistani Somoni (TJS)"),
    ("TZS", "Tanzanian Shilling (TZS)"),
    ("THB", "Thai Baht (THB)"),
    ("TOP", "Tongan Paʻanga (TOP)"),
    ("TTD", "Trinidad & Tobago Dollar (TTD)"),
    ("TND", "Tunisian Dinar (TND)"),
    ("TRY", "Turkish Lira (TRY)"),
    ("TMT", "Turkmenistani Manat (TMT)"),
    ("USD", "US Dollar (USD)"),
    ("UGX", "Ugandan Shilling (UGX)"),
    ("UAH", "Ukrainian Hryvnia (UAH)"),
    ("AED", "United Arab Emirates Dirham (AED)"),
    ("UYU", "Uruguayan Peso (UYU)"),
    ("UZS", "Uzbekistani Som (UZS)"),
    ("VUV", "Vanuatu Vatu (VUV)"),
    ("VES", "Venezuelan Bolívar (VES)"),
    ("VND", "Vietnamese Dong (VND)"),
    ("XOF", "West African CFA Franc (XOF)"),
    ("YER", "Yemeni Rial (YER)"),
    ("ZWB", "ZWB (ZWB)"),
    ("ZMW", "Zambian Kwacha (ZMW)"),
]

CURRENCY_CHOICES_WITH_CODE_SORT_BY_KEY = [
    ("AED", "United Arab Emirates Dirham (AED)"),
    ("AFN", "Afghan Afghani (AFN)"),
    ("ALL", "Albanian Lek (ALL)"),
    ("AMD", "Armenian Dram (AMD)"),
    ("ANG", "Netherlands Antillean Guilder (ANG)"),
    ("AOA", "Angolan Kwanza (AOA)"),
    ("ARS", "Argentine Peso (ARS)"),
    ("AUD", "Australian Dollar (AUD)"),
    ("AWG", "Aruban Florin (AWG)"),
    ("AZN", "Azerbaijani Manat (AZN)"),
    ("BAM", "Bosnia-Herzegovina Convertible Mark (BAM)"),
    ("BBD", "Barbadian Dollar (BBD)"),
    ("BDT", "Bangladeshi Taka (BDT)"),
    ("BGN", "Bulgarian Lev (BGN)"),
    ("BHD", "Bahraini Dinar (BHD)"),
    ("BIF", "Burundian Franc (BIF)"),
    ("BMD", "Bermudan Dollar (BMD)"),
    ("BND", "Brunei Dollar (BND)"),
    ("BOB", "Bolivian Boliviano (BOB)"),
    ("BRL", "Brazilian Real (BRL)"),
    ("BSD", "Bahamian Dollar (BSD)"),
    ("BTC", "Bitcoin (BTC)"),
    ("BTN", "Bhutanese Ngultrum (BTN)"),
    ("BWP", "Botswanan Pula (BWP)"),
    ("BYN", "Belarusian Ruble (BYN)"),
    ("BZD", "Belize Dollar (BZD)"),
    ("CAD", "Canadian Dollar (CAD)"),
    ("CDF", "Congolese Franc (CDF)"),
    ("CHF", "Swiss Franc (CHF)"),
    ("CKD", "CKD (CKD)"),
    ("CLP", "Chilean Peso (CLP)"),
    ("CNY", "Chinese Yuan (CNY)"),
    ("COP", "Colombian Peso (COP)"),
    ("CRC", "Costa Rican Colón (CRC)"),
    ("CUP", "Cuban Peso (CUP)"),
    ("CVE", "Cape Verdean Escudo (CVE)"),
    ("CZK", "Czech Koruna (CZK)"),
    ("DJF", "Djiboutian Franc (DJF)"),
    ("DKK", "Danish Krone (DKK)"),
    ("DOP", "Dominican Peso (DOP)"),
    ("DZD", "Algerian Dinar (DZD)"),
    ("EGP", "Egyptian Pound (EGP)"),
    ("ERN", "Eritrean Nakfa (ERN)"),
    ("ETB", "Ethiopian Birr (ETB)"),
    ("EUR", "Euro (EUR)"),
    ("FJD", "Fijian Dollar (FJD)"),
    ("FKP", "Falkland Islands Pound (FKP)"),
    ("FOK", "FOK (FOK)"),
    ("GBP", "British Pound (GBP)"),
    ("GEL", "Georgian Lari (GEL)"),
    ("GGP", "GGP (GGP)"),
    ("GHS", "Ghanaian Cedi (GHS)"),
    ("GIP", "Gibraltar Pound (GIP)"),
    ("GMD", "Gambian Dalasi (GMD)"),
    ("GNF", "Guinean Franc (GNF)"),
    ("GTQ", "Guatemalan Quetzal (GTQ)"),
    ("GYD", "Guyanaese Dollar (GYD)"),
    ("HKD", "Hong Kong Dollar (HKD)"),
    ("HNL", "Honduran Lempira (HNL)"),
    ("HRK", "Croatian Kuna (HRK)"),
    ("HTG", "Haitian Gourde (HTG)"),
    ("HUF", "Hungarian Forint (HUF)"),
    ("IDR", "Indonesian Rupiah (IDR)"),
    ("ILS", "Israeli New Shekel (ILS)"),
    ("IMP", "IMP (IMP)"),
    ("INR", "Indian Rupee (INR)"),
    ("IQD", "Iraqi Dinar (IQD)"),
    ("IRR", "Iranian Rial (IRR)"),
    ("ISK", "Icelandic Króna (ISK)"),
    ("JEP", "JEP (JEP)"),
    ("JMD", "Jamaican Dollar (JMD)"),
    ("JOD", "Jordanian Dinar (JOD)"),
    ("JPY", "Japanese Yen (JPY)"),
    ("KES", "Kenyan Shilling (KES)"),
    ("KGS", "Kyrgystani Som (KGS)"),
    ("KHR", "Cambodian Riel (KHR)"),
    ("KID", "KID (KID)"),
    ("KMF", "Comorian Franc (KMF)"),
    ("KPW", "North Korean Won (KPW)"),
    ("KRW", "South Korean Won (KRW)"),
    ("KWD", "Kuwaiti Dinar (KWD)"),
    ("KYD", "Cayman Islands Dollar (KYD)"),
    ("KZT", "Kazakhstani Tenge (KZT)"),
    ("LAK", "Laotian Kip (LAK)"),
    ("LBP", "Lebanese Pound (LBP)"),
    ("LKR", "Sri Lankan Rupee (LKR)"),
    ("LRD", "Liberian Dollar (LRD)"),
    ("LSL", "Lesotho Loti (LSL)"),
    ("LYD", "Libyan Dinar (LYD)"),
    ("MAD", "Moroccan Dirham (MAD)"),
    ("MDL", "Moldovan Leu (MDL)"),
    ("MGA", "Malagasy Ariary (MGA)"),
    ("MKD", "Macedonian Denar (MKD)"),
    ("MMK", "Myanmar Kyat (MMK)"),
    ("MNT", "Mongolian Tugrik (MNT)"),
    ("MOP", "Macanese Pataca (MOP)"),
    ("MRU", "Mauritanian Ouguiya (MRU)"),
    ("MUR", "Mauritian Rupee (MUR)"),
    ("MVR", "Maldivian Rufiyaa (MVR)"),
    ("MWK", "Malawian Kwacha (MWK)"),
    ("MXN", "Mexican Peso (MXN)"),
    ("MYR", "Malaysian Ringgit (MYR)"),
    ("MZN", "Mozambican Metical (MZN)"),
    ("NAD", "Namibian Dollar (NAD)"),
    ("NGN", "Nigerian Naira (NGN)"),
    ("NIO", "Nicaraguan Córdoba (NIO)"),
    ("NOK", "Norwegian Krone (NOK)"),
    ("NPR", "Nepalese Rupee (NPR)"),
    ("NZD", "New Zealand Dollar (NZD)"),
    ("OMR", "Omani Rial (OMR)"),
    ("PAB", "Panamanian Balboa (PAB)"),
    ("PEN", "Peruvian Sol (PEN)"),
    ("PGK", "Papua New Guinean Kina (PGK)"),
    ("PHP", "Philippine Piso (PHP)"),
    ("PKR", "Pakistani Rupee (PKR)"),
    ("PLN", "Polish Zloty (PLN)"),
    ("PND", "PND (PND)"),
    ("PRB", "PRB (PRB)"),
    ("PYG", "Paraguayan Guarani (PYG)"),
    ("QAR", "Qatari Rial (QAR)"),
    ("RON", "Romanian Leu (RON)"),
    ("RSD", "Serbian Dinar (RSD)"),
    ("RUB", "Russian Ruble (RUB)"),
    ("RWF", "Rwandan Franc (RWF)"),
    ("SAR", "Saudi Riyal (SAR)"),
    ("SBD", "Solomon Islands Dollar (SBD)"),
    ("SCR", "Seychellois Rupee (SCR)"),
    ("SDG", "Sudanese Pound (SDG)"),
    ("SEK", "Swedish Krona (SEK)"),
    ("SGD", "Singapore Dollar (SGD)"),
    ("SHP", "St. Helena Pound (SHP)"),
    ("SLL", "Sierra Leonean Leone (SLL)"),
    ("SLS", "SLS (SLS)"),
    ("SOS", "Somali Shilling (SOS)"),
    ("SRD", "Surinamese Dollar (SRD)"),
    ("SSP", "South Sudanese Pound (SSP)"),
    ("STN", "São Tomé & Príncipe Dobra (STN)"),
    ("SYP", "Syrian Pound (SYP)"),
    ("SZL", "Swazi Lilangeni (SZL)"),
    ("THB", "Thai Baht (THB)"),
    ("TJS", "Tajikistani Somoni (TJS)"),
    ("TMT", "Turkmenistani Manat (TMT)"),
    ("TND", "Tunisian Dinar (TND)"),
    ("TOP", "Tongan Paʻanga (TOP)"),
    ("TRY", "Turkish Lira (TRY)"),
    ("TTD", "Trinidad & Tobago Dollar (TTD)"),
    ("TVD", "TVD (TVD)"),
    ("TWD", "New Taiwan Dollar (TWD)"),
    ("TZS", "Tanzanian Shilling (TZS)"),
    ("UAH", "Ukrainian Hryvnia (UAH)"),
    ("UGX", "Ugandan Shilling (UGX)"),
    ("USD", "US Dollar (USD)"),
    ("UYU", "Uruguayan Peso (UYU)"),
    ("UZS", "Uzbekistani Som (UZS)"),
    ("VES", "Venezuelan Bolívar (VES)"),
    ("VND", "Vietnamese Dong (VND)"),
    ("VUV", "Vanuatu Vatu (VUV)"),
    ("WST", "Samoan Tala (WST)"),
    ("XAF", "Central African CFA Franc (XAF)"),
    ("XCD", "East Caribbean Dollar (XCD)"),
    ("XOF", "West African CFA Franc (XOF)"),
    ("XPF", "CFP Franc (XPF)"),
    ("YER", "Yemeni Rial (YER)"),
    ("ZAR", "South African Rand (ZAR)"),
    ("ZMW", "Zambian Kwacha (ZMW)"),
    ("ZWB", "ZWB (ZWB)"),
]

LIST_GENERATED_CURRENCY_MODULES = [
    "aed.py",
    "afn.py",
    "all.py",
    "amd.py",
    "ang.py",
    "aoa.py",
    "ars.py",
    "aud.py",
    "awg.py",
    "azn.py",
    "bam.py",
    "bbd.py",
    "bdt.py",
    "bgn.py",
    "bhd.py",
    "bif.py",
    "bmd.py",
    "bnd.py",
    "bob.py",
    "brl.py",
    "bsd.py",
    "btn.py",
    "bwp.py",
    "byn.py",
    "bzd.py",
    "cad.py",
    "cdf.py",
    "chf.py",
    "ckd.py",
    "clp.py",
    "cny.py",
    "cop.py",
    "crc.py",
    "cup.py",
    "cve.py",
    "czk.py",
    "djf.py",
    "dkk.py",
    "dop.py",
    "dzd.py",
    "egp.py",
    "ern.py",
    "etb.py",
    "eur.py",
    "fjd.py",
    "fkp.py",
    "fok.py",
    "gbp.py",
    "gel.py",
    "ggp.py",
    "ghs.py",
    "gip.py",
    "gmd.py",
    "gnf.py",
    "gtq.py",
    "gyd.py",
    "hkd.py",
    "hnl.py",
    "hrk.py",
    "htg.py",
    "huf.py",
    "idr.py",
    "ils.py",
    "imp.py",
    "inr.py",
    "iqd.py",
    "irr.py",
    "isk.py",
    "jep.py",
    "jmd.py",
    "jod.py",
    "jpy.py",
    "kes.py",
    "kgs.py",
    "khr.py",
    "kid.py",
    "kmf.py",
    "kpw.py",
    "krw.py",
    "kwd.py",
    "kyd.py",
    "kzt.py",
    "lak.py",
    "lbp.py",
    "lkr.py",
    "lrd.py",
    "lsl.py",
    "lyd.py",
    "mad.py",
    "mdl.py",
    "mga.py",
    "mkd.py",
    "mmk.py",
    "mnt.py",
    "mop.py",
    "mru.py",
    "mur.py",
    "mvr.py",
    "mwk.py",
    "mxn.py",
    "myr.py",
    "mzn.py",
    "nad.py",
    "ngn.py",
    "nio.py",
    "nok.py",
    "npr.py",
    "nzd.py",
    "omr.py",
    "pab.py",
    "pen.py",
    "pgk.py",
    "php.py",
    "pkr.py",
    "pln.py",
    "pnd.py",
    "prb.py",
    "pyg.py",
    "qar.py",
    "ron.py",
    "rsd.py",
    "rub.py",
    "rwf.py",
    "sar.py",
    "sbd.py",
    "scr.py",
    "sdg.py",
    "sek.py",
    "sgd.py",
    "shp.py",
    "sll.py",
    "sls.py",
    "sos.py",
    "srd.py",
    "ssp.py",
    "stn.py",
    "syp.py",
    "szl.py",
    "thb.py",
    "tjs.py",
    "tmt.py",
    "tnd.py",
    "top.py",
    "try.py",
    "ttd.py",
    "tvd.py",
    "twd.py",
    "tzs.py",
    "uah.py",
    "ugx.py",
    "usd.py",
    "uyu.py",
    "uzs.py",
    "ves.py",
    "vnd.py",
    "vuv.py",
    "wst.py",
    "xaf.py",
    "xcd.py",
    "xof.py",
    "xpf.py",
    "yer.py",
    "zar.py",
    "zmw.py",
    "zwb.py",
]
