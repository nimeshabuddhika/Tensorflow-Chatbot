
var month;
var day;
var year;
var weekId;

function getTodayDateId() {
    var date = new Date();
    month = date.getMonth() + 1;
    day = date.getDate();
    if (day < 10)
        day = "0" + day;
    if (month < 10)
        month = "0" + month;
    var start = date.getFullYear() + "" + month + "" + day;
    return parseInt(start);
}

function getTodayDate() {
    var date = new Date();
    month = date.getMonth() + 1;
    day = date.getDate();
    if (day < 10)
        day = "0" + day;
    if (month < 10)
        month = "0" + month;
    var year = date.getFullYear() + "-" + month + "-" + day;
    return year;
}
function difDates(first, second) {
    return Math.round((new Date(second) - new Date(first)) / (1000 * 60 * 60 * 24));
}
function getDate(add) {
    var endDate = new Date();
    endDate.setDate(endDate.getDate() + add);
    month = endDate.getMonth() + 1;
    day = endDate.getDate();
    if (day < 10)
        day = "0" + day;

    if (month < 10)
        month = "0" + month;

    var start = endDate.getFullYear() + "" + month + "" + day;
    return parseInt(start);
}

function getDateById(date) {//20170722 => 2017-07-22
    day = "-" + date.substring(6, 8);
    month = "-" + date.substring(4, 6);
    year = date.substring(0, 4);
    return year + month + day;
}

function getDateId(date) { //2017-07-22 => 20170722
    date = date.replace("-","");
    return parseInt(date.replace("-", ""));
}

function isValidDate(date) {
    return getTodayDateId() <= date;
}

function addDays(days) {
    var date = new Date();
    date.setDate(date.getDate() + days);
    month = date.getMonth() + 1;
    day = date.getDate();
    if (day < 10)
        day = "0" + day;
    if (month < 10)
        month = "0" + month;
    var year = date.getFullYear() + "-" + month + "-" + day;
    return year;
}

function addDaysTo(today, days) {
    var date = new Date(today);
    date.setDate(date.getDate() + days);
    month = date.getMonth() + 1;
    day = date.getDate();
    if (day < 10)
        day = "0" + day;
    if (month < 10)
        month = "0" + month;
    var year = date.getFullYear() + "-" + month + "-" + day;
    return year;
}

function getWeekDay(day) { //20171218 => 1 (Monday == 1)
    return new Date(getDateById(day)).getDay();
}

function getWeekDayIs(day,arr) { //20171218,[1,2 .. 6] => true
    weekId = new Date(getDateById(day)).getDay();
    var state = false;
    arr.forEach(function(date) {
        if (date == weekId) {
            state =  true;
        }
            
    });
    return state;
}

function formatDate(date) { //20171219 => Tuesday December 19 2017
    var month = [
        "January", "February", "March",
        "April", "May", "June", "July",
        "August", "September", "October",
        "November", "December"
    ];

    var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    date = new Date(getDateById(date));
    return days[date.getDay()] + ", " + month[date.getMonth()] + " " + date.getDate() + " " + date.getFullYear();
}