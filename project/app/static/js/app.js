// window.addEventListener("load", function () {
//    fetch("/app/module", { method: "POST" })
//      .then((response) => response.text())
//      .then((data) => {
//        let myObj = JSON.parse(data);
//        if (myObj.status === "error") {
//          Toastify({
//            text: myObj.message,
//            duration: 3000,
//            close: true,
//            gravity: "top",
//            position: "center",
//            stopOnFocus: true,
//            style: {
//              background: "#dc3545",
//              color: "#fff",
//            },
//            onClick: function () {},
//          }).showToast();
//        } else {
//          Toastify({
//            text: myObj.message,
//            duration: 3000,
//            close: true,
//            gravity: "top",
//            position: "center",
//            stopOnFocus: true,
//            style: {
//              background: "#28a745",
//              color: "#fff",
//            },
//            onClick: function () {},
//          }).showToast();
//        }
    
//     })})