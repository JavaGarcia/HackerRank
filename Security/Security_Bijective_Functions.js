/*Security Bijective Functions
Javier Garcia
*/
function processData(input) {
    var n = parseInt(input.split('\n')[0]);
    var f = input.split('\n')[1].split(' ');
    var o = [];

        for(var i = 0; i < f.length; i++){
            if(o.indexOf(f[i]) >= 0){
                console.log('NO');
                return(null);
            }else{
                o.push(f[i]);
            }
        }
        console.log('YES');
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
