// SLide form page
const slidePage = document.querySelector(".slide-page");
const nextBtnFirst = document.querySelector(".firstNext");
const prevBtnSec = document.querySelector(".prev-1");
const nextBtnSec = document.querySelector(".next-1");
const prevBtnThird = document.querySelector(".prev-2");
const nextBtnThird = document.querySelector(".next-2");
const prevBtnFourth = document.querySelector(".prev-3");
const nextBtnFourth = document.querySelector(".next-3");
const prevBtnFifth = document.querySelector(".prev-4");
const progressText = document.querySelectorAll(".step p");
const progressCheck = document.querySelectorAll(".step .check");
const bullet = document.querySelectorAll(".step .bullet");
let current = 1;


nextBtnFirst.addEventListener("click", function(event){
  event.preventDefault();
// Hairstylist Validation
  hairstylistValidation();
  slidePage.style.marginLeft = "-25%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});
nextBtnSec.addEventListener("click", function(event){
  event.preventDefault();
// Date and Time Validation
  DateTimeValidation();
  slidePage.style.marginLeft = "-50%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});
nextBtnThird.addEventListener("click", function(event){
  event.preventDefault();
// Functions below
//  getCheckboxValue();
  checkboxValidation();
  slidePage.style.marginLeft = "-75%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});
nextBtnFourth.addEventListener("click", function(event){
  event.preventDefault();
  slidePage.style.marginLeft = "-100%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});

prevBtnSec.addEventListener("click", function(event){
  event.preventDefault();
  slidePage.style.marginLeft = "0%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});
prevBtnThird.addEventListener("click", function(event){
  event.preventDefault();
  slidePage.style.marginLeft = "-25%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});
prevBtnFourth.addEventListener("click", function(event){
  event.preventDefault();
  slidePage.style.marginLeft = "-50%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});
prevBtnFifth.addEventListener("click", function(event){
  event.preventDefault();
  slidePage.style.marginLeft = "-75%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});


// calculate price
function totalPrice() {
  var input = document.getElementsByName("service");
  var total = 0;
  for (var i = 0; i < input.length; i++) {
    if (input[i].checked) {
      total += parseFloat(input[i].value);
    };
  };
  document.getElementById("total").innerHTML = total.toFixed(2);
};


// Alert
const c4 = document.getElementById("service-3")
const c5 = document.getElementById("service-4")
const c1 = document.getElementById("service-0")
const c2 = document.getElementById("service-1")
const c3 = document.getElementById("service-2")

function getCheckboxValue() {
    if (c4.checked == true && c5.checked == true){
        alert("We regret to inform you that straightening and perming of hair are not to be done in the same appointment.");
        script.stop;
    };
};

// Hairstylist Validation
function hairstylistValidation() {
    var hairstylist = document.getElementById('hairstylist')
    if(hairstylist.value) {
        document.getElementById("hairstylist_error").style.visibility = "hidden";
        return true;
    }
    else {
        document.getElementById("hairstylist_error").style.visibility = "visible";
        script.stop;
        return false;
    };
};

// Date and Time Validation
function DateTimeValidation() {
    var date = document.getElementById('date');
    var time = document.getElementById('time')
    if(date.value == false) {
        document.getElementById('dateORtime').innerText = 'date'
        document.getElementById("schedule_error").style.visibility = "visible";
        script.stop;
        return false;
    } else if (time.value == false) {
        document.getElementById('dateORtime').innerText = 'time'
        document.getElementById("schedule_error").style.visibility = "visible";
        script.stop;
        return false;
    }
    else {
        document.getElementById("schedule_error").style.visibility = "hidden";
        return true;
    };
};

// Checkbox Validation
function checkboxValidation() {
    price = document.getElementById("total").innerText
    if(price == "0.00") {
        document.getElementById("chk_option_error").style.visibility = "visible";
        script.stop;
        return false;
    }
    else {
        document.getElementById("chk_option_error").style.visibility = "hidden";
        return true;
    };
};

document.getElementById('date').min = new Date().toISOString().split("T")[0];


function showInput() {
        document.getElementById('summary1').innerHTML =
                    document.getElementById("hairstylist").value;
        document.getElementById('summary2').innerHTML =
                    document.getElementById("date").value;
        document.getElementById('summary3').innerHTML =
                    document.getElementById("time").value;
        document.getElementById('summary4').innerHTML =
                    document.getElementById("total").innerText;
        document.getElementById('summary5').innerHTML =
                    document.getElementById("remarks").value;

    }
