function login(){
    const userData={
        username:document.getElementById('username').value.trim(),
        hashed_password:document.getElementById('password').value.trim()
    }
    const jsonData = JSON.stringify(userData, null, 2);
            a=fetch('/login',{
                method:'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body:jsonData
            })
            console.log(a)
            console.log("AA")
    alert(username+password)
}