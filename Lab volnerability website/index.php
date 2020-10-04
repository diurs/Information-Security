<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h2>Чтобы получить доступ к библиотеке, введите учебные данные :</h2>
        <form method="get" action="?">
            <p>Введите ваше имя</p>
            <input name="name" type="text">
            <p>Введите ваш пароль</p>
            <input name="password" type="text"><br />
            <input type="submit">
        </form>

        <?php
        $mysqli = new mysqli("localhost", "root", "", "db_library");
        if (mysqli_connect_errno()) {
            printf("Не удалось подключиться: %s\n", mysqli_connect_error());
            exit();
        } else {
            $mysqli->query("SET NAMES UTF8");
            $mysqli->query("SET CHARACTER SET UTF8");
            $mysqli->query("SET character_set_client = UTF8");
            $mysqli->query("SET character_set_connection = UTF8");
            $mysqli->query("SET character_set_results = UTF8");
        }

        $name = filter_input(INPUT_GET, 'name');
        $password = filter_input(INPUT_GET, 'password');
        if ($result = $mysqli->query("SELECT * FROM `members` WHERE name = '$name' AND password = '$password'")) {
            while ($obj = $result->fetch_object()) {
                echo "<p><b>Ваше имя: </b> $obj->name</p>
        <p><b>Ваш статус:</b> $obj->status</p>
        <p><b>Доступные для Вас книги:</b> $obj->books</p><hr />";
            }
        } else {
            printf("Ошибка: %s\n", $mysqli->error);
        }
        $mysqli->close();
        ?>

    </body>
</html>
