function PyScripts_with_Nodejs_runner(dir){
    const {PythonShell} = require("python-shell");

    let pyshell = new PythonShell(dir)

    pyshell.on('message',(message) => console.log(message))

    pyshell.end((err)=> {(err)? console.log(err) : console.log('finsihed') } )
}

module.exports = PyScripts_with_Nodejs_runner