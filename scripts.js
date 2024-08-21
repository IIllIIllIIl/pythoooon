function changeName() {
      const name = document.querySelector("#input_name").value;
      const nameElements = document.querySelectorAll("#myname");


      // 각 요소에 대해 텍스트 변경
      nameElements.forEach(element => {
          element.innerText = name;
      });
  }
  document.getElementById("changeButton").addEventListener("click", changeName);