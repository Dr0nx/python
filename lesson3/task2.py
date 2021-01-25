def func(surname, name, email, year_of_birth, telephone, city):
    print("Студент " + name, surname + ",", "год рождения:", str(year_of_birth) + ",",
          "город", city + ",", "email: " + email + ",", "телефон: " + telephone)


func(surname="Божков", name="Андрей", telephone="+79183550065",
     city="Краснодар", email="kovbozh@gmail.com", year_of_birth=1977)
