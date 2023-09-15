import requests 



staff = [
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "doe@navis.com",
        "phone_number": "0712345678",
        "id_number": "12345678",
        "kra_pin": "98765432",
        "password": "33992433nkl"
    },
    {
        "first_name": "John",
        "last_name": "Smith",
        "email": "smith@navis.com",
        "phone_number": "0723456789",
        "id_number": "23456789",
        "kra_pin": "876543218",
        "password": "33992433nkl"
    },
    {
        "first_name": "Grace",
        "last_name": "Njoroge",
        "email": "njoroge@navis.com",
        "phone_number": "0734567890",
        "id_number": "34567890",
        "kra_pin": "76543210",
        "password": "33992433nkl"
    },
    {
        "first_name": "Daniel",
        "last_name": "Kamau",
        "email": "kamau@navis.com",
        "phone_number": "0712345678",
        "id_number": "45678901",
        "kra_pin": "65432109",
        "password": "33992433nkl"
    },
    {
        "first_name": "Sarah",
        "last_name": "Ochieng",
        "email": "sarah@navis.com",
        "phone_number": "0723456789",
        "id_number": "56789012",
        "kra_pin": "54321098",
        "password": "33992433nkl"
    },
    {
        "first_name": "Peter",
        "last_name": "Mwangi",
        "email": "peter@navis.com",
        "phone_number": "0734567890",
        "id_number": "67890123",
        "kra_pin": "43210987",
        "password": "33992433nkl"
    },
    {
        "first_name": "Mary",
        "last_name": "Kariuki",
        "email": "mary@navis.com",
        "phone_number": "0712345678",
        "id_number": "78901234",
        "kra_pin": "32109876",
        "password": "33992433nkl"
    },
    {
        "first_name": "David",
        "last_name": "Odhiambo",
        "email": "david@navis.com",
        "phone_number": "0723456789",
        "id_number": "89012345",
        "kra_pin": "21098765",
        "password": "33992433nkl"
    },
    {
        "first_name": "Mercy",
        "last_name": "Gitau",
        "email": "gitau@navis.com",
        "phone_number": "0734567890",
        "id_number": "90123456",
        "kra_pin": "10987654",
        "password": "33992433nkl"
    },
    {
        "first_name": "James",
        "last_name": "Njeru",
        "email": "james@navis.com",
        "phone_number": "0712345678",
        "id_number": "01234567",
        "kra_pin": "09876543",
        "password": "33992433nkl"
    },
    {
        "first_name": "Eva",
        "last_name": "Kiprop",
        "email": "eva@navis.com",
        "phone_number": "0723456789",
        "id_number": "98765432",
        "kra_pin": "98765432",
        "password": "33992433nkl"
    },
    {
        "first_name": "Joseph",
        "last_name": "Waweru",
        "email": "waweru@navis.com",
        "phone_number": "0734567890",
        "id_number": "876554321",
        "kra_pin": "8765439216",
        "password": "33992433nkl"
    },
    {
        "first_name": "Alice",
        "last_name": "Kimani",
        "email": "alice@navis.com",
        "phone_number": "0712345678",
        "id_number": "76543210",
        "kra_pin": "76543210",
        "password": "33992433nkl"
    },
    {
        "first_name": "Charles",
        "last_name": "Gathoni",
        "email": "charles@navis.com",
        "phone_number": "0723456789",
        "id_number": "65432109",
        "kra_pin": "65432109",
        "password": "33992433nkl"
    },
    {
        "first_name": "Linda",
        "last_name": "Oloo",
        "email": "oloo@navis.com",
        "phone_number": "0734567890",
        "id_number": "54321098",
        "kra_pin": "54321098",
        "password": "33992433nkl"
    },
    {
        "first_name": "George",
        "last_name": "Wanjiku",
        "email": "george@navis.com",
        "phone_number": "0712345678",
        "id_number": "43210987",
        "kra_pin": "43210987",
        "password": "33992433nkl"
    },
    {
        "first_name": "Nancy",
        "last_name": "Gitonga",
        "email": "nancy@navis.com",
        "phone_number": "0723456789",
        "id_number": "32109876",
        "kra_pin": "32109876",
        "password": "33992433nkl"
    },
    {
        "first_name": "Samuel",
        "last_name": "Mugo",
        "email": "mugo@navis.com",
        "phone_number": "0734567890",
        "id_number": "21098765",
        "kra_pin": "21098765",
        "password": "33992433nkl"
    },
    {
        "first_name": "Rebecca",
        "last_name": "Ndungu",
        "email": "rebecca@navis.com",
        "phone_number": "0712345678",
        "id_number": "10987654",
        "kra_pin": "10987654",
        "password": "33992433nkl"
    },
    {
        "first_name": "Michael",
        "last_name": "Githinji",
        "email": "githinji@navis.com",
        "phone_number": "0723456789",
        "id_number": "09876543",
        "kra_pin": "09876543",
        "password": "33992433nkl"
    }
]

