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
        setInterval(checkData, 5000);
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
      }
    } catch (error) {
      console.error(error.message);
    }
        }