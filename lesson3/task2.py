def func(name, surname, year_of_birth, city, email, telephone):
    print("Студент " + name, surname + ",", "год рождения:", str(year_of_birth) + ",",
          "город", city + ",", "email: " + email + ",", "телефон: " + telephone)


func(surname="Божков", name="Андрей", telephone="+79183550065",
     city="Краснодар", email="kovbozh@gmail.com", year_of_birth=1977)