trucks = [
    
    {
        "carry_weight": "4800.00",
        "chasis_number": "AB123456",
        "engine_power": "550",
        "engine_size": "4200",
        "manufacturer": "Ford",
        "model": "Transit",
        "registration_number": "KBC 123T",
        "yom": "2017-08-22"
    },
    {
        "carry_weight": "5200.00",
        "chasis_number": "CD789012",
        "engine_power": "480",
        "engine_size": "4000",
        "manufacturer": "Mercedes-Benz",
        "model": "Sprinter",
        "registration_number": "KDE 456S",
        "yom": "2016-05-30"
    },
    {
        "carry_weight": "5500.00",
        "chasis_number": "EF345678",
        "engine_power": "620",
        "engine_size": "4800",
        "manufacturer": "Volvo",
        "model": "FH16",
        "registration_number": "KDF 678Q",
        "yom": "2018-11-10"
    },
    {
        "carry_weight": "4700.00",
        "chasis_number": "GH901234",
        "engine_power": "490",
        "engine_size": "4300",
        "manufacturer": "Scania",
        "model": "R450",
        "registration_number": "KEA 567W",
        "yom": "2019-02-15"
    },
    {
        "carry_weight": "5100.00",
        "chasis_number": "IJ567890",
        "engine_power": "540",
        "engine_size": "4600",
        "manufacturer": "MAN",
        "model": "TGX",
        "registration_number": "KFA 890X",
        "yom": "2020-07-05"
    },
    {
        "carry_weight": "4900.00",
        "chasis_number": "KL123456",
        "engine_power": "600",
        "engine_size": "4900",
        "manufacturer": "DAF",
        "model": "XF 105",
        "registration_number": "KGA 123H",
        "yom": "2014-04-18"
    },
    {
        "carry_weight": "5300.00",
        "chasis_number": "MN234567",
        "engine_power": "570",
        "engine_size": "4700",
        "manufacturer": "Kenworth",
        "model": "W990",
        "registration_number": "KHA 234E",
        "yom": "2021-09-03"
    },
    {
        "carry_weight": "4600.00",
        "chasis_number": "OP345678",
        "engine_power": "510",
        "engine_size": "4400",
        "manufacturer": "Isuzu",
        "model": "NPR",
        "registration_number": "KIA 345G",
        "yom": "2013-12-27"
    },
    {
        "carry_weight": "5400.00",
        "chasis_number": "QR456789",
        "engine_power": "590",
        "engine_size": "4500",
        "manufacturer": "Peterbilt",
        "model": "389",
        "registration_number": "KJA 456L",
        "yom": "2022-04-14"
    },
    {
        "carry_weight": "4900.00",
        "chasis_number": "ST567890",
        "engine_power": "620",
        "engine_size": "4800",
        "manufacturer": "Freightliner",
        "model": "Cascadia",
        "registration_number": "KKA 567M",
        "yom": "2016-09-08"
    },
    {
        "carry_weight": "4700.00",
        "chasis_number": "UV678901",
        "engine_power": "580",
        "engine_size": "4700",
        "manufacturer": "International",
        "model": "ProStar",
        "registration_number": "KLA 678N",
        "yom": "2015-10-25"
    },
    {
        "carry_weight": "5200.00",
        "chasis_number": "WX789012",
        "engine_power": "490",
        "engine_size": "4200",
        "manufacturer": "Hino",
        "model": "268",
        "registration_number": "KMA 789P",
        "yom": "2017-07-12"
    },
    {
        "carry_weight": "5100.00",
        "chasis_number": "YZ890123",
        "engine_power": "520",
        "engine_size": "4300",
        "manufacturer": "Mack",
        "model": "Anthem",
        "registration_number": "KNA 890R",
        "yom": "2019-03-29"
    },
    {
        "carry_weight": "5000.00",
        "chasis_number": "AB012345",
        "engine_power": "570",
        "engine_size": "4500",
        "manufacturer": "Western Star",
        "model": "4900",
        "registration_number": "KOA 012H",
        "yom": "2020-08-20"
    },
    {
        "carry_weight": "5300.00",
        "chasis_number": "BC123456",
        "engine_power": "580",
        "engine_size": "4700",
        "manufacturer": "Kenworth",
        "model": "T680",
        "registration_number": "KPA 123E",
        "yom": "2018-05-16"
    },
    {
        "carry_weight": "4700.00",
        "chasis_number": "CD234567",
        "engine_power": "510",
        "engine_size": "4400",
        "manufacturer": "Freightliner",
        "model": "M2",
        "registration_number": "KQA 234W",
        "yom": "2014-11-02"
    },
    {
        "carry_weight": "5400.00",
        "chasis_number": "DE345678",
        "engine_power": "590",
        "engine_size": "4600",
        "manufacturer": "Volvo",
        "model": "VNL 860",
        "registration_number": "KRA 345M",
        "yom": "2022-02-09"
    },
    {
        "carry_weight": "4600.00",
        "chasis_number": "EF456789",
        "engine_power": "530",
        "engine_size": "4300",
        "manufacturer": "Peterbilt",
        "model": "567",
        "registration_number": "KSA 456N",
        "yom": "2017-12-11"
    },
    {
        "carry_weight": "5100.00",
        "chasis_number": "FG567890",
        "engine_power": "550",
        "engine_size": "4500",
        "manufacturer": "Mack",
        "model": "Granite",
        "registration_number": "KTA 567R",
        "yom": "2016-06-06"
    }
]



