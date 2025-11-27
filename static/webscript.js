const getresponsebtn = document.getElementById('send-response');

getresponsebtn.addEventListener('click', () => {
    sendHttpRequest();
});

addEventListener('keydown', (e) => {
    if (e.code === "Enter"){
        sendHttpRequest();
    }
} )
   

function sendHttpRequest() {
    textToAnalyze = document.getElementById('user-text').value;

    let xml = new XMLHttpRequest();
    xml.onreadystatechange = function() {
        if (this.readyState == 4){
            if (this.status == 200){
                document.getElementById('results').innerHTML = xml.responseText;
            }
            if (this.status == 400){
                document.getElementById('results').innerHTML = xml.responseText;
            }
        }
    }

    xml.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xml.send();
};

