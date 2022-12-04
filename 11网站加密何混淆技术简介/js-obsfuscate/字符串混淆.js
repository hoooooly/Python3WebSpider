const code = `
  var a = 'hello world
  
`

const options = {
    stringArray: true,
    rotateStringArray: true,
    stringArrayEncoding: true,
    stringArrayThreshold: 1,
    // compact: true, // 代码压缩
    // identifierNamesGenerator: 'hexadecimal' // mangled
}

const obfuscator = require('javascript-obfuscator')

function obfuscate(code, options) {
    return obfuscator.obfuscate(code, options).getObfuscatedCode()
}

console.log(obfuscate(code, options))