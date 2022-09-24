const {stdout} = require('process')
const spawn = require('child_process').spawn
const path = require('path');

let text = 'some new text';

function setText(input){
    return text = {'text': input}
}


let stringifiedData = JSON.stringify({'text': text});

let hellopath = path.resolve('../', 'py', 'helloworld.py');

const py = spawn('python', [hellopath, stringifiedData]);

let resultString = '';

py.stdout.on('data', (stdData) =>{
    resultString += stdData.toString();
});

py.stdout.on('end', ()=>{
    let resultData = JSON.parse(resultString);
    let text = resultData['result'];
    console.log('You wrote :', text);
})

// export default setText;