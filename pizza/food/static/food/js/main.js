var hours = 24
var now = new.Data.getTime();
var stepTime = localStorage.getItem('stepTime');

if (stepTime == null) {
    localStorage.setItem('stepTime', now);
}
else{
    if(now - stepTime > hours*60*60*1000){
        localStorage.clear();
        localStorage.setItem('stepItem', now);
    }
}