drivers = [
    {
        "first_name": "Nickson",
        "last_name": "Langat",
        "email": "nicksonlangat95@gmail.com",
        "phone_number": "0713754946",
        "licence_number": "65432154",
        "identity_number": "33993544",
        "kra_pin": "56768754"
    },
    {
        "first_name": "Alice",
        "last_name": "Wanjiru",
        "email": "alicewanjiru@example.com",
        "phone_number": "0725463987",
        "licence_number": "78965432",
        "identity_number": "12345678",
        "kra_pin": "98765432"
    },
    {
        "first_name": "David",
        "last_name": "Ochieng",
        "email": "davidochieng@example.com",
        "phone_number": "0738124567",
        "licence_number": "45678901",
        "identity_number": "23456789",
        "kra_pin": "876545321"
    },
    {
        "first_name": "Grace",
        "last_name": "Muthoni",
        "email": "gracemuthoni@example.com",
        "phone_number": "0712345678",
        "licence_number": "54321678",
        "identity_number": "34567890",
        "kra_pin": "76543210"
    },
    {
        "first_name": "John",
        "last_name": "Kiprop",
        "email": "johnkiprop@example.com",
        "phone_number": "0723487654",
        "licence_number": "67890123",
        "identity_number": "45678901",
        "kra_pin": "65432109"
    },
    {
        "first_name": "Mary",
        "last_name": "Githinji",
        "email": "marygithinji@example.com",
        "phone_number": "0715874321",
        "licence_number": "78901234",
        "identity_number": "56789012",
        "kra_pin": "54321098"
    },
    {
        "first_name": "Peter",
        "last_name": "Mugo",
        "email": "petermugo@example.com",
        "phone_number": "0732123456",
        "licence_number": "89012345",
        "identity_number": "67890123",
        "kra_pin": "43210987"
    },
    {
        "first_name": "Sarah",
        "last_name": "Kariuki",
        "email": "sarahkariuki@example.com",
        "phone_number": "0721345678",
        "licence_number": "90123456",
        "identity_number": "78901234",
        "kra_pin": "32109876"
    },
    {
        "first_name": "James",
        "last_name": "Odhiambo",
        "email": "jamesodhiambo@example.com",
        "phone_number": "0714789653",
        "licence_number": "23456789",
        "identity_number": "89012345",
        "kra_pin": "10987654"
    },
    {
        "first_name": "Alice",
        "last_name": "Gitau",
        "email": "alicegitau@example.com",
        "phone_number": "0727896543",
        "licence_number": "34567890",
        "identity_number": "01234567",
        "kra_pin": "09876543"
    },
    {
        "first_name": "Charles",
        "last_name": "Waweru",
        "email": "charleswaweru@example.com",
        "phone_number": "0731234567",
        "licence_number": "45678901",
        "identity_number": "12345678",
        "kra_pin": "98765432"
    },
    {
        "first_name": "Linda",
        "last_name": "Onyango",
        "email": "lindaonyango@example.com",
        "phone_number": "0712456789",
        "licence_number": "56789012",
        "identity_number": "23456789",
        "kra_pin": "876543321"
    },
    {
        "first_name": "George",
        "last_name": "Njoroge",
        "email": "georgenjoroge@example.com",
        "phone_number": "0723567890",
        "licence_number": "67890123",
        "identity_number": "34567890",
        "kra_pin": "76543210"
    },
    {
        "first_name": "Nancy",
        "last_name": "Oloo",
        "email": "nancyoloo@example.com",
        "phone_number": "0736789012",
        "licence_number": "78901234",
        "identity_number": "45678901",
        "kra_pin": "65432109"
    },
    {
        "first_name": "Samuel",
        "last_name": "Kimani",
        "email": "samuelkimani@example.com",
        "phone_number": "0714567890",
        "licence_number": "90123456",
        "identity_number": "56789012",
        "kra_pin": "54321098"
    },
    {
        "first_name": "Rebecca",
        "last_name": "Omondi",
        "email": "rebeccao@example.com",
        "phone_number": "0725678901",
        "licence_number": "01234567",
        "identity_number": "67890123",
        "kra_pin": "32109876"
    },
    {
        "first_name": "Michael",
        "last_name": "Wanjiku",
        "email": "michaelwanjiku@example.com",
        "phone_number": "0731234567",
        "licence_number": "12345678",
        "identity_number": "78901234",
        "kra_pin": "10987654"
    },
    {
        "first_name": "Eva",
        "last_name": "Kariuki",
        "email": "evakariuki@example.com",
        "phone_number": "0712345678",
        "licence_number": "23456789",
        "identity_number": "01234567",
        "kra_pin": "09876543"
    },
    {
        "first_name": "Joseph",
        "last_name": "Githinji",
        "email": "josephgithinji@example.com",
        "phone_number": "0723456789",
        "licence_number": "34567890",
        "identity_number": "23456789",
        "kra_pin": "8765443211"
    }
]


