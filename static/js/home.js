
	var userAction = async (selection) => {
		await fetch("color", {
			method: 'POST',
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ color: selection })
		});
	}
	var btnContainer = document.getElementById("buttonContainer");

	var btns = btnContainer.getElementsByClassName("list-group-item list-group-item-action");

	// Loop through the buttons and add the active class to the current/clicked button
	for (var i = 0; i < btns.length; i++) {
		btns[i].addEventListener("click", function () {
			var current = document.getElementsByClassName("active");

			// If there's no active class
			if (current.length > 0) {
				current[0].className = current[0].className.replace(" active", "");
			}

			// Add the active class to the current/clicked button
			if (this.innerHTML != "Clear"){
				this.className += " active";
			}

			userAction(this.innerHTML).then(res => {
				console.log(this.innerHTML);
			}
			)
		});
	}