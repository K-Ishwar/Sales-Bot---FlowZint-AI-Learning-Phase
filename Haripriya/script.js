async function getUser() {
    try {
        const response =
        await fetch(
            "https://api.github.com/users/haripriyaBurase"
        );

        const data =
        await response.json();
        console.log(data);

        document.getElementById("result")
        .innerHTML = `
            <h3>${data.login}</h3>
            <p>ID: ${data.id}</p>
            <p>Followers: ${data.followers}</p>
            <a href="${data.html_url}" target="_blank">
                View Profile
             </a>
        `;

    }
    catch(error){

        document.getElementById("result")
        .innerHTML =
        "<p>Something went wrong!</p>";

        console.log(error);

    }

}

    function allowDrop(e){
        e.preventDefault();
    }
    function drag(e) {
        e.dataTransfer.setData("text",e.target.id);
    }
    function drop(e) {
        e.preventDefault();
        let data= e.dataTransfer.getData("text");
        e.target.appendChild(document.getElementById(data));
    }