drivers2 = [
    
    {
        "first_name": "Alice",
        "last_name": "Wanjiru",
        "email": "alicewandjiru@example.com",
        "phone_number": "07222262222",
        "licence_number": "222226222",
        "identity_number": "222222622",
        "kra_pin": "222222622"
    },
    {
        "first_name": "David",
        "last_name": "Ochieng",
        "email": "davidocdhieng@example.com",
        "phone_number": "0733333333",
        "licence_number": "33333333",
        "identity_number": "33333333",
        "kra_pin": "33333333"
    },
    {
        "first_name": "Grace",
        "last_name": "Muthoni",
        "email": "gracemduthoni@example.com",
        "phone_number": "0744444444",
        "licence_number": "44444444",
        "identity_number": "44444444",
        "kra_pin": "44444444"
    },
    {
        "first_name": "John",
        "last_name": "Kiprop",
        "email": "johndkiprop@example.com",
        "phone_number": "0755555555",
        "licence_number": "55555555",
        "identity_number": "55555555",
        "kra_pin": "55555555"
    },
    {
        "first_name": "Mary",
        "last_name": "Githinji",
        "email": "marygidthinji@example.com",
        "phone_number": "0766666666",
        "licence_number": "66666666",
        "identity_number": "66666666",
        "kra_pin": "66666666"
    },
    {
        "first_name": "Peter",
        "last_name": "Mugo",
        "email": "peterdmugo@example.com",
        "phone_number": "0777777777",
        "licence_number": "77777777",
        "identity_number": "77777777",
        "kra_pin": "77777777"
    },
    {
        "first_name": "Sarah",
        "last_name": "Kariuki",
        "email": "sarahdkariuki@example.com",
        "phone_number": "0788888888",
        "licence_number": "88888888",
        "identity_number": "88888888",
        "kra_pin": "88888888"
    },
    {
        "first_name": "James",
        "last_name": "Odhiambo",
        "email": "jamesdodhiambo@example.com",
        "phone_number": "0799999999",
        "licence_number": "99999999",
        "identity_number": "99999999",
        "kra_pin": "99999999"
    },
    {
        "first_name": "Nancy",
        "last_name": "Gitau",
        "email": "nancygditau@example.com",
        "phone_number": "0700000000",
        "licence_number": "00000000",
        "identity_number": "00000000",
        "kra_pin": "00000000"
    }
]

