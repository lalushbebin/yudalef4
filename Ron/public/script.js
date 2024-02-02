var elements = document.getElementById('CodeArea').children

for (let index = 0; index < elements.length; index++) {
    elements[index].children[0].addEventListener("keyup", (ev) => {
        if (index == elements.length - 1)
            return;

        GoToNext(index)
    });
    elements[index].children[0].addEventListener("focus", () => GoToNext(index) );

    elements[index].children[0].addEventListener("keydown", (ev) => {
        if (index > 0 && ev.keyCode == 8) {
            if (elements[index].children[0].value && elements[index].children[0].value.length > 0) return console.log("test");
            
            document.querySelector("#CodeArea #n" + (index - 1)).value = ""
            return document.querySelector("#CodeArea #n" + (index - 1)).focus()
        }
    })
}

function GoToNext(index) {
    // Number 13 is the "Enter" key on the keyboard
    
    if (elements[index].children[0].value && elements[index].children[0].value.length == 1) {
        // Focus on the next sibling
        document.querySelector("#CodeArea #n" + (index + 1)).focus()
    }
}

function submit() {
    code = ""

    for (let index = 0; index < elements.length; index++) {
        code += elements[index].children[0].value;
    }

    console.log("test")

    fetch("/code", {
        method: "POST",
        body: JSON.stringify({
            "code": code
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((response) => response.json())
    .then((json) => console.log(json));
}