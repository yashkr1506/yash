<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday, Love!</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            background-color: #f9f3f3;
            overflow: hidden;
        }

        h1 {
            font-size: 60px;
            color: #ff4081;
            text-align: center;
            margin-top: 50px;
        }

        #surpriseButton {
            display: block;
            margin: 30px auto;
            padding: 15px 30px;
            background-color: #ff4081;
            color: white;
            font-size: 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            animation: pulse 1.5s infinite;
        }

        #surpriseButton:hover {
            background-color: #c2185b;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }

        .hidden-section {
            display: none;
            text-align: center;
        }

        .message {
            margin-top: 20px;
            font-size: 28px;
            color: #e91e63;
        }

        .gallery {
            margin-top: 40px;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }

        .gallery img {
            margin: 10px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            width: 200px;
            height: 150px;
        }

        /* Floating hearts */
        .heart {
            position: fixed;
            width: 30px;
            height: 30px;
            background-color: #ff80ab;
            animation: float 10s infinite ease-in-out;
            border-radius: 50% 50% 0 0;
            transform: rotate(-45deg);
        }

        .heart:before {
            content: '';
            position: absolute;
            width: 30px;
            height: 30px;
            background-color: #ff80ab;
            border-radius: 50%;
            top: -15px;
            left: 0;
        }

        .heart:after {
            content: '';
            position: absolute;
            width: 30px;
            height: 30px;
            background-color: #ff80ab;
            border-radius: 50%;
            left: 15px;
            top: 0;
        }

        @keyframes float {
            0% { transform: translateY(0) rotate(-45deg); }
            50% { transform: translateY(-300px) rotate(-45deg); }
            100% { transform: translateY(0) rotate(-45deg); }
        }

        /* Multiple floating hearts */
        .heart1 { left: 20%; animation-duration: 8s; }
        .heart2 { left: 40%; animation-duration: 10s; }
        .heart3 { left: 60%; animation-duration: 12s; }
        .heart4 { left: 80%; animation-duration: 9s; }
    </style>
</head>
<body>

    <h1>Happy Birthday, Beautiful!</h1>

    <button id="surpriseButton">Click for a Surprise!</button>

    <!-- Hidden Section -->
    <div class="hidden-section" id="surpriseSection">
        <div class="message">
            <p>You make my world brighter every day. Here’s to us, my love! ❤️</p>
            <p>I hope this day is as special as you are!</p>
        </div>

        <!-- Gallery -->
        <div class="gallery">
            <img src="memory1.jpg" alt="Memory 1">
            <img src="memory2.jpg" alt="Memory 2">
            <img src="memory3.jpg" alt="Memory 3">
            <img src="memory4.jpg" alt="Memory 4">
        </div>

        <!-- Birthday Song -->
        <audio id="birthdaySong" src="birthday-song.mp3"></audio>
    </div>

    <!-- Floating Hearts -->
    <div class="heart heart1"></div>
    <div class="heart heart2"></div>
    <div class="heart heart3"></div>
    <div class="heart heart4"></div>

    <script>
        const surpriseButton = document.getElementById("surpriseButton");
        const surpriseSection = document.getElementById("surpriseSection");
        const birthdaySong = document.getElementById("birthdaySong");

        // When the button is clicked, reveal the surprise section and play the song
        surpriseButton.addEventListener("click", function() {
            surpriseSection.style.display = "block";
            birthdaySong.play();
            surpriseButton.style.display = "none"; // Hide the button after click
        });
    </script>

</body>
</html>