clients = [
    {
        "first_name": "Nickson",
        "last_name": "Langat",
        "email": "nicksonlangat95@gmail.com",
        "phone_number": "0713754946",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "33992433"
    },
    {
        "first_name": "Alice",
        "last_name": "Wanjiru",
        "email": "alicewanjiru@example.com",
        "phone_number": "0725463987",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "12345678"
    },
    {
        "first_name": "David",
        "last_name": "Ochieng",
        "email": "davidochieng@example.com",
        "phone_number": "0738124567",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "23456789"
    },
    {
        "first_name": "Grace",
        "last_name": "Muthoni",
        "email": "gracemuthoni@example.com",
        "phone_number": "0712345678",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "34567890"
    },
    {
        "first_name": "John",
        "last_name": "Kiprop",
        "email": "johnkiprop@example.com",
        "phone_number": "0723487654",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "45678901"
    },
    {
        "first_name": "Mary",
        "last_name": "Githinji",
        "email": "marygithinji@example.com",
        "phone_number": "0715874321",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "56789012"
    },
    {
        "first_name": "Peter",
        "last_name": "Mugo",
        "email": "petermugo@example.com",
        "phone_number": "0732123456",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "67890123"
    },
    {
        "first_name": "Sarah",
        "last_name": "Kariuki",
        "email": "sarahkariuki@example.com",
        "phone_number": "0721345678",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "78901234"
    },
    {
        "first_name": "James",
        "last_name": "Odhiambo",
        "email": "jamesodhiambo@example.com",
        "phone_number": "0714789653",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "89012345"
    },
    {
        "first_name": "Alice",
        "last_name": "Gitau",
        "email": "alicegitau@example.com",
        "phone_number": "0727896543",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "01234567"
    },
    {
        "first_name": "Charles",
        "last_name": "Waweru",
        "email": "charleswaweru@example.com",
        "phone_number": "0731234567",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "09876543"
    },
    {
        "first_name": "Linda",
        "last_name": "Onyango",
        "email": "lindaonyango@example.com",
        "phone_number": "0712456789",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "10987654"
    },
    {
        "first_name": "George",
        "last_name": "Njoroge",
        "email": "georgenjoroge@example.com",
        "phone_number": "0723567890",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "21098765"
    },
    {
        "first_name": "Nancy",
        "last_name": "Oloo",
        "email": "nancyoloo@example.com",
        "phone_number": "0736789012",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "32109876"
    },
    {
        "first_name": "Samuel",
        "last_name": "Kimani",
        "email": "samuelkimani@example.com",
        "phone_number": "0714567890",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "43210987"
    },
    {
        "first_name": "Rebecca",
        "last_name": "Omondi",
        "email": "rebeccao@example.com",
        "phone_number": "0725678901",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "54321098"
    },
    {
        "first_name": "Michael",
        "last_name": "Wanjiku",
        "email": "michaelwanjiku@example.com",
        "phone_number": "0731234567",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "65432109"
    },
    {
        "first_name": "Eva",
        "last_name": "Kariuki",
        "email": "evakariuki@example.com",
        "phone_number": "0712345678",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "76543210"
    },
    {
        "first_name": "Joseph",
        "last_name": "Githinji",
        "email": "josephgithinji@example.com",
        "phone_number": "0723456789",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "87654321"
    },
    {
        "first_name": "Julia",
        "last_name": "Kamau",
        "email": "juliakamau@example.com",
        "phone_number": "0734567890",
        "location": "1028c573-46eb-440c-8e0a-8cca1367af05",
        "identity_number": "98765432"
    }
]



