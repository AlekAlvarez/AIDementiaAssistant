        const languages = [];

        function addLanguage() {
            const newLanguage = document.getElementById('new-language').value.trim();
            if (newLanguage && !languages.includes(newLanguage)) {
                languages.push(newLanguage);
                document.getElementById('language-list').value = languages.map(lang => `• ${lang}`).join('\n');
                document.getElementById('new-language').value = "";
            } else {
                alert("Language already exists or is empty.");
            }
        }

        function saveInfo() {
            const patientData = {
                patientName: document.getElementById('patient-name').value.trim(),
                familyMembers: document.getElementById('family-members').value.trim(),
                medications: document.getElementById('medications').value.trim(),
                hobbies: document.getElementById('hobbies').value.trim(),
                languagesSpoken: languages,
                modificationRequest: document.getElementById('modification-request').value.trim(),
                mood: document.getElementById('mood').value.trim().toLowerCase()
            };
            const jsonData = JSON.stringify(patientData, null, 2);
            fetch('/DataToServer',{
                method:'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body:jsonData
            })
            alert("Data is Saved To Server");
        }
        setInterval(checkData, 500);
        async function checkData(){
            const url = "http://localhost:5000/DataToPortal";
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      
      const json = await response.json();
      if(json["modificationRequest"]!="" ){
        document.getElementById('modification-request').value+=json[modificationRequest];
      }
        if(json["mood"]!=""){
            document.getElementById('mood').value=json["mood"]
            if(json["mood"]=='Disturbed'){
              alert("The patient is disturbed")
            }
      }
    } catch (error) {
      console.error(error.message);
    }
        }
        function setUpLanguages(){
            for(let i=0;i<languages.length;i++){
                document.getElementById('language-list').value+=languages[i]+'\n'
            }
        }
        window.addEventListener('load', async function pageLoadFunction() {
            const url = "http://localhost:5000/loadData";
    try {
        console.log("hi")
      const response = await fetch(url);
      console.log("a")
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      
      const json = await response.json();
      console.log("b")
      this.document.getElementById('patient-name').value=json['patientName'];
       document.getElementById('family-members').value=json["familyMembers"];console.log("b")
       document.getElementById('medications').value=json["medications"];console.log("b")
            document.getElementById('hobbies').value=json["hobbies"];console.log("b")
            if (Array.isArray(json["languagesSpoken"])) {
                document.getElementById('languages').value = json["languagesSpoken"].join(", "); // Assuming you want to display them as a comma-separated list
              }
                document.getElementById('modification-request').value=json["modificationRequest"];console.log("b")
                document.getElementById('mood').value=json['mood'];console.log("b")
    } catch (error) {
      console.error(error.message);
    }
            window.removeEventListener('load', pageLoadFunction);
          });