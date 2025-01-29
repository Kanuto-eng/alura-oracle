<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Juego de piedra, papel o tijera </title>
    <script>
        // Devuelve un número entre 1 y 3, aleatoreamente
        function aleatorios( min, max){
            return Math.floor(Math.random() * (max - min + 1) + min);
        }

        /* Devuelve el tipo de jugada codigo re factorizado de:         /* Seleccion de piedra, papel, tijera
        if (jugador == 1) {
            alert("Elegiste 🪨")
        } else if (jugador == 2) {
            alert("Elegiste 🧻")
        } else if (jugador == 3) {
            alert("Elegiste ✂️")
        } else  {
            alert("Opción invalida")
        }

        if (computador == 1) {
            alert("PC elige 🪨")
        } else if (computador == 2) {
            alert("PC elige 🧻")
        } else if (computador == 3) {
            alert("PC elige ✂️")
        } else  {
            alert("Opción invalida")
        }*/
        function eleccion ( jugada ){
            let resultado = ""
            if (jugada == 1) {
                resultado = "Piedra 🪨"
            } else if (jugada == 2) {
                resultado = "Papel 🧻"
            } else if (jugada == 3) {
                resultado = "Tijera ✂️"
            } else  {
                alert("Opción invalida")
            }
            return resultado
        }

        // 1 es piedra, 2 es papel o 3 es tijera
        let jugador = 0
        let computador = aleatorios(1, 3)
        jugador = prompt("Por favor Elige 1 es para piedra, 2 es para papel o 3 es para tijera")

        alert("Pc elige: " + eleccion(computador))
        alert("Tu elegiste: " + eleccion(jugador))

        // Comparación jugador vs computador
        if (jugador == computador) {
            alert("Empate!")
        } else if (
            (jugador == 1 && computador == 3) ||
            (jugador == 2 && computador == 1) ||
            (jugador == 3 && computador == 2)
        ) {
            alert("Ganaste!")
        } else {
            alert("Perdiste!")
        }

    </script>
</head>
<body>
    
</body>
</html>