parcels = [
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "120.00",
        "item": "Electrical appliances",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0712543976",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "85.50",
        "item": "Furniture",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0723456789",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "62.30",
        "item": "Clothing",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0734567890",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "150.20",
        "item": "Kitchen Appliances",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0712345678",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "45.80",
        "item": "Books",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0721345678",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "110.75",
        "item": "Electronics",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0719876543",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "75.60",
        "item": "Toys",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0734567890",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "95.40",
        "item": "Home Decor",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0712345678",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "130.90",
        "item": "Sporting Goods",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0727896543",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "88.25",
        "item": "Jewelry",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0731234567",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "120.00",
        "item": "Electrical appliances",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0712543976",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "85.50",
        "item": "Furniture",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0723456789",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "62.30",
        "item": "Clothing",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0734567890",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "150.20",
        "item": "Kitchen Appliances",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0712345678",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "45.80",
        "item": "Books",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0721345678",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "110.75",
        "item": "Electronics",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0719876543",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "75.60",
        "item": "Toys",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0734567890",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "95.40",
        "item": "Home Decor",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0712345678",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "130.90",
        "item": "Sporting Goods",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0727896543",
        "status": "READY"
    },
    {
        "client": "4e5499ec-7de8-436c-8f45-57ccdbea6727",
        "weight": "88.25",
        "item": "Jewelry",
        "destination": "9bf09ad7-d124-4813-9182-340232d74afc",
        "recipient_contact": "0731234567",
        "status": "READY"
    }
]




auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MjkxNTY0LCJpYXQiOjE2OTQ2OTk1NjQsImp0aSI6IjQxODI4Njc4ZTE2MzQwYzBiYTBmMDgxNzU5ZTY5Yzk4IiwidXNlcl9pZCI6ImI2NGJmYTUxLTY3Y2ItNGFiYy1iMDU0LTVkMDUxNzVhZGE4MCJ9.q3EYWCPyTT36KpGUKUuU_qm7UCfYIVMk56AxNPjDsRY'
headers = {'Authorization': f'Bearer {auth_token}'}

url = 'https://navis-api.techwithnick.com/parcels'

for item in parcels:
    # print(item)
    response = requests.post(url, json=item, headers=headers)
    print(response)
    # print("done")
    print(response.json())
