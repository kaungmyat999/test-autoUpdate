
dir = "../../Python/Selenium_Testing/yt1.py"
const path = require('path');
const PyScripts_with_Nodejs_runner = require('./lib');

console.log(__dirname);
document.getElementById("btn1").onclick = ()=>PyScripts_with_Nodejs_runner(path.join(__dirname,'python_scripts/youtube/yt3.py'));
document.getElementById("btn2").onclick = ()=>PyScripts_with_Nodejs_runner(path.join(__dirname,'python_scripts/youtube/yt2.py'));
document.getElementById("btn3").onclick = ()=>PyScripts_with_Nodejs_runner(path.join(__dirname,'python_scripts/youtube/yt1.py'));


back_btn = document.getElementById('back_btn')
back_btn.addEventListener('click',()=>location.href='./index.html')