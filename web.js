const PyScripts_with_Nodejs_runner = require("./lib")
const path = require('path')
// Back Button
back_btn = document.getElementsByClassName('back_btn')
back_btn[0].addEventListener('click',()=>location.href='./index.html')

box1 = document.getElementsByClassName('box1')[0]
box2 = document.getElementsByClassName('box2')[0]
box3 = document.getElementsByClassName('box3')[0]
box4 = document.getElementsByClassName('box4')[0]


box1.addEventListener('click',()=>PyScripts_with_Nodejs_runner(path.join(__dirname,'python_scripts/websites/web1.py')))
box2.addEventListener('click',()=>PyScripts_with_Nodejs_runner(path.join(__dirname,'python_scripts/websites/web2.py')))
box3.addEventListener('click',()=>PyScripts_with_Nodejs_runner(path.join(__dirname,'python_scripts/websites/web3.py')))
box4.addEventListener('click',()=>PyScripts_with_Nodejs_runner(path.join(__dirname,'python_scripts/websites/web3.1.py')))