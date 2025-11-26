const getresponsebtn = document.getElementById('send-response');

getresponsebtn.addEventListener('click', () => {
    textToAnalyze = document.getElementById('user-text').value;

    let xml = new XMLHttpRequest();
    xml.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            document.getElementById('results').innerHTML = JSON.parse(xml.responseText);
        }
    };

    xml.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xml.send();
});
