const video = document.getElementById("video-element");
let click_button = document.getElementById("click-photo");
console.log('hey')
let canvas = document.querySelector("canvas");



function support() {
    console.log('inside canvas')
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    let image_data_url = canvas.toDataURL('');
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    emoji = { 'Angry': '&#128544;', 'Disgust': '&#129314;', 'Fear': '&#128561;', 'Happy': '&#128516;', 'Neutral': '&#128528;', 'Sad': '&#128549;', 'Surprise': '&#128562;' }

    var raw = JSON.stringify({
        "s": image_data_url,
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    const predictedEmoji = document.getElementById('predictedEmoji')
    const predictedExp = document.getElementById('predictedExp')
    console.log('predictedexp', predictedExp)
        // predictedEmoji.innerHTML = emoji['Angry']
    predictedExp.innerText = 'Pending....';
    fetch("http://127.0.0.1:8000/prediction/?s=shdsa", requestOptions)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            console.log(emoji[result.prediction])
            if (result.prediction == null) {
                predictedExp.innerText = 'No Face Detected try again';
                predictedEmoji.innerHTML = '&#8987;';
            } else {
                predictedEmoji.innerHTML = emoji[result.prediction];
                predictedExp.innerText = result.prediction;
                console.log(predictedExp)
            }


        })
        .catch(error => console.log('error', error));
}

console.log("video=>", video)
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        console.log(stream);
        video.srcObject = stream
    })
}



// click_button.addEventListener("click", function() {
//     support();
// });



setInterval(function() { support() }, 1000);