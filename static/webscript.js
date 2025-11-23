const getresponsebtn = document.getElementById('send-response');
const textToAnalyze = document.getElementById('user-text').value;

getresponsebtn.addEventListener('click', () => {
    
    const xml = new XMLHttpRequest();
    xml.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){

            document.getElementById('results').innerHTML = xml.response.Text;
            }
    };

    xml.open("GET", "emotionDetector?textToAnalyze"+"="+ `${textToAnalyze}`);
    xml.send();
});
