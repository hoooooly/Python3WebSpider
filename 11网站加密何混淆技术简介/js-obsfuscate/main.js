const code = `
    let = '1' +1
    console.log('x', x)
`

const options = {
    compact: true, // 代码压缩
    controlFlowFlattening: true  //控制流平坦化
}

const obfuscator = require('javascript-obfuscator')

function obfuscate(code, options) {
    return obfuscator.obfuscate(code, options).getObfuscatedCode()
}

console.log(obfuscate(code, options))