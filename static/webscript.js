const getresponsebtn = document.getElementById('send-response');

getresponsebtn.addEventListener('click', () => {
    sendHttpRequest();
});

addEventListener('keydown', (e) => {
    if (e.code === "Enter"){
        sendHttpRequest();
    }
})
   

function sendHttpRequest() {
    textToAnalyze = document.getElementById('user-text').value;

    let xml = new XMLHttpRequest();
    xml.onreadystatechange = function() {
        if (this.readyState == 4){
            if (this.status == 200){
                
                const respobj = JSON.parse(xml.responseText);
                //scores is an object within an object so we need to extract it
                const respobjscores = respobj.scores;

                let text = '';
                for (const emotion in respobjscores){
                    text+= `<span> <em>${emotion} </em> </span>: ${respobjscores[emotion]} <br>`;
                }
                
                document.getElementById('results').innerHTML = `<p style="color: green;"> For the given text: <span style="font-weight: bold;"> ${respobj.input} </span><br><br>
                The system response is <br> <br> ${text} <br> 
                The Dominant Emotion is ${respobj.dominant_emotion}! </p>`
            }
            if (this.status == 400){
                document.getElementById('results').innerHTML = `<span style="color: red; font-weight: bold;"> ${xml.responseText} </span>`;
            }
        }
    }
    document.getElementById("user-text").value = '';

    xml.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xml.send();
